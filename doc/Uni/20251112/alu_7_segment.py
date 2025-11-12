"""
ALU with 7-Segment Display
Amaranth HDL Implementation

Author: Generated from VHDL reference
Description: Arithmetic Logic Unit with 7-segment display output
"""

from amaranth import Elaboratable, Module, Signal, Mux, ClockDomain
from amaranth.build import Platform
from amaranth.back import verilog


class SevenSegmentDecoder(Elaboratable):
    """Decoder für 4-Bit Wert zu 7-Segment Anzeige"""
    
    def __init__(self):
        # Eingabe: 4-Bit Wert
        self.digit = Signal(4)
        # Ausgabe: 7 Segmente (active low für common anode)
        self.segments = Signal(7)
    
    def elaborate(self, platform):
        module = Module()
        
        # 7-Segment Dekodierung (gfedcba)
        # Active LOW für common anode Display
        with module.Switch(self.digit):
            with module.Case(0x0):
                module.d.comb += self.segments.eq(0b1000000)  # 0
            with module.Case(0x1):
                module.d.comb += self.segments.eq(0b1111001)  # 1
            with module.Case(0x2):
                module.d.comb += self.segments.eq(0b0100100)  # 2
            with module.Case(0x3):
                module.d.comb += self.segments.eq(0b0110000)  # 3
            with module.Case(0x4):
                module.d.comb += self.segments.eq(0b0011001)  # 4
            with module.Case(0x5):
                module.d.comb += self.segments.eq(0b0010010)  # 5
            with module.Case(0x6):
                module.d.comb += self.segments.eq(0b0000010)  # 6
            with module.Case(0x7):
                module.d.comb += self.segments.eq(0b1111000)  # 7
            with module.Case(0x8):
                module.d.comb += self.segments.eq(0b0000000)  # 8
            with module.Case(0x9):
                module.d.comb += self.segments.eq(0b0010000)  # 9
            with module.Case(0xA):
                module.d.comb += self.segments.eq(0b0001000)  # A
            with module.Case(0xB):
                module.d.comb += self.segments.eq(0b0000011)  # b
            with module.Case(0xC):
                module.d.comb += self.segments.eq(0b1000110)  # C
            with module.Case(0xD):
                module.d.comb += self.segments.eq(0b0100001)  # d
            with module.Case(0xE):
                module.d.comb += self.segments.eq(0b0000110)  # E
            with module.Case(0xF):
                module.d.comb += self.segments.eq(0b0001110)  # F
            with module.Default():
                module.d.comb += self.segments.eq(0b1111111)  # blank
        
        return module


