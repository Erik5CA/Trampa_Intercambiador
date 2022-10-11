
import sensorBMP as BMP

def on_message_sensores_BMP(client, userdata, msg):
    client.publish("trampa/sensor/bmp/temperatura", BMP.tempBmp)
    client.publish("trampa/sensor/bmp/presion", BMP.presBmp)
    client.publish("trampa/sensor/bmp/altitud", BMP.altBmp)
    client.publish("trampa/sensor/bmp/presionanm", BMP.presNmBmp)
    print("\nActualizado")
    