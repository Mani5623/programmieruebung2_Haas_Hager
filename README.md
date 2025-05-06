# programmieruebung2_Haas_Hager

#Manuel Hager und Jakob Haas

PDM ist ein Paketverwaltungstool. Es managed die Pakete die man für ein Projekt braucht. Wenn man an verschiedenen Projekten arbeitet, kann es sein, dass verschiedene Versionen von z.B. Numpy oder Python benötigt werden. PDM hilft einem dabei, immer die Richtige Version für sein aktuelles Projekt zu benutzen. PDM erstellt und verwaltet projektbezogene virtuelle Umgebungen, ohne dass man sie manuell aktivieren musst.

Projekt initialisieren:
pdm init

Abhängigkeiten installieren:
pdm add numpy pandas

In dieser Virtuellen Umgebung haben wir dann 3 Python files.
1. load_data.py: Hier werden die gegeben Datensätze eingelesen.
2. sort.py: Hier werden die Daten, in unserem Fall, die Leistungszahlen mit Hilfe eines Bubble Sorts, geordnet.
3. powercurve.py: Hier werden die davor sortierten Daten in unserem Fall, Leistungszahlen geplottet.

<img src="\figures\powercurve.png">
