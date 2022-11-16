# Este codigo es para el driver A4988 que se alimenta con 5V de la raspberry
# Checar el pinout de la raspberry para saber cuales estan en bajo y cambiar el pinHab

import time                     # Para las pausas
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)          # Usar la numeracion de GPIO

pinDir = 27                     # Pin DIR
pinHab = 24                     # Pin para habilitar las funciones
pinStep = 22
pinSleep = 5
pinReeset = 6

frec = 800
microPausa = 1/frec        # Segundos para los ultimos 60 pasos
numSteps = 250          # Tiempo para girar una posicion en la trampa

GPIO.setup(pinHab,GPIO.OUT)
GPIO.setup(pinDir,GPIO.OUT)
GPIO.setup(pinSleep,GPIO.OUT)
GPIO.setup(pinStep,GPIO.OUT)
GPIO.setup(pinReeset,GPIO.OUT)

def front(tiempo, numSteps):
    GPIO.output(pinHab,0)
    GPIO.output(pinDir,0)
    GPIO.output(pinReeset,1)
    GPIO.output(pinSleep,1)

    for x in range(0,numSteps):
        GPIO.output(pinStep, True)
        time.sleep(tiempo)
        GPIO.output(pinStep, False)
        time.sleep(tiempo)

def back(tiempo, numSteps):
    GPIO.output(pinHab,0)
    GPIO.output(pinDir,1)  
    GPIO.output(pinReeset,1)
    GPIO.output(pinSleep,1)       
    
    for x in range(0,numSteps):
        GPIO.output(pinStep, True)
        time.sleep(tiempo)
        GPIO.output(pinStep, False)
        time.sleep(tiempo)

def reset():
    GPIO.output(pinStep,0)
    GPIO.output(pinDir,0)
    GPIO.output(pinHab,1)
    GPIO.output(pinReeset,0)
    GPIO.output(pinSleep,0)

if __name__ == '__main__':
    front(microPausa,3*numSteps)
    reset()
    time.sleep(2)
    back(microPausa,3*numSteps)
    reset()