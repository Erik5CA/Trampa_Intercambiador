# 1. Comando sudo raspi-config
# 2. Interfacing -> I2C
# 3. Comando sudo reboot
# 4. OK
# pines configurados
# SDA = GPIO 2 (SDA I2C)
# SCL = GPIO 3 (SCL I2C)
# Alimentacion de 3.3 V

import Adafruit_BMP.BMP085 as BMP

sensorBmp = BMP.BMP085()
tempBmp = sensorBmp.read_temperature()
presBmp = sensorBmp.read_pressure()
altBmp = sensorBmp.read_altitude()
presNmBmp = sensorBmp.read_sealevel_pressure()