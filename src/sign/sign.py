#!/usr/bin/env python3
"""
PDF Signatur mit PNG und PDF Support
Unterstützt PNG, JPG und PDF als Signatur-Dateien
Benötigt: pip install pypdf pillow reportlab
"""

import os
import tempfile

from PIL import Image
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas


class PDFSigner:
    def __init__(self):
        # Umrechnungsfaktoren zu PDF-Punkten (1 Punkt = 1/72 Zoll)
        self.POINTS_PER_INCH = 72
        self.POINTS_PER_CM = 72 / 2.54  # ~28.35 Punkte pro cm
        self.POINTS_PER_MM = self.POINTS_PER_CM / 10  # ~2.835 Punkte pro mm
        self.POINTS_PER_PIXEL = 1  # Annahme: 72 DPI (1 Pixel = 1 Punkt)

    def convert_to_points(self, value, unit="points"):
        unit = unit.lower()
        if unit in ["points", "pt"]:
            return float(value)
        elif unit in ["px", "pixel"]:
            return float(value) * self.POINTS_PER_PIXEL
        elif unit == "cm":
            return float(value) * self.POINTS_PER_CM
        elif unit == "mm":
            return float(value) * self.POINTS_PER_MM
        elif unit in ["inch", "in"]:
            return float(value) * self.POINTS_PER_INCH
        else:
            raise ValueError(
                f"Unbekannte Einheit: {unit}. Verwende: points, px, cm, mm, inch"
            )

    def get_page_dimensions(self, pdf_path, page_number=1):
        try:
            reader = PdfReader(pdf_path)
            page = reader.pages[page_number - 1]
            width_pt = float(page.mediabox.width)
            height_pt = float(page.mediabox.height)
            width_cm = width_pt / self.POINTS_PER_CM
            height_cm = height_pt / self.POINTS_PER_CM
            return width_pt, height_pt, width_cm, height_cm
        except Exception as e:
            print(f"❌ Fehler beim Lesen der Seitendimensionen: {e}")
            return None

    def prepare_image(self, image_path, out_path):
        """Speichert das Bild als sauberes PNG ohne Transparenz"""
        try:
            img = Image.open(image_path)
            if img.mode in ("RGBA", "LA"):
                background = Image.new("RGB", img.size, (255, 255, 255))
                background.paste(img, mask=img.split()[-1])
                img = background
            elif img.mode != "RGB":
                img = img.convert("RGB")
            img.save(out_path, "PNG")
            return out_path, img.size  # Pixelmaße zurückgeben
        except Exception as e:
            print(f"❌ Fehler bei Bildvorbereitung: {e}")
            return None, None

    def add_signature_precise(
        self,
        input_pdf,
        signature_file,
        output_pdf,
        page_number=1,
        x=0,
        y=0,
        x_unit="cm",
        y_unit="cm",
        origin="bottom-left",
        scale=1.0,  # <--- neuer Parameter
    ):
        """Fügt eine Signatur (Bild) mit optionaler gleichmäßiger Skalierung ein"""
        try:
            # Seitengröße auslesen
            dimensions = self.get_page_dimensions(input_pdf, page_number)
            if not dimensions:
                return False
            page_width_pt, page_height_pt, page_width_cm, page_height_cm = dimensions

            # Koordinaten berechnen
            x_points = self.convert_to_points(x, x_unit)
            y_points = self.convert_to_points(y, y_unit)

            # Bild vorbereiten und Größe in Pixeln lesen
            temp_img = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
            prepared_img, (img_width_px, img_height_px) = self.prepare_image(
                signature_file, temp_img.name
            )
            temp_img.close()
            if prepared_img is None:
                return False

            # Originalgröße in PDF-Punkten
            sig_width = img_width_px * self.POINTS_PER_PIXEL * scale
            sig_height = img_height_px * self.POINTS_PER_PIXEL * scale

            # Ursprung beachten
            if origin == "top-left":
                y_points = page_height_pt - y_points - sig_height
            elif origin == "center":
                x_points = (page_width_pt / 2) + x_points
                y_points = (page_height_pt / 2) + y_points

            print(
                f"📄 Seite {page_number}: {page_width_cm:.1f} x {page_height_cm:.1f} cm"
            )
            print(f"📍 Signatur an Position ({x_points:.1f}, {y_points:.1f}) Punkte")
            print(
                f"📐 Signaturgröße: {sig_width:.1f} x {sig_height:.1f} Punkte (Skalierung {scale:.2f})"
            )

            # Overlay-PDF mit Signatur erzeugen
            temp_overlay = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)
            c = canvas.Canvas(
                temp_overlay.name, pagesize=(page_width_pt, page_height_pt)
            )
            c.drawImage(
                prepared_img,
                x_points,
                y_points,
                width=sig_width,
                height=sig_height,
                mask="auto",
            )
            c.save()

            # Haupt-PDF laden und mergen
            reader = PdfReader(input_pdf)
            writer = PdfWriter()
            with open(temp_overlay.name, "rb") as overlay_file:
                overlay_pdf = PdfReader(overlay_file)
                overlay_page = overlay_pdf.pages[0]

                for i, page in enumerate(reader.pages):
                    if i == page_number - 1:
                        page.merge_page(overlay_page)
                    writer.add_page(page)

            with open(output_pdf, "wb") as out_file:
                writer.write(out_file)

            os.unlink(temp_overlay.name)
            os.unlink(prepared_img)

            print(f"✅ Signatur erfolgreich eingefügt: {output_pdf}")
            return True

        except Exception as e:
            print(f"❌ Fehler: {e}")
            return False


def main():
    signer = PDFSigner()

    print("=== Signierung ===")
    signer.add_signature_precise(
        input_pdf="Hausverbot.pdf",
        signature_file="Unterschrift.png",
        output_pdf="Hausverbot-sign.pdf",
        page_number=2,
        x=2.0,
        y=5.0,
        x_unit="cm",
        y_unit="cm",
        origin="top-left",  # "bottom-left" oder "center"
        scale=0.4,  # <- z.B. 0.5 für 50% oder 2.0 für 200%
    )


if __name__ == "__main__":
    main()
