# Se alimenta con 5V

import Adafruit_DHT as DHT

sensorDht = DHT.DHT11
pinDht = 23

humDht, tempDht = DHT.read_retry(sensorDht, pinDht)