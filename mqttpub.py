import paho.mqtt.client as mqtt
import time
import sensorBMP as BMP

client = mqtt.Client()
client.connect("test.mosquitto.org", 1883, 60)
client.publish("trampa/sensor/bmp/temperatura", BMP.tempBmp)
client.publish("trampa/sensor/bmp/presion", BMP.presBmp)
client.publish("trampa/sensor/bmp/altitud", BMP.altBmp)
client.publish("trampa/sensor/bmp/presionanm", BMP.presNmBmp)
