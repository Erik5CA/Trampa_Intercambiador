import sensorDHT as DHT

def on_message_sensores_DHT(client, userdata, msg):
    client.publish("trampa/sensor/dht11/temperatura", DHT.tempDht)
    client.publish("trampa/sensor/dht11/humedad", DHT.humDht)
    print("Actualizado")