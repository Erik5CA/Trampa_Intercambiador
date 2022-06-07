import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
import mqttBMP as BMP
import mqttDHT as DHT
import mqttMotor as Motor

def on_connect(client, userdata, flags, rc): ##comentario
    print("Connected with result code "+str(rc))
    client.subscribe("trampa/#")

try:
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = Motor.on_message

    client.connect("test.mosquitto.org", 1883, 60)
    client.message_callback_add("trampa/sensor/dato/bmp",BMP.on_message_sensores_BMP)
    client.message_callback_add("trampa/sensor/dato/dht",DHT.on_message_sensores_DHT)
    client.loop_forever()
except KeyboardInterrupt:
    Motor.motorDriver1.reset()
    GPIO.cleanup()

