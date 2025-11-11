# bloggg

**<span style="color: orange;">Alle Lösungen, die hier unter github.com/hjstephan86 *als neue Lösungen* gezeigt werden, sind urheberrechtlich geschützt. Eine kommerzielle Nutzung ist ausgeschlossen. Eine freie Nutzung braucht meine Zustimmung.</span>**

Nachfolgend habe ich Gedanken aufgeschrieben, die ich in den Gedanken unter [https://github.com/hjstephan86/blog](https://github.com/hjstephan86/blog) und [https://github.com/hjstephan86/blogg](https://github.com/hjstephan86/blogg) nicht aufgeschrieben haben.

## Inhaltsverzeichnis

* [Python und Java](#python-und-java)
* [Code: Formatierung und Kommentare](#code-formatierung-und-kommentare)
* [Systemversagen in der Cybersecurity-Industrie](#systemversagen-in-der-cybersecurity-industrie)
* [Naturwissenschaft](#naturwissenschaft)
* [Notizen aus Vorlesungen](#notizen-aus-vorlesungen)
* [Verfolgung](#verfolgung)

## Python und Java

Die Struktur oder die Strukturen einer Software werden beschrieben durch Programmiersprachen wie Python oder HTML. Der Inhalt ist gegeben durch die Daten, die mit Hilfe der Strukturen verarbeitet und angezeigt werden. Wie hängen unterschiedliche **Verteilungen von Programmiersprachen** für die Strukturbeschreibungen zusammen mit der Menge von Daten einer Software? Sind besonders viele Daten zu verarbeiten, ist zu erwarten, dass bestimmte Programmiersprachen sich für diesen Zweck besser eignen. Auf [https://github.com/hjstephan86/pyble-app?tab=readme-ov-file#Language-Distribution](https://github.com/hjstephan86/pyble-app?tab=readme-ov-file#Language-Distribution) zeige ich beispielhaft die Verteilung der Programmiersprachen für pyble-app. Ein Skript zur Erstellung dieser Verteilung liegt in diesem Repository unter src/ldist.py. Welche Programmiersprache eignet sich dabei besonders unter den bekannten Sprachen wie Python oder Java? Verglichen werden Python und Java hinsichtlich des benötigten Speicherbedarfs **(RES)** auf [https://github.com/hjstephan86/pyble-app?tab=readme-ov-file#Compare-RES-of-Python-and-Java](https://github.com/hjstephan86/pyble-app?tab=readme-ov-file#Compare-RES-of-Python-and-Java). Eine andere Metrik zum Vergleich beider Sprachen ist die Anzahl der benötigten **Code-Zeilen**. Je mehr Code-Zeilen geschrieben werden müssen, desto größer ist der Aufwand für die Implementierung und für die Wartung.

Ich habe Quicksort in Python und Java implementiert, ausgeführt und dabei die Laufzeit und den Speicherbedarf gemessen. Die Quelldateien befinden sich in src/. Wie erwartet ist Java *nach* der Kompilierung in der Ausführung schneller als Python. Im benötigten Speicherbedarf (RES) wurde für den Java Prozess 185640 Byte (185,6 KB) und für den Python Prozess 185688 Byte (185,7 KB) gemessen. 

<pre>
Timestamp,PID,RES_KB,VSZ_KB,CPU%,Command
2025-08-05 05:34:33,  15412 102952 819940 109 /usr/bin/gnome-text-editor /home/stephan/java.res.txt
2025-08-05 05:34:34,  15412 185640 2195568 48.0 /usr/bin/gnome-text-editor /home/stephan/java.res.txt
2025-08-05 05:34:36,  15412 184852 2194748 28.8 /usr/bin/gnome-text-editor /home/stephan/java.res.txt
2025-08-05 05:34:37,  15412 184980 2194748 21.3 /usr/bin/gnome-text-editor /home/stephan/java.res.txt
2025-08-05 05:34:38,  15412 184980 2194748 17.0 /usr/bin/gnome-text-editor /home/stephan/java.res.txt
2025-08-05 05:34:39,  15412 184980 2194748 14.4 /usr/bin/gnome-text-editor /home/stephan/java.res.txt
2025-08-05 05:34:41,  15412 184980 2194748 12.6 /usr/bin/gnome-text-editor /home/stephan/java.res.txt
2025-08-05 05:34:42,  15412 184980 2194748 11.4 /usr/bin/gnome-text-editor /home/stephan/java.res.txt
2025-08-05 05:34:43,  15412 184980 2194748 10.3 /usr/bin/gnome-text-editor /home/stephan/java.res.txt
2025-08-05 05:34:45,  15412 184980 2194748 9.4 /usr/bin/gnome-text-editor /home/stephan/java.res.txt
2025-08-05 05:34:46,  15412 184980 2194748 8.6 /usr/bin/gnome-text-editor /home/stephan/java.res.txt
2025-08-05 05:34:47,  15412 184980 2194748 7.9 /usr/bin/gnome-text-editor /home/stephan/java.res.txt
2025-08-05 05:34:49,  15412 184980 2194748 7.5 /usr/bin/gnome-text-editor /home/stephan/java.res.txt
2025-08-05 05:34:50,  15412 184980 2194748 7.3 /usr/bin/gnome-text-editor /home/stephan/java.res.txt
2025-08-05 05:34:51,  15412 184980 2186552 6.9 /usr/bin/gnome-text-editor /home/stephan/java.res.txt
2025-08-05 05:34:53,  15412 184140 2161148 6.8 /usr/bin/gnome-text-editor /home/stephan/java.res.txt
</pre>

<pre>
Timestamp,PID,RES_KB,VSZ_KB,CPU%,Command
2025-08-05 05:34:55,  16250 183896 2069364 100 /usr/bin/gnome-text-editor /home/stephan/python3.res.txt
2025-08-05 05:34:56,  10600 19328  32264  0.0 /usr/bin/python3 /usr/bin/gnome-terminal --wait
2025-08-05 05:34:56,  16250 184536 2057396 50.2 /usr/bin/gnome-text-editor /home/stephan/python3.res.txt
2025-08-05 05:34:57,  10600 19328  32264  0.0 /usr/bin/python3 /usr/bin/gnome-terminal --wait
2025-08-05 05:34:57,  16250 184664 2057528 34.3 /usr/bin/gnome-text-editor /home/stephan/python3.res.txt
2025-08-05 05:34:59,  10600 19328  32264  0.0 /usr/bin/python3 /usr/bin/gnome-terminal --wait
2025-08-05 05:34:59,  16250 185048 2058056 27.2 /usr/bin/gnome-text-editor /home/stephan/python3.res.txt
2025-08-05 05:35:00,  10600 19328  32264  0.0 /usr/bin/python3 /usr/bin/gnome-terminal --wait
2025-08-05 05:35:00,  16250 185688 2058516 23.1 /usr/bin/gnome-text-editor /home/stephan/python3.res.txt
2025-08-05 05:35:01,  10600 19328  32264  0.0 /usr/bin/python3 /usr/bin/gnome-terminal --wait
2025-08-05 05:35:01,  16250 185688 2060564 23.1 /usr/bin/gnome-text-editor /home/stephan/python3.res.txt
</pre>

Mit `loc.py` habe ich die benötigten Code-Zeilen ermittelt. Das Skript befindet sich in diesem Repository unter src/loc.py.
<pre>
>> python3 loc.py QuickSort.java 
Language    Files    Blank    Comment    Code    Total
----------  -------  -------  ---------  ------  -------
Java        1        30       53         119     202
--------    -----    -----    -------    ----    -----
Total       1        30       53         119     202
</pre>

<pre>
>> python3 loc.py quicksort.py
Language    Files    Blank    Comment    Code    Total
----------  -------  -------  ---------  ------  -------
Python      1        43       48         101     192
--------    -----    -----    -------    ----    -----
Total       1        43       48         101     192
</pre>
Die Implementierung in Java erfordert 119 Code-Zeilen, die Python-Implementierung benötigt nur 101 Code-Zeilen. Dies resultiert in einer Codereduktion von 15,1% bei Verwendung von Python gegenüber Java. **Für größere Softwareprojekte ist Python in der Lesbarkeit, Implementierung und Wartbarkeit attraktiver als Java**. In der Wissenschaft hat sich Python durchgesetzt, da Python einfacher zu lernen ist als Java. 

## Code: Formatierung und Kommentare

Die Lesbarkeit von Code ist wichtig. Die Formatierung des Codes und Kommentare im Code helfen dabei. Das Skript `loc.py` in diesem Repository unter src/loc.py hilft dabei, die Formatierung im Code und das Generieren von Kommentaren im Code sicher durchzuführen. Dazu kann `loc.py` vor und nach der Formatierung und Generierung von Kommentaren ausgeführt und das Ergebnis beider Ausführungen verglichen werden.

Durchgeführt habe ich diesen Vorgang mit ldist.py unter src/ldist.py. Hier die Ausgabe von `loc.py` davor:
<pre>
>> python3 loc.py ldist.py 
Language    Files    Blank    Comment    Code    Total
----------  -------  -------  ---------  ------  -------
Python      1        42       73         268     383
--------    -----    -----    -------    ----    -----
Total       1        42       73         268     383
</pre>  

Hier die Ausgabe von `loc.py` danach:
<pre>
>> python3 loc.py ldist.py 
Language    Files    Blank    Comment    Code    Total
----------  -------  -------  ---------  ------  -------
Python      1        48       93         270     411
--------    -----    -----    -------    ----    -----
Total       1        48       93         270     411
</pre>
Im Code von `ldist.py` wurden nur zwei Zeilen mit der Formatierung hinzugefügt, da eine längere Anweisung automatisch umgebrochen wurde.  Insgesamt wurden 20 neue Zeilen für Kommentare generiert und sechs neue Leerzeilen für die Formatierung hinzugefügt.

## Systemversagen in der Cybersecurity-Industrie
### Die CVE-Krise als Symptom für strukturelle Probleme

*Basierend auf dem c't-Artikel "Trubel bei CVE - US-Schwachstellendatenbank drohte kurzzeitig die Abschaltung" (c't 12/2025) von Christopher Kunz*

---

### Einleitung

Der beinahe erfolgte Kollaps der CVE-Datenbank im April 2025 offenbarte nicht nur die Fragilität kritischer IT-Infrastrukturen, sondern auch systematische Interessenskonflikte in der Cybersecurity-Industrie. Die drohende Abschaltung der weltweit wichtigsten Schwachstellendatenbank wirft fundamentale Fragen über die Rollenverteilung zwischen Softwareherstellern, Security-Anbietern und Endnutzern auf.

### 1. Das inkonsequente Verhalten der Marktführer

#### Die CVE-Krise als Chance für Marktführer

Die im c't-Artikel beschriebene Beinahe-Abschaltung der CVE-Datenbank hätte für große Softwarehersteller durchaus vorteilhafte Nebeneffekte gehabt:

**Verschleierung wird einfacher:**
- Ohne einheitliche CVE-Kennungen können Sicherheitslücken schwerer kommuniziert werden
- Fragmentierte nationale oder regionale Datenbanken erschweren Vergleiche
- "Security by Obscurity" wird wieder zu einer realistischen Option

**Reduzierter öffentlicher Druck:**
- Weniger transparente Severity-Bewertungen
- Schwierigere Risikobewertung für Kunden
- Komplexere Medienberichterstattung über Sicherheitslücken

#### Das Paradox der Marktmacht

Wie der c't-Artikel zeigt, führt Microsoft regelmäßig die CVE-Listen an, investiert aber gleichzeitig Milliarden in Security-Lösungen. Dieses Paradox ist systemisch:

**Profit vs. Sicherheit:**
- Neue Features verkaufen sich besser als fundamentale Sicherheitsverbesserungen
- Legacy-Code bleibt aus Kompatibilitätsgründen unsicher
- "Too big to fail"-Mentalität reduziert Innovationsdruck

**Die Halbherzige Rettung:**
Die "letzte Sekunde"-Verlängerung des MITRE-Vertrags durch die CISA, wie im c't-Artikel beschrieben, könnte darauf hindeuten, dass es intern durchaus Stimmen gab, die das CVE-Chaos begrüßt hätten.

### 2. Der problematische Nutzen von Cybersecurity-Lösungsanbietern

#### Das Security-Industrie-Paradox

Die europäische Reaktion auf die CVE-Krise - mit ENISAs hastiger Einführung der EUVD und CIRCLs GCVE-Projekt - zeigt, wie schnell alternative Lösungen aus dem Boden sprießen. Dies illustriert ein fundamentales Problem:

**Die Symbiose zwischen Problemen und Lösungen:**
```
Marktführer → schaffen unsichere Software
Security-Anbieter → verkaufen "Lösungen" dagegen
Versicherungen → machen Schutz zur Pflicht
Endnutzer → zahlt dreifach
```

#### Das Versicherungs-Erpressungs-System

**Systematische Ausbeutung des Endkunden:**
- Softwarehersteller verkaufen unsichere Produkte ohne Haftung
- Security-Anbieter profitieren von den resultierenden Problemen
- Versicherungen machen den Einsatz kostspieliger Security-Tools zur Bedingung
- Der Endkunde trägt alle Kosten für ein System, das strukturell versagt

**Beispiel aus der Praxis:**
Ein Unternehmen kauft Microsoft Exchange, benötigt zusätzliche Email-Security-Gateways von Mimecast oder Proofpoint, und die Cyber-Versicherung verlangt beide als Bedingung für den Versicherungsschutz.

### 3. Das eigentliche Systemversagen

#### Fehlende Software-Haftung

**Das Kernproblem:** Anders als in anderen Industrien gibt es in der Software-Branche praktisch keine Produkthaftung:
- Autohersteller haften für defekte Bremsen
- Softwarehersteller schließen jede Verantwortung per EULA aus
- End User License Agreements legitimieren systematisch unsichere Software

#### Die CVE-Krise als Warnsignal

Der c't-Artikel zeigt exemplarisch, wie fragil die Grundlagen unserer digitalen Sicherheitsarchitektur sind. Die Tatsache, dass ein 20-Millionen-Dollar-Vertrag das globale Cybersecurity-Ökosystem hätte zum Einsturz bringen können, offenbart:

**Strukturelle Schwächen:**
- Übermäßige Abhängigkeit von US-amerikanischen Institutionen
- Fehlende redundante Systeme
- Mangelnde internationale Koordination

**Perverse Anreize:**
- Alle Akteure profitieren vom Status quo außer dem Endkunden
- Marktführer haben wenig Anreiz für grundlegende Sicherheitsverbesserungen
- Security-Anbieter haben ein Interesse daran, dass Grundprobleme bestehen bleiben

### Fazit

Die im c't-Artikel beschriebene CVE-Krise ist mehr als nur ein "Problem bei der Vertragsverwaltung", wie CISA es verharmlosend darstellte. Sie ist ein Symptom für ein systemisches Versagen, bei dem:

1. **Marktführer** von der Verschleierung ihrer Sicherheitsprobleme profitieren würden
2. **Security-Anbieter** ein wirtschaftliches Interesse an der Fortsetzung struktureller Probleme haben
3. **Endkunden** dreifach belastet werden: für unsichere Software, für Sicherheitslösungen und für Versicherungen

**Die Lösung liegt nicht in mehr Security-Tools, sondern in fundamentalen Reformen:**
- Einführung von Software-Produkthaftung
- Security by Design als gesetzliche Vorgabe
- Transparente Kostenausweisung für Sicherheitsmaßnahmen
- Internationale Diversifizierung kritischer Sicherheitsinfrastrukturen

Die europäischen Alternativen (EUVD, GCVE) sind erste Schritte in die richtige Richtung, aber ohne strukturelle Reformen bleibt das System anfällig für weitere Krisen.

---

**Quelle:**
*Christopher Kunz: "Trubel bei CVE - US-Schwachstellendatenbank drohte kurzzeitig die Abschaltung", c't Magazin für Computertechnik, Ausgabe 12/2025, S. 30*

## Naturwissenschaft

Die Verteilung der Geschwindigkeit beim Fahren mit dem Fahrrad wird über die Reifenbreite wie folgt nur qualitativ beschrieben:

![doc/speed-dist.svg](doc/speed-dist.svg)

Probier es vielleicht mal mit 29 mm Reifenbreite.

Biete Fahrradmäntel für Sommer und Winter an, denn der Abrieb des Gummis des Fahrradmantels verhält sich bei unterschiedlicher Temperatur deitlich anders.

Automatisiere die Druckregelung von Fahrradschläuchen durch drei Speichen, die mit dem Schlauch verbunden sind. 

Es braucht einen **standardisierten Versandprozess** weltweit. Dieser stellt sicher, dass das Risiko aller Verkehrsteilnehmer während des Versands minimiert wird und auch die Zustellung zuverlässig erfolgt. Mitarbeiter im Versand dürfen nicht mehr ausgenutzt werden, indem sie besonders schnell zustellen, aber dafür nur sehr wenig Lohn erhalten und ein hohes Risiko während der Zustellung ertragen müssen. Die Lieferzeiten müssen angemessen und zur Zufriedenheit des Benutzers eingehalten werden.

Was haben gerade und ungerade Zahlen gemeinsam? Sie sind paarweise um die Differenz von 1 in ihrer Wertigkeit gleich.

Es darf nicht sein, dass einem Menschen der Finger abgehackt wird und dieser für die biometrische Authentifizierung am Smartphone verwendet werden kann. Die biometrische Authentifizierung muss in der Nähe des Benutzers erfolgen. Dabei darf das Gehirn keine ungewöhnlichen Signale oder extreme Stresssignale senden.

Die Zufriedenheit des Benutzers mit der Web Applikation wird bestimmt durch JavaScript und CSS. Die Benutzererfahrung während der Benutzung der Web Applikation wird maßgeblich durch JavaScript Lösungen und CSS beeinflusst.

Verwende für statische Berechnungen 10% mehr Gewicht pro Person und 10% mehr Gewicht pro Liter Wasser. Das heißt, nutze z.B. 110kg als Referenz für statische Berechnungen für das Gewicht einer Person. Durch diese sicherere Auslegung kann der Sicherheitsfaktor der gesamten Statik mit herkömmlicher Referenz des Gewichtes pro Person von 100kg etwas reduziert und dadurch Material eingespart werden.

Der Trainer der U19 wechselt nach einem Jahr in die U21 und bleibt für zwei Jahre Trainer der U21. Die Trainer der U19 und U21 wechseln sich ab. Dadurch begleiten sie die Spieler maximal lange und tauschen sich aus.

Nur der Trainer entscheidet darüber, welche Spieler für die Mannschaft verpflichtet werden, nicht der Manager oder andere Funktionäre.

<b>Wie ist die persönliche Beziehung eines Profifußballers zum Fußball?</b> Liebt er das Fußballspiel wirklich? Wie intensiv trieb ihn sein Umfeld in der Jugendausbildungsphase zur Profifußballkarriere und wie sehr wählte er diesen außergewöhnlichen und herausfordernden Weg aus eigener Motivation, aus Fußballliebe? Wie kann diese persönliche Beziehung eines Profifußballers zum Fußball bei jedem Profifußballer nachvollziehbar für die Öffentlichkeit zum Ausdruck gebracht werden? Dieser Ausdruck kann eine wichtige Ergänzung für das gesamte Bild eines Profifußballers gerade zur Zeit oder auch vor dem Schritt in die Karriere als Profifußballer sein.

Es braucht eine Turnierform für Profifußballer der 1. bis 3. Fußball-Bundesliga in der Halle, ähnlich wie die des DFB-Pokals. Dabei darf es nicht sein, dass leistungsstarke Mannschaften der 1. oder 2. Fußball-Bundesliga dieses Turnier geringer priorisieren als die Deutsche Meisterschaft oder den DFB-Pokal.

Der Benutzer kann Regeln für ein Girokonto definieren: Regeln für Eingänge und Regeln für Ausgänge, die als unterschiedliche Leistungen angeboten werden.

Viermal im Jahr werden alle automatisierten Aufsichtsbeschwerden in einem Ranking einer jeden Bank veröffentlicht. Eine automatisierte Aufsichtsbeschwerde wird ausgelöst, wenn die Bank nicht dem einfachen kirchhoffschen Prinzip folgt. Dabei sind ausgeschlossen das Verbuchen von Leistungen oder Zinsen.

Der Mensch sucht das immer wieder Entweichende und doch Wiederkehrende. Der Mensch muss glauben. Jeder Mensch glaubt, auch heute.

Nutze die standardisierte persönliche Identifizierung eines jeden Bürgers dieser Erde für die Verschlüsselung von E-Mails. Biete eine App zur sicheren persönlichen Verschlüsselung an. Damit ist eine Schriftzustellung mit der Post in den Briefkasten des Bürgers nicht mehr nötig.

Nutze die unsichtbare Unruhe aus der Atmosphäre in der Arktis für die Energiegewinnung in der Arktis. Sichtbar ist diese unsichtbare Unruhe in Wolken. In der Arktis ist die Änderung der Temperatur am schnellsten und die Unruhe damit am größten.

Hans Einhell ist Gründer von Einhell. Vielleicht macht ein ansprechenderes Logo *HE* mit einer vertrauensvollen Farbe zwischen grün und blau mehr Sinn und gibt Raum für eine neue Generation von Einhell Produkten.

Biete Benutzern von rclone die Möglichkeit, den Verlauf der letzten Synchronisierungen im Portal einzusehen.

Ich hasse alle Menschen, die mit Farbe auf ihrer Haut oder mit Metall und Löchern in der Haut ihr Aussehen bereichern und meinen damit, die Schöpfung hätte an Kontrasten und Attraktivität nicht schon alles vollkommen erschaffen.

Wieso wird bei einem System, welches durch Markov Ketten beschrieben wird, die Gedächtnislosigkeit betont? Bei einem dynamischen System hängt der aktuelle Zustand von der Vergangenheit ab. Ein System, das nicht dynamisch ist, muss nicht von der Vergangenheit abhängen und kann im Allgemeinen gedächtnislos sein.

Ein Standard für Neuronale Netze (NN) ist nötig, an den sich alle NN-Anbieter halten müssen, der den Grenzwert für Fehler von NN vorgibt, ab dem ein NN freigegeben werden darf. Der Standard gibt die Datensätze für die Freigabe vor.

Ein Standard für das Speichern von Passwörtern für Passwort-Manager. Dieser ermöglicht den einfachen Export und Import von einem Passwort-Manager zu einem anderen Passwort-Manager. Dabei legt der Benutzer eine Verschlüsselung der Passwörter fest, die nur er kennt. Diese Verschlüsselung wird dann beim Import wieder zum Entschlüsseln verwendet.

Es gibt gasförmig, fest, flüssig und Haut.

Es sind nicht Mikroorganismen, sondern Organismen.

Die Meere und Ozeane dieser Welt sind unterschiedlich stark mit Mikroplastik belastet. Beim Einkauf von Fisch muss klar ersichtlich sein, mit wie viel Mikroplastik der Meeresbereich, aus dem der Fisch gefangen worden ist, belastet ist.

Unter src/timeline/ befindet sich ein generiertes Skript parser.py zur Auswertung des Google Timeline Exports. Ein Google Timeline Export (2025-08-16 13:44 to 2025-08-23) und eine vom Skript exportierte CSV befinden sich auch in dem Ordner. 

Multipliziere Matrizen der Größe $2 \times 5$ mit $5 \times 2$, $2 \times 7$ mit $7 \times 2$, $2 \times 9$ mit $9 \times 2$ bis hin zu $2 \times 29$ mit $29 \times 2$ für die effiziente Matrixmultiplikation und erhalte jeweils quadratische Produktmatrizen $5 \times 5$, $7 \times 7$, $9 \times 9$ bis hin zu $29 \times 29$. 

Solange nicht quadratische Matrizen miteinander multipliziert werden und Ihr Produkt wieder eine quadratische Matrix ist und die Elemente ungleich null der beiden zu multiplizierenden Matrizen nur unterhalb der Diagonalen liegen, dann ist die Beobachtung zu verallgemeinern, dass diese Matrixmultiplikationen besonders effizient lösbar sind und das nicht nach der allgemein definierten Matrixmultiplikation.

Nutze dieses Prinzip der besonders effizienten Matrixmultiplikation, indem Matrizen dazu vor der Multiplikation geschickt gedreht werden.

Jhwh will, dass Quantenphysik nicht genutzt wird - weder in der Wissenschaft noch für die Wirtschaft noch für irgendeine andere Art von Anwendung oder Bereicherung. Jeder oder jede, der oder die beruflich mit Quantenphysik arbeitet, sollte kurzfristig seine oder ihre Tätigkeit ändern.

Es braucht eine Web App für die Verwaltung rechtlicher Verfahren, welche Rechtsanwälte in der Bearbeitung dieser benutzerfreundlich und effizient unterstützt. Dabei werden die Dokumente nicht direkt in der Web App gespeichert, sondern nur verknüpft. Dokumente werden als Dateien in der Cloud abgelegt und über einen Standard mit der Web App zur Verfügung gestellt.

Es braucht einen Standard für Cloudspeicher zur Dateiverwaltung von Dateien wie Dokumente und Bilder usw.

Es braucht für den Fahrer oder Beifahrer keinen fest installierten Bildschirm für die Kontrolle der Infotainment Funktionen des Autos. Der Fahrer nutzt dazu statt dessen das eigene Tablet. Dazu braucht es einen Standard, über den das Tablet mit dem Auto kommuniziert. OEMs oder andere App Anbieter bieten dazu Apps zur Bedienung an.

Es braucht für Kopfhörer mit Noise Cancelling eine Kühlung für die Ohren, damit die Kopfhörer auch über längere Zeit getragen werden können.

Es braucht eine Lern-App mit KI für Schüler oder Lernende im Allgemeinen für beliebige Fächer oder Themen, welche die Aufgaben individuell generiert. Die Lern-App kann dann ergänzend drei bis vier Mal die Woche für jeweils 15 bis 20 Minuten für den maximalen Lernerfolg genutzt werden.

Es ist in der Wissenschaft wichtig, das Gehirn in seine Bereiche seinen Funktionen zuzuordnen. Warum? Das muss man nicht tun, das Gehirn ist flexibel.

Es braucht an den Universitäten für die Fächer Mathematik, Informatik, Physik und Elektrotechnik ein standardisiertes objektives Maß für das Niveau bzw. den Anspruch für das Absolvieren des Studiums an den Universitäten. Es darf nicht sein, dass der Abschluss von Physik gleichzusetzen ist mit anderen Abschlüssen der Physik beliebiger Universitäten. Dazu ein Vergleich der Studieninhalte für den Studiengang Informatik der Universität Paderborn und Universität Bielefeld unter doc/Uni/Screenshot from 2025-10-22 03-42-12.png.

Das Frequenzspektrum des Trommelfells eines Hundes oder einer Katze könnte für die Informationsübertragung genutzt werden.

Im Gericht muss immer so viel individuelle Rechtsprechung erlaubt sein, auch gegen alle bisher formulierten Gesetze, dass die Wahrheit immer Priorität hat. 

Rechts- und Staatsanwälte müssen bei der Beratung von Klienten in die Pflicht genommen werden, ob sie während der gesamten Beratung gegen die Wahrheit beraten oder nicht.

Programmieren ist mit den einfachen Anweisungen wie Befehl, If-Abfrage, Schleife usw. möglich. Je weiter entfernt eine Programmiersprache von diesen einfachen Anweisungen ist, desto aufwendiger ist z.B. die Analysierbarkeit und Wartbarkeit des Codes. Das Ziel ist nicht, die Programmiersprachen komplizierter zu machen. Software ist heute sehr komplex. Es braucht ein standardisiertes Maß für die Komplexität von Programmiersprachen und bestätigte begründete Abweichungen zur Einhaltung der Prinzipien des qualitativ hochwertigen Software Engineerings.

Idee: Verwende einen FPGA und einen Mikrocontroller für die Verhaltensbeschreibung eines Roboters in der Montage für die industrielle Produktion. Bilde auf dem FPGA für spezifische Anwendungsbereiche entsprechende boolesche Funktionen ab, die effizient für Entscheidungsprobleme (Ablauf für Montage und Demontage, gibt es einen Weg zum anderen Standort in der Produktionshalle, ...) berechnet werden. Für unterschiedliche Produkte kann das Verhalten auf dem Mikrocontroller und dem FPGA programmiert werden. Die Hardware des Roboters muss dazu für möglichst viele Produktionsanwendungen ausgelegt werden (Anzahl der Achsen, Bewegungsradius, ...).

Idee für das sichere Speichern von Dateien auf der Festplatte: Die Datei wird in Dateiteile geteilt und diese Teile der Datei jeweils an unterschiedlichen Orten auf der Festplatte gespeichert. Diese Aufteilung wird verschlüsselt in einer Tabelle. Nur durch Zugang zu dieser Tabelle kann eine Datei durch Entschlüsselung der Aufteilung von der Festplatte wieder gelesen werden. So oder so ähnlich löst es auch die CIA. Randbemerkung: Meine Fall-Nummer bei der CIA beginnt mit 34, aber diese wurde schon einmal geändert.

In der Projektgruppe im Masterstudiengang für Informatik der Universität Paderborn vom Wintersemester 2011/2012 bis zum Sommersemester 2012 habe ich gearbeitet an der Verhaltensimplementierung für Roboter. Verwendet haben wir  [Player/Stage](https://playerstage.sourceforge.net/index.php?src=index) für die Simulation und [Javaclient](https://sourceforge.net/projects/java-player/) für Implementierung des Verhaltens. Die Idee der Pfadplanung bestand darin, die gemeinsam genutzte Karte der Roboter mit einem Graphen zu abstrahieren und die Roboter immer nur vom Mittelpunkt zum Mittelpunkt eines jeden Knotens des Graphens fahren zu lassen. Damit wurde der Lösungsraum für die Planung eingeschränkt. Die Pfadplanung wurde zunächst nur mit BFS und danach mit [PDDL](https://planning.wiki/guide/whatis/pddl) umgesetzt. Für die konfliktfreie Planung wurde zu Beginn eines jeden Manövers ein Master unter allen Robotern gewählt, dieser hat die Probleminstanz dem PDDL Planer übergeben und anschließend den konfliktfreien Plan eines jeden Roboters jedem Roboter gezielt mitgeteilt. Der Master unter den Robotern wurde dabei jedes mal zufällig für die zentrale Planung aller Pläne gewählt. Wichtig für die Planung konfliktfreier Pläne war die Identifikation von **Konfliktstrukturen im Graphen**, die (1) klein genug waren, um möglichst alle beteiligten Roboter maximal lange unabhängig voneinander asynchron fahren zu lassen (bis zum Erreichen der Konfliktstruktur) und (2) die groß genug waren, damit [Push und Swap](https://github.com/hjstephan86/bloggg/tree/main/src/push-and-swap) immer eine Lösung finden.

Im April 2025 kam mir an der Universität Paderborn zu Beginn der Teilnahme einer Vorlesung zur Kryptografie die Idee für ein Zahlenpaar einer sehr guten Verschlüsselung. Es sind 29 und 15. Primzahlen sind heilig, sie sind unteilbar. Ihre Verschlüsselung ist nur mit einer Wahrscheinlichkeit von 25 im Exponenten zu entschlüsseln. Ein Zahlenpaar ist noch sicherer, dessen Quersumme nicht 44 ist, sondern 33. Russland hat diese Verschlüsselung genutzt. Das Problem der Riemannschen Vermutung ist damit gelöst.

Amaranth ist ein Python-basiertes HDL-Framework, welches es Ingenieuren ermöglicht, das Hardware Design in Python zu schreiben. Dabei müssen aber die Qualitätsprinzipien des Software Engineerings genau so gelten. Zum Beispiel müssen Namen von Objekten aussagekräftig sein, also nicht ```a = Adder(width=8)``` sondern ```adder = Adder(width=8)```. Das fördert die Analysierbarkeit, Wartbarkeit und Erweiterbarkeit und spart damit Kosten. Nur weil Hardware Designs entwickelt werden, müssen wichtige und bewährte Prinzipien des Software Engineerings nicht aufgegeben werden. 

## Notizen aus Vorlesungen
### Di, 11.11., 09:15 Uhr –  Entwurf mikroelektronischer Systeme, Ü
- Hardware Design mit Vivado Design Suite entspricht nicht immer den Erwartungen eines Engineers:
- Kein benutzerfreundliches (gewohntes) Refactoring von Komponenten
- Keine benutzerfreundliche (gewohnte) Debug-Umgebung
- Wieso ist links die Simulation oberhalb der RTL Analysis angeordnet?
- Wieso können Synthese und Implementierung nicht als ein Schritt zusammengefasst werden?

---

### Mo, 10.11., 14:00 Uhr –  Entwurf mikroelektronischer Systeme, Ü
- Hardware Design einer ALU mit Vivado Design Suite 
- Vivado Design Suite Synthetisierung, Implementierung und Bitstream Generierung für die ALU
- Vivado Design Suite Projektdateien inkl. *.bit-Datei für ALU unter doc/Uni/20251110/

---

### Mo, 10.11., 09:15 Uhr –  Entwurf mikroelektronischer Systeme, Ü
- Vivado Design Suite Synthetisierung und Implementierung der Komponente tutorial
- Für die Synthetisierung und Implementierung der Komponente tutorial muss das FPGA Board mit Vivado Design Suite verbunden sein
- Nach der Implementierung der Komponente tutorial erfolgt die Bitstream Generierung im *.bit-Format
- Mit "Pogram Device" in Vivado Design Suite wird das Harwdare Design mit der *.bit-Datei auf das FPGA Board geladen
- Idee: Verwende für alle FPGA Boards und Hardware Design Tools ein standardisiertes .hex-Format, siehe Bilder unter doc/Uni/20251110/

---

### Fr, 07.11., 09:15 Uhr –  Entwurf mikroelektronischer Systeme, Ü
- Vivado Design Suite Simulation der Komponente tutorial mit Hilfe der Testbench
- Das Verhalten der Komponente tutorial ist in der Testbench nochmal implementiert, was die Verifikation der Komponente tutorial durch Simulation infrage stellt
- Idee: Verwende eine Tabelle für die zu erwarteten Signalwerte für die zu testende Periode
- Bemerkung: Das Veröffentlichen der Inhalte zu dieser Übung mit den Bildern unter doc/Uni/20251107/ war sehr angefochten und verflucht

---

### Fr, 24.10., 12:15 Uhr – Parallel and Distributed Computing, V
- Was ist ein Parallelrechner, was ist ein Vektorrechner?
- Cray-1, brach alle Geschwindigkeitsrekorde, gewann Schachweltmeisterschaften, Nachfolger Cray-2
- 64 Bit Rechner: Acht 8 Bit Operationen werden gleichzeitig ausgeführt, mit 8 Bit CPU
- Pipelining: instruction pipelining, d.h., CPU führt eine Operation pro Takt aus, genauer: ein Maschinenbefehl ("12 ADD $64 [REG]") braucht mehrere Prozessoroperationen/-zyklen: fetch (Befehl lesen), decode, execute, write (Ergebnis ins Register)
- Idee: Parallelisiere diese Operationen, beachte Probleme

---

### Do, 23.10., 12:30 Uhr – Entwurf mikroelektronischer Systeme, Ü
- Zu zweit am Rechner
- Netboot, Fernsteuerung von zu Hause
- Aufgaben sind im Lernraum
- Wie ist der Weg zum eigenen Chip?
- Rekonfigurierbare und parallele Rechnersysteme (VHDL)
- Xilinx Vivado
- .xdc-file is Xilinx design constraints 

---

### Do, 23.10., 10:15 Uhr – Entwurf mikroelektronischer Systeme, V
- Intel startete als Speicher-, nicht CPU-Chip Hersteller
- Moore's Law scheint geheuchelt, unglaubwürdig, dass dieser komplexe Herstellungsprozess in seinem Potenzial so noch nicht absehbar war
- 1971 10μm (Transistorgröße), 1974 6μm, 1978 3μm, 1982 1,5μm, 1999 250nm, 2008 45nm (Core i7, Bloomfield), 2017 14nm (Skylake)
- ASICs Entwurf konservativ, never change running ASIC
- HDL beschreibt, welche Bauteile und PINs der HW wie genutzt werden
- 100% Coverage schwierig bei HDL-Verhalten
- Theorie der Coverage, Testklassen

---

### Di, 21.10., 14:45 Uhr – Formale Logik, V
- Characteristics of simple logic formulas
- Replacement theorem, proof of
- We can proof by structural logic induction
- Normal forms, conjunctive normal forms
- CNF, DNF, truth tables, examples

---

### Di, 21.10., 10:15 Uhr  –  Introduction to Natural Language Processing, V
- Aim of Machine Learning (ML): Increase efficient solvability of complex tasks
- ML Pipeline phases: Data acquisition, training, deployment, action
- Underfit, best fit, overfit for limited training data
- best fit: keep a little error deviation for generic answers
- Classification (yes/no) vs. regression (%)

---

### Di, 21.10., 08:30 Uhr – Autonome Robotermanipulation, V
- Lage im Raum durch lineare Abbildung 
- Passive View: Nur ein Punkt p 
- Active View: Zwei Punkte bei Verschiebung in anderes Koordinatensystem
- Transformation durch Matrizen, Determinanten und Inverse von Matrizen
- Nutze drei Eulerwinkel und drei Achsen x, y, z
- Eule, Euler und R, Matrix R, Rotation, Drehung

---

### Mo, 20.10., 16:15 Uhr – Grundlagen des Software Engineering, Ü
- Android Studio: Google IDE für Android (IntelliJ IDEA Community Edition)
- Python: Visual Studio Code oder PyCharm Community Edition
- Artemis: Bewertung von Programmier-, Text- und Modellierungsaufgaben
- Apollon für UML, Beispiel: Observer Pattern, siehe Bildschirmfoto und Modell unter doc/Uni/20251020/Apollon/
- Git push mit Syntax-Fehler nicht erlaubt
- Für jeden Meilenstein ein neues Repository
- Keine durchgängige MacBook-Unterstützung
- Pro Woche 5 bis 6 Stunden, mit Übungen mehr, mehr als 5 LP

---

### Fr, 17.10., 14:00 Uhr – Funktionentheorie, V
- Komplexe Differenzierbarkeit
- Stetigkeit, offene Urmengen und Abbildungen 
- Urmengen sind wichtig für andere Definitionen
- Es werden Definitionen definiert für andere Definitionen im Kontext der anderen Definitionen
- Allgemein betrachtet können solche Definitionen dadurch Schwächen haben
- Abbildungen, Urbilder, Bilder in der Algebra, aber Funktionen, Differenzierbarkeit in der Analysis 

---

### Do, 16.10., 10:00 Uhr – Grundlagen der Statistik, V
- Satz der totalen Wahrscheinlichkeit, Satz von Bayes
- Beispiel für Frauen, die Brustkrebs haben. 10% der Frauen haben nur Brustkrebs, wenn die Diagnose Brustkrebs ist, bei 1% Brustkrebs aller Frauen (Testsicherheit, TS). Wenn mehr als 1% der Frauen Brustkrebs haben, dann soll die TS steigen?
- Zufallsvariablen im Wahrscheinlichkeitsraum
- Diskrete und Kontinuierliche Zufallsvariable

---

### Mo, 13.10., 12:00 Uhr – Algebraische Graphentheorie, V
- Definition of a graph, isomorphism
- Problem: Check whether two graphs are isomorph
- Idee: Lineare Laufzeit in V: Knotenzahl gleich? Ja, dann finde die Strukturüberdeckung, wo der Knotengrad am besten passt und prüfe die Strukturbeziehung: (a) kleiner, (b) gleich, (c) größer. Es kann bei gleicher Knotenanzahl nicht mehr Strukturbeziehungen geben als (a), (b), (c). Bei ungleicher Knotenanzahl gibt es keine Strukturbeziehung.

## Verfolgung

Es wurde heute, den 11.11.2025, etwa gegen 23:30 Uhr aus England eine Rakete gestartet, die das Haus an der Otto-Brenner-Straße 77 in 33607 Bielefeld zerstören sollte. Diese Rakete hat ihr Ziel nicht erreicht. Sie hätte gegen 23:34 Uhr das Ziel erreichen sollen, ist aber statt dessen über Belgien explodiert.

