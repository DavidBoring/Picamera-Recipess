# Picamera Zeitraffer-Aufnahmen  :movie_camera:
![Zeitraffer Gif](PiZeitraffer.gif "Zeitraffer Gif")
## :squirrel: Was macht dieses Programm ?
 Mit dem Programm lassen sich mit dem Raspberry Pi und dem Kamera-Modul einfach Zeitrafferaufnamen erstellen. Der Code basiert weitesgehend auf der offiziellen Dokumentation des Kamera-Moduls [Picamera Docs](https://picamera.readthedocs.io/)

 Die einzelnen Funktion sind umfangreich kommentiert, damit auch EinsteigerInnen (hoffentlich) nachvollziehen können, was der Code bewirkt.

## :water_buffalo: Was brauche ich?
 - Raspberry Pi (egal welches Modell)
 - Raspberry Pi Kamera-Modul (egal welches Modell, sollte auch mit auch mit der Infrarot-Kamera Pi Noir Camera laufen)
 - Raspbian oder ein anderes Betriebssystem mit Python 3

## :whale2: Welches Vorwissen brauche ich ?
Du benötigst keine Programmierkenntnisse. Allerdings wirst du es etwas leichter haben, wenn du dich ein bisschen mit dem Raspberry Pi und seinem Betriebssystem auskennst. Und du solltest Wissen, was ein Texteditor ist und wie du damit eine Datei veränderst.

## :ox: Wie ist das Programm aufgebaut ? 

Das Programm besteht aus zwei Dateien, 'zeitraffer.py' und 'rezepte.py'. 'zeitraffer.py' dient als Starter für das Programm, hier kann man zum Beispiel entscheiden, ob man eine Aufnahme bei Tag oder Nacht erstellen möchte. Außerdem gibt es noch die Möglichkeit Testaufnahmen mit unterschiedlich langer Belichtungszeit zu erstellen. Mit den Testaufnahmen kann man entscheiden, welche Belichtungszeit für die jeweilige Nachtaufnahme das beste Ergebnis ergibt.
### :octopus: Welche Einstellungen kann ich verädern?

Einfache Einstellungen lassen sich direkt im Start-Programm 'zeitraffer.py' verändern, der Programm-Code sieht so aus:

```python
#!/usr/bin/env python3

import rezepte

# rezepte.TagAufnahme(ZeitZwischenBildern=5, ZeitVorStart=30)
# rezepte.NachtAufnahme(Belichtungszeit=6)
# rezepte.NachtTest()
```

Die Raute **(#)** vor einer Zeile bedeutet für die Programmiersprache Python, dass diese Zeile nicht bearbeitet werden soll. Wollen wir also zum Beispiel eine Zeitrafferaufnahme bei Tag starten, müssen wir die Raute vor der dieser Zeile entfernen:

```python
rezepte.TagAufnahme(ZeitZwischenBildern=5, ZeitVorStart=30)
```
In der Klammer stehen die sogenannten *Parameter*, in diesen Parametern können wir zwei Sachen bestimmen:
1. Der zeitliche Abstand in denen ein Foto gemacht werden soll. Hier kannst du also die Pause zwischen zwei Bildern in Sekunden angeben. Je nachdem, was du für einen Zeitrafferfilm drehen möchtest 
    - [dieser Film](http://cloud.christianbusse.net/index.php/s/gw3yskEXKmHEXG3) wurde zum Beispiel über mehrere Tage gedreht. Die Pause zwischen zwei Bildern ist hier 150 Sekunden, also zweieinhalb Minuten lang
    - [und dieser Film](http://cloud.christianbusse.net/index.php/s/TMGLRkwA9Z6EsYc) wurde nur ein Nachmittag lang gefilmt mit einer Pause von 5 Sekunden

## :turtle: Wie mache ich aus den einzelnen Bildern einen Film?

## :dromedary_camel: Wie kann ich das Programm automatisch starten lassen, sobald ich meinen Raspberry anschalte ?

in der Datei  /etc/rc.local kann man die Anweisung eintragen, dass dieses Script nach dem Hochfahren automatisch startet
in der Datei muss diese Zeile "python3 /home/pi/starter.py &" vor der Zeile "exit 0" eingefügt werden

einzelne Bilder in einen Film berechnen
```shell
ffmpeg -i Dateiname_%05d.png -c:v libx264 -b 5000k -r 24 -pix_fmt yuv420p Filmdatei.mp4
```
In der /etc/rc.local wird automatisch beim boot das Python-Script starter.py im Homeverzeichnis gestartet

## :blowfish: Beispiele

## :postal_horn: Noch Fragen ?
