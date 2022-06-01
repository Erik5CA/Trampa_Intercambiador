import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
 
pin = 7
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("trampa/#")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if msg.payload.decode() == "0":
        print("OFF")
        GPIO.output(pin, GPIO.LOW)
    else:
        print("ON")
        GPIO.output(pin, GPIO.HIGH)

try:
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("test.mosquitto.org", 1883, 60)

    client.loop_forever()
except KeyboardInterrupt:
    GPIO.cleanup()
