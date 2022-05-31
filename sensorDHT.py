import Adafruit_DHT as DHT
import time

sensorDht = DHT.DHT11
pinDht = 17

humDht, tempDht = DHT.read_retry(sensorDht, pinDht)

# print('Temperatura = {0:0.2f} *C'.format(tempDht))
# print('Humedad = {0:0.2f} %'.format(humDht))