class ALU(Elaboratable):
    """Arithmetic Logic Unit"""
    
    # Operation Codes
    OP_ADD = 0b0000   # A + B
    OP_SUB = 0b0001   # A - B
    OP_MULT = 0b0010  # A * B
    OP_DIV = 0b0011   # A / B
    OP_AND = 0b0100   # A and B
    OP_OR = 0b0101    # A or B
    
    def __init__(self):
        # Eingänge
        self.a = Signal(4)
        self.b = Signal(4)
        self.control = Signal(4)
        
        # Ausgang
        self.result = Signal(8)
    
    def elaborate(self, platform):
        module = Module()
        
        # Erweitere Eingänge auf 8 Bit
        a_extended = Signal(8)
        b_extended = Signal(8)
        
        module.d.comb += [
            a_extended.eq(self.a),
            b_extended.eq(self.b)
        ]
        
        # ALU Operationen
        with module.Switch(self.control):
            with module.Case(self.OP_ADD):
                # Addition
                module.d.comb += self.result.eq(a_extended + b_extended)
            
            with module.Case(self.OP_SUB):
                # Subtraktion (clamp auf 0 bei negativem Ergebnis)
                subtraction = Signal(9, name="subtraction")
                module.d.comb += subtraction.eq(a_extended - b_extended)
                
                # Prüfe ob negativ (MSB = 1)
                with module.If(subtraction[8]):
                    module.d.comb += self.result.eq(0)
                with module.Else():
                    module.d.comb += self.result.eq(subtraction[:8])
            
            with module.Case(self.OP_MULT):
                # Multiplikation
                module.d.comb += self.result.eq(self.a * self.b)
            
            with module.Case(self.OP_DIV):
                # Division
                with module.If(b_extended == 0):
                    # Division durch 0 -> Zeige FF
                    module.d.comb += self.result.eq(0xFF)
                with module.Else():
                    module.d.comb += self.result.eq(a_extended // b_extended)
            
            with module.Case(self.OP_AND):
                # Bitweises AND
                module.d.comb += self.result.eq(a_extended & b_extended)
            
            with module.Case(self.OP_OR):
                # Bitweises OR
                module.d.comb += self.result.eq(a_extended | b_extended)
            
            with module.Default():
                # Undefinierte Operationen -> 0
                module.d.comb += self.result.eq(0)
        
        return module


class ALU7Segment(Elaboratable):
    """
    ALU mit 7-Segment Display Ausgabe
    
    Ports:
        clock: 100 MHz Takt
        switches: 16 Schalter (15:12 = Control, 7:4 = A, 3:0 = B)
        segments: 7-Segment Anzeige Segmente
        anodes: 7-Segment Anzeige Anoden
    """
    
    # Refresh-Rate Konstante
    # 100MHz / 100000 = 1kHz refresh rate (250Hz pro Digit)
    REFRESH_COUNT = 100000
    
    def __init__(self):
        # Eingänge (Port-Namen wie in VHDL für Äquivalenz-Check)
        self.CLK = Signal()
        self.SWT = Signal(16)
        
        # Ausgänge (Port-Namen wie in VHDL)
        self.SEG = Signal(7)
        self.AN = Signal(4)
    
    def elaborate(self, platform):
        module = Module()
        
        # Interne Signale
        a = Signal(4)
        b = Signal(4)
        control = Signal(4)
        result = Signal(8)
        
        # Mapping der Schalter
        module.d.comb += [
            a.eq(self.SWT[4:8]),      # A_IN von SWT 7:4
            b.eq(self.SWT[0:4]),      # B_IN von SWT 3:0
            control.eq(self.SWT[12:16])  # CTRL von SWT 15:12
        ]
        
        # ALU Instanz
        alu = ALU()
        module.submodules.alu = alu
        
        module.d.comb += [
            alu.a.eq(a),
            alu.b.eq(b),
            alu.control.eq(control),
            result.eq(alu.result)
        ]
        
        # Digits für 7-Segment Display
        digit_0 = Signal(4)  # B_IN
        digit_1 = Signal(4)  # A_IN
        digit_2 = Signal(4)  # Ergebnis unteres Nibble
        digit_3 = Signal(4)  # Ergebnis oberes Nibble
        
        module.d.comb += [
            digit_0.eq(b),
            digit_1.eq(a),
            digit_2.eq(result[0:4]),
            digit_3.eq(result[4:8])
        ]
        
        # Multiplexing Signale
        refresh_counter = Signal(range(self.REFRESH_COUNT))
        digit_select = Signal(2)
        current_digit = Signal(4)
        
        # Display Multiplexing
        with module.If(refresh_counter == self.REFRESH_COUNT - 1):
            module.d.sync += [
                refresh_counter.eq(0),
                digit_select.eq(digit_select + 1)
            ]
        with module.Else():
            module.d.sync += refresh_counter.eq(refresh_counter + 1)
        
        # Digit Selection
        with module.Switch(digit_select):
            with module.Case(0b00):
                module.d.comb += [
                    self.AN.eq(0b1110),  # Digit 0 (rechts, B_IN)
                    current_digit.eq(digit_0)
                ]
            with module.Case(0b01):
                module.d.comb += [
                    self.AN.eq(0b1101),  # Digit 1 (A_IN)
                    current_digit.eq(digit_1)
                ]
            with module.Case(0b10):
                module.d.comb += [
                    self.AN.eq(0b1011),  # Digit 2 (Ergebnis lower)
                    current_digit.eq(digit_2)
                ]
            with module.Case(0b11):
                module.d.comb += [
                    self.AN.eq(0b0111),  # Digit 3 (Ergebnis upper)
                    current_digit.eq(digit_3)
                ]
            with module.Default():
                module.d.comb += [
                    self.AN.eq(0b1111),
                    current_digit.eq(0)
                ]
        
        # 7-Segment Decoder
        decoder = SevenSegmentDecoder()
        module.submodules.decoder = decoder
        
        module.d.comb += [
            decoder.digit.eq(current_digit),
            self.SEG.eq(decoder.segments)
        ]
        
        return module


def generate_verilog():
    """Generiere Verilog-Code für Vivado"""
    
    top = ALU7Segment()
    
    ports = [
        top.CLK,
        top.SWT,
        top.SEG,
        top.AN
    ]
    
    output = verilog.convert(
        top,
        name="alu_7_segment",
        ports=ports
    )
    
    with open("alu_7_segment.v", "w") as file:
        file.write(output)
    
    print("Verilog-Datei 'alu_7_segment.v' wurde erfolgreich generiert!")
    print("\nPort-Mapping für Vivado (identisch mit VHDL):")
    print("  CLK     -> CLK")
    print("  SWT[15:0] -> SWT")
    print("  SEG[6:0]  -> SEG")
    print("  AN[3:0]   -> AN")


if __name__ == "__main__":
    generate_verilog()
