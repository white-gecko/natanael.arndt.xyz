---
layout: page
parent: notes
title: Biometrische Passbilder Herstellen
abstract: "Eine kleine Anleitung, wie man selbst mit einfachen Mitteln biometrische Passbilder herstellen kann"
---

Das folgend Vorgehen nutze ich, um biometrische Fotos anzufertigen.
Ich kann aber nicht garantieren, dass die resultierenden Bilder tatsächlcih biometrisch korrekt sind und von den entsprechenden Behörden akzeptiert werden.
Die Quelle für die zugrundeliegenden Maße ist in diesem Fall die [„Passbild-Schablone für Personen ab einem Alter von 10 Jahren“](https://www.bundesdruckerei.de/sites/default/files/passbildschablone_erwachsene.pdf) der Bundesdruckerei.
Es ist also ratsam, sich ebenfalls die Hinweise der Bundesdruckerei und der übrigen Behörden anzusehen.

| **Bildgröße:**              | 35mm×45mm            |
| **Kinnhöhe/Gesichtshöhe:**  | 32mm–36mm -> 34mm    |
| **Augenbereich:**           | 22mm–32mm (~0,5–0,7) |

## Bild Vorbereiten

1. Bild drehen, so dass Augen auf einer Linie sind und Mund-Mitte, Nasen-Mitte und Stirn-Mitte

2. Ausschnitthöhe durch Skallierungsverhältniss Berechnen
    1. Kinnhöhe auf dem Bild ausmessen (Gimp Werkzeug: Maßband), die Höhe -> X (X ist die Kinnhöhe)
    2. (X/34mm)×45mm = Y (Y ist die Ausschnitthöhe auf der Arbeitsfläche, es ist auch wichtig die Einheit von X zu notieren z.B. „mm“)

## Bild Zuschneiden

3. Bild zuschneiden (Gimp Werkzeug: Zuschneiden)

    1. Festes Seitenverhältnis einstellen: Hacken vor „Fest:“ setzen, in das Feld darunter „35:45“ eintragen (Bildbreite zu Bildhöhe).
    2. Den Zuschnitt-Bereich mit der Maus aufziehen (In das Bild klicken und die Maus bewegen)
    3. Größe setzen: das zweite Eingabe-Feld bei „Größe“ auf Y setzen, dabei darauf achten, dass die Einheit darüber gleich zu der Einheit von X bzw. Y aus 2.b. gewählt ist (z.B. auch „mm“)
    Tip: Falls der Wert so nicht angenommen wird, sollte man den Zuschnitt-Bereich in der Mitte Anfassen und in die Mitte des oberen Bildrandes schieben und den Wert neu eingeben
    4. In dem Auswahlmenü Gestaltungsregeln („Keine Hilfslinien“) die „Drittelregel auswählen“
    5. Den Bereich so positionieren, dass die obere Hilfslinie oberhalb der Augen sind bzw. die Augen sich zwischen der Mitte des Zuschnitt-Bereichs und der oberen Hilfslinie befinden
    6. Die [Enter]/[Eingabe]-Taste drücken oder in die Mitte des Zuschnittbereichs klicken

## Bild für den Druck skallieren

4. Bild für den Druck skallieren
    1. Im Menü „Bild“ > „Bild skalieren“ auswählen
    2. X- aund Y-Auflösung auf einen guten Wert setzen, z.B. 300 Pixel/in
    3. Höhe auf „45 mm“ setzen, wenn alles beim Zuschneiden geklappt hat sollte für die Breite automatisch ein Wert in der Nähe von „35 mm“ gesetzt werden
    Tip: Evtl. muss die Kette rechts von den zwei Eingeabefeldern noch angeklickt werden
    4. „Skalieren“ drücken

5. Datei Exportieren
