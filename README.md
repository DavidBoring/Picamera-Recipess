# Picamera Recipes

[Picamera Docs](https://picamera.readthedocs.io/)


in der Datei  /etc/rc.local kann man die Anweisung eintragen, dass dieses Script nach dem Hochfahren automatisch startet
in der Datei muss diese Zeile "python3 /home/pi/starter.py &" vor der Zeile "exit 0" eingefügt werden

einzelne Bilder in einen Film berechnen
`ffmpeg -i Dateiname_%04d.png -c:v libx264 -r 15 -pix_fmt yuv420p Dateiname.mp4`
möglichwerweise ergibt dieser Befehl Videos mit besserer Qualität (weniger Artefakte)
`ffmpeg -i Dateiname_%04d.png -c:v libx264 -b 5000k -r 24 -pix_fmt yuv420p Dateiname.mp4`