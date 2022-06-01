import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pines = [24,25,8,7]
#prueba

for pin in pines:
    GPIO.setup(pin,GPIO.OUT)
        #GPIO.output(pin,0)
    
def reset():
    for pin in pines:
        GPIO.output(pin,0)

#Esta funcion define la secuencia del paso
def paso(w1,w2,w3,w4):
    GPIO.output(pines[0], w1)
    GPIO.output(pines[1], w2)
    GPIO.output(pines[2], w3)
    GPIO.output(pines[3], w4)

#Esta funcion configura el motor hacia adelante
def adelante(delay, pasos):
    for i in range(0,pasos):
        paso(1,0,1,0)
        time.sleep(delay)
        paso(0,1,1,0)
        time.sleep(delay)
        paso(0,1,0,1)
        time.sleep(delay)
        paso(1,0,0,1)
        time.sleep(delay)
    
#Esta funcion configura el motor hacia atras
def atras(delay, pasos):
    for i in range(0,pasos):
        paso(1,0,0,1)
        time.sleep(delay)
        paso(0,1,0,1)
        time.sleep(delay)
        paso(0,1,1,0)
        time.sleep(delay)
        paso(1,0,1,0)
        time.sleep(delay)

#7.2 grados por paso
# pasos = 50
# tiempo = 0.005

# adelante(tiempo,pasos)
# reset()
# time.sleep(3)
# atras(tiempo,pasos)
# reset()

# GPIO.cleanup()




