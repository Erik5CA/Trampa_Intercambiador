# Se alimenta con 5V

import Adafruit_DHT as DHT


sensorDht = DHT.DHT11
pinDht = 23

def datos():
    retries = 1
    try:
        humDht, tempDht = DHT.read_retry(sensorDht, pinDht, retries)
        if humDht is not None and tempDht is not None:
            return humDht,tempDht
    except TypeError:
        print("\n\t\tSENSOR DHT11 DESCONECTADO")