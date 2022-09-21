#1. Comando sudo raspi-config
#2. Interfacing -> I2C
#3. Comando sudo reboot
#4. OK

import Adafruit_BMP.BMP085 as BMP
import time


#pines configurados
#SDA = GPIO 2 (SDA I2C)
#SCL = GPIO 3 (SCL I2C)

sensorBmp = BMP.BMP085()
tempBmp = sensorBmp.read_temperature()
presBmp = sensorBmp.read_pressure()
altBmp = sensorBmp.read_altitude()
presNmBmp = sensorBmp.read_sealevel_pressure()

# pres0 = presNmBmp/((1-(altBmp/44330))**5.255) 

# print('Temperatura = {0:0.2f} *C'.format(tempBmp))
# print('Presion = {0:0.2f} *Pa'.format(presBmp))
# print('Altitud = {0:0.2f} *m'.format(altBmp))
# print('Presion a nivel del mar = {0:0.2f} *Pa'.format(pres0))


