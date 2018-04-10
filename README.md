# Picamera Zeitraffer-Aufnahmen :water_buffalo:  :squirrel:
 [TOC]
## Was macht dieses Programm ?
 Mit dem Programm lassen sich mit dem Raspberry Pi und dem dazugehörigen Kamera-Modul einfach Zeitrafferaufnamen erstellen. Der Code basiert weitesgehend auf der offiziellen Dokumentation des Kamera-Moduls [Picamera Docs](https://picamera.readthedocs.io/)

 Die einzelnen Funktion sind umfangreich kommentiert, damit auch EinsteigerInnen (hoffentlich) nachvollziehen können, was der Code bewirkt.

## Was brauche ich?
 - Raspberry Pi (egal welches Modell)
 - Raspberry Pi Kamera-Modul (egal welches Modell, sollte auch mit auch mit der Infrarot-Kamera Pi Noir Camera laufen)
 - Raspbian oder ein anderes Betriebssystem mit Python 3

## Welches Vorwissen brauche ich ?
Du benötigst keine Programmierkenntnisse. Allerdings wirst du es etwas leichter haben, wenn du dich ein bisschen mit dem Raspberry Pi und seinem Betriebssystem auskennst. 



## Wie ist das Programm aufgebaut? 

Das Programm besteht aus zwei Dateien, 'zeitraffer.py' und 'rezepte.py'. 'zeitraffer.py' dient als Starter für das Programm, hier kann man zum Beispiel entscheiden, ob man eine Aufnahme bei Tag oder Nacht erstellen möchte. Außerdem gibt es noch die Möglichkeit Testaufnahmen mit unterschiedlich langer Belichtungszeit zu erstellen. Mit den Testaufnahmen kann man entscheiden, welche Belichtungszeit für die jeweilige Nachtaufnahme das beste Ergebnis ergibt
### Welche Einstellungen kann ich verädern?

Einfache Einstellungen lassen sich direkt im Start-Programm 'zeitraffer.py' verändern


```python
#!/usr/bin/env python3

import rezepte

# rezepte.TagAufnahme(ZeitZwischenBildern=5, ZeitVorStart=30)
# rezepte.NachtAufnahme(Belichtungszeit=6)
# rezepte.NachtTest()
```

```python
rezepte.TagAufnahme(ZeitZwischenBildern=5, ZeitVorStart=30)
```

in der Datei  /etc/rc.local kann man die Anweisung eintragen, dass dieses Script nach dem Hochfahren automatisch startet
in der Datei muss diese Zeile "python3 /home/pi/starter.py &" vor der Zeile "exit 0" eingefügt werden

einzelne Bilder in einen Film berechnen
```shell
ffmpeg -i Dateiname_%05d.png -c:v libx264 -b 5000k -r 24 -pix_fmt yuv420p Filmdatei.mp4
```
# In der /etc/rc.local wird automatisch beim boot das Python-Script starter.py im Homeverzeichnis gestartet
