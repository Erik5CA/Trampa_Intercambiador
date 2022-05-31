import RPi.GPIO as GPIO
import time

pin = 7
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

try:
    while(True):
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(10)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(10)
except KeyboardInterrupt:
    GPIO.cleanup()
