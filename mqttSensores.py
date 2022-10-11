import sensorBMP as BMP
import sensorDHT as DHT
import sensorHall as _49e
import sensorTemp as LM
import sensorCorriente as SCT

def on_message_sensores_BMP(client, userdata, msg):
    client.publish("trampa/sensor/bmp/temperatura", BMP.tempBmp)
    client.publish("trampa/sensor/bmp/presion", BMP.presBmp)
    client.publish("trampa/sensor/bmp/altitud", BMP.altBmp)
    client.publish("trampa/sensor/bmp/presionanm", BMP.presNmBmp)
    print("\nDatos sensor BMP actualizados")

def on_message_sensores_DHT(client, userdata, msg):
    client.publish("trampa/sensor/dht11/temperatura", DHT.tempDht)
    client.publish("trampa/sensor/dht11/humedad", DHT.humDht)
    print("\nDatos sensor DHT actualizados")

def on_message_sensores_Hall(client, userdata, msg):
    client.publish("trampa/sensor/49e/intensidad", _49e.intensity_field(True))
    print("\nDatos sensor 49e actualizado")

def on_message_sensores_LM(client, userdata, msg):
    client.publish("trampa/sensor/lm/temperatura", LM.temperatura(True))
    print("\nDatos sensor LM35 actualizado")

def on_message_sensores_SCT(client, userdata, msg):
    client.publish("trampa/sensor/sct013/corriente1", SCT.Corriente(SCT.senI_1,SCT.relacion_1),True)
    client.publish("trampa/sensor/sct013/corriente2", SCT.Corriente(SCT.senI_2,SCT.relacion_2),True)
    print("\nDatos sensores SCT's actualizados")