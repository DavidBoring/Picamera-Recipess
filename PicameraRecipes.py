#!/usr/bin/env python3

import picamera, time, random, os
from fractions import Fraction

# Damit keine Dateien ueberschrieben werden, wir erst ein zufaelliger String generiert, der spaeter als Dateiname benutzt wird

wort = ''

for x in range(5):
    buchstabe = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    wort = wort + buchstabe
wort = wort + '_'

# Hier geht es mit dem Camera Script weiter

camera = picamera.PiCamera()
camera.resolution = (1280, 720)
camera.led = False
camera.vflip = True
camera.hflip = True


def ledblink():
    camera.led = True
    time.sleep(0.01)
    camera.led = False

def NachtAufnahme(Belichtungszeit):
    camera.framerate = Fraction(1, Belichtungszeit) # Framerate und Shutterspeed (also Belichtungszeit) sind bei der Kamera voneinander abhängig. Die zweite Zahl sollte bei Nachtaufnahmen zwischen 1 und 6 liegen
    camera.shutter_speed = Belichtungszeit*1000000 # hier steht jetzt die Belichtungszeit, diese sollte den Wert der Framerate mal 1000000 sein. Bsp Framerate (1, 6) und Shutterspeed 6000000 entspricht einer Belichtungszeit von 6 Sekunden
    camera.iso = 800
    time.sleep(30)
    camera.exposure_mode = 'off'
    time.sleep(10)
    counter = 0
    while True:
        counter = counter + 1
        # ledblink()
        if counter < 10 :
            camera.capture('/home/pi/output/'+wort+'000'+str(counter)+'.png')
        elif counter < 100 :
            camera.capture('/home/pi/output/'+wort+'00'+str(counter)+'.png')
        elif counter < 1000 :
            camera.capture('/home/pi/output/'+wort+'0'+str(counter)+'.png')
        else :
            camera.capture('/home/pi/output/'+wort+str(counter)+'.png')
        print('Klick')


def TagAufnahme(ZeitZwischenBildern, ZeitVorStart):
    camera.sharpness = 0
    camera.contrast = 0
    camera.brightness = 50
    camera.saturation = 0
    camera.ISO = 0
    camera.video_stabilization = False
    camera.exposure_compensation = 0
    camera.exposure_mode = 'auto' # auto, night, nightpreview, backlight, spotlight, sports, snow, beach, verylong, fixedfps, antishake, fireworks
    camera.meter_mode = 'average'
    camera.awb_mode = 'auto' # auto, sunlight, cloudy, shade, tungsten, fluorescent, incandescent, flash, horizon
    camera.image_effect = 'none'
    camera.color_effects = None
    camera.rotation = 0
    camera.crop = (0.0, 0.0, 1.0, 1.0)
    time.sleep(30)
    for filename in camera.capture_continuous('/home/pi/output/'+wort+'{counter:05d}.png', 'png'): 
        ledblink()
        print('Captured %s' % filename)
        time.sleep(ZeitZwischenBildern)

def tester():
    for y in range(30):
        ledblink()
        time.sleep(0.1)
    print('Test beendet!')

def NachtTest():
    camera.framerate = Fraction(1, 6)
    camera.shutter_speed = 6000000
    camera.iso = 800
    camera.exposure_mode = 'off'
    time.sleep(30)
    ledblink()
    camera.capture('/home/pi/output/6sekundenBelichtung.png')
    camera.framerate = Fraction(1, 5)
    camera.shutter_speed = 5000000
    time.sleep(30)
    ledblink()
    camera.capture('/home/pi/output/5sekundenBelichtung.png')
    camera.framerate = Fraction(1, 4)
    camera.shutter_speed = 4000000
    time.sleep(30)
    ledblink()
    camera.capture('/home/pi/output/4sekundenBelichtung.png')
    camera.framerate = Fraction(1, 3)
    camera.shutter_speed = 3000000
    time.sleep(30)
    ledblink()
    camera.capture('/home/pi/output/3sekundenBelichtung.png')
    camera.framerate = Fraction(1, 2)
    camera.shutter_speed = 2000000
    time.sleep(30)
    ledblink()
    camera.capture('/home/pi/output/2sekundenBelichtung.png')
    camera.framerate = Fraction(1, 1)
    camera.shutter_speed = 1000000
    time.sleep(30)
    ledblink()
    camera.capture('/home/pi/output/1sekundenBelichtung.png')

    # zweiter Test im Sport Modus
    camera.framerate = Fraction(1, 6)
    camera.shutter_speed = 6000000
    camera.iso = 0
    camera.exposure_mode = 'sports'
    time.sleep(30)
    ledblink()
    camera.capture('/home/pi/output/6sekundenBelichtung2.png')
    camera.framerate = Fraction(1, 5)
    camera.shutter_speed = 5000000
    time.sleep(30)
    ledblink()
    camera.capture('/home/pi/output/5sekundenBelichtung2.png')
    camera.framerate = Fraction(1, 4)
    camera.shutter_speed = 4000000
    time.sleep(30)
    ledblink()
    camera.capture('/home/pi/output/4sekundenBelichtung2.png')
    camera.framerate = Fraction(1, 3)
    camera.shutter_speed = 3000000
    time.sleep(30)
    ledblink()
    camera.capture('/home/pi/output/3sekundenBelichtung2.png')
    camera.framerate = Fraction(1, 2)
    camera.shutter_speed = 2000000
    time.sleep(30)
    ledblink()
    camera.capture('/home/pi/output/2sekundenBelichtung2.png')
    camera.framerate = Fraction(1, 1)
    camera.shutter_speed = 1000000
    time.sleep(30)
    ledblink()
    camera.capture('/home/pi/output/1sekundenBelichtung2.png')
    print('Test abgeschlossen')
    os.system('sudo shutdown now')

def Belichtung():
    camera.start_preview()
    camera.still_stats = True
    camera.capture('stats2.jpg')
    # camera.framerate = 1
    # while True:

    #   analog = str(camera.analog_gain)
    #     digital = str(camera.digital_gain)
    #     if '/' in analog:
    #         splitter = analog.split('/')
    #         analog = int(splitter[0])/int(splitter[1])
    #     if '/' in digital:
    #         splitter = digital.split('/')
    #         digital = int(splitter[0])/int(splitter[1])
    #     print ('Analog: ', analog, 'Digital: ', digital)
    #     time.sleep(2)

# Jetzt lässt sich das Kameraprogramm auswählen. Mit # markierte Zeilen sind auskommentiert und werden nicht verarbeitet. Es lässt sich immer nur ein Kameraprogramm starten. Sind zwei oder mehr Kameraprogramme nicht auskommentiert, wird nur das erste ausgeführt

TagAufnahme(ZeitZwischenBildern=7, ZeitVorStart=0)
# NachtAufnahme(Belichtungszeit=6) # Hier kann man noch die Belichtungszeit ändern, siehe oben. Maximal 6 Sekunden
#tester() # testet ob die Kamera richtig angeschlossen ist und lässt 30 mal die LED aufleuchten
#NachtTest() # erstellt 6 Bilder mit jeweils einer Belichtungszeit von 1 bis 6 Sekunden. Hilft bei der Entscheidung, welche Belichtungszeit für einen Nachtaufnahme genutzt werden soll
#Belichtung() # Work in Progress

