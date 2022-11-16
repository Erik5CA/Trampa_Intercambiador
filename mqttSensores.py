import sensorBMP as BMP
import sensorCorriente as SCT
import sensorDHT as DHT
import sensorHall as _49e
import sensorTemp as LM

def estado(opt):
    if opt: 
        return f"CONECTADO"
    else:   
        return f"DESCONECTADO"

def on_message_sensores_bmp(client, userdata, msg):
    try:
        tempe, press, alt, presNm = BMP.datos()
        estadoBMP = True
        client.publish("trampa/sensor/bmp/temperatura", tempe)
        client.publish("trampa/sensor/bmp/presion", press)
        client.publish("trampa/sensor/bmp/altitud", alt)
        client.publish("trampa/sensor/bmp/presionanm", presNm)
        client.publish("trampa/sensor/bmp/status", estado(estadoBMP))
        print("\nDatos sensor BMP actualizados")
    except TypeError:
        estadoBMP = False
        client.publish("trampa/sensor/bmp/status", estado(estadoBMP))
        print(f'\n\t\tREVISAR CONEXIÓN DEL SENSOR BMP180')
    
def on_message_sensores_dht11(client, userdata, msg):
    try:
        hum, temp = DHT.datos()
        estadoDHT = True
        client.publish("trampa/sensor/dht11/temperatura", temp)
        client.publish("trampa/sensor/dht11/humedad", hum)
        client.publish("trampa/sensor/dht11/status", estado(estadoDHT))
        print("\nDatos sensor DHT11 actualizados")
    except TypeError:
        estadoDHT = False
        client.publish("trampa/sensor/dht11/status", estado(estadoDHT))
        print(f'\n\t\tREVISAR CONEXIÓN DEL SENSOR DHT11')

def on_message_sensores_Hall(client, userdata, msg):
    try:
        client.publish("trampa/sensor/49e/intensidad", _49e.intensity_field(True))
        estado49e = True
        client.publish("trampa/sensor/49e/status", estado(estado49e))
        print("\nDatos sensor 49e actualizado")
    except TypeError:
        estado49e = False
        client.publish("trampa/sensor/49e/status", estado(estado49e))
        print(f'\n\t\tREVISAR CONEXIÓN DEL SENSOR EFECTO HALL: 49e')

def on_message_sensores_LM(client, userdata, msg):
    try:
        temp = LM.datos(True)
        estadolm = True
        client.publish("trampa/sensor/lm/temperatura", temp)
        client.publish("trampa/sensor/lm/status", estado(estadolm))
        print("\nDatos sensor LM35 actualizado")
    except TypeError:
        estadolm = False
        client.publish("trampa/sensor/lm/status", estado(estadolm))
        print("\n\t\tREVISAR CONEXIÓN DEL SENSOR LM35")

def on_message_sensores_SCT(client, userdata, msg):
    client.publish("trampa/sensor/sct013/corriente1", SCT.Corriente(SCT.senI_1,SCT.relacion_1),True)
    client.publish("trampa/sensor/sct013/corriente2", SCT.Corriente(SCT.senI_2,SCT.relacion_2),True)
    print("\nDatos sensores SCT's actualizados")

def control_SSR():
    print('control SSR')