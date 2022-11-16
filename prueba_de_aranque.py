# sudo nano /etc/rc.local
# En el archivo rc.local, inserte la siguiente línea de código antes de la línea 
# «exit 0»: python3 /home/pi/PiCounter/display.py &.
import time

import RPi.GPIO as GPIO

pin = 17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

try:
    while True:
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(10)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(10)
except KeyboardInterrupt:
    GPIO.cleanup()