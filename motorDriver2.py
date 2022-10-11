# Este codigo es para el driver A4988 que se alimenta con 5V de la raspberry
# Checar el pinout de la raspberry para saber cuales estan en bajo y cambiar el pinHab

import time                     # Para las pausas
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)          # Usar la numeracion de GPIO

pinDir = 27                     # Pin DIR
pinStep = 22                    # Pin Step
pinHab = 24                     # Pin para habilitar las funciones
pinSleep = 5
pinReeset = 6

numSteps = 250                  # Numero de pasos del motor
microPausa = 0.0001              # Numero de segundos de pausa

GPIO.setup(pinHab,GPIO.OUT)
GPIO.setup(pinDir,GPIO.OUT)
GPIO.setup(pinStep,GPIO.OUT)
GPIO.setup(pinSleep,GPIO.OUT)
GPIO.setup(pinReeset,GPIO.OUT)

def front(tiempo,numSteps):
    GPIO.output(pinHab,0)
    GPIO.output(pinDir,0)
    
    GPIO.output(pinReeset,1)
    GPIO.output(pinSleep,1)

    for x in range(0,numSteps):
        GPIO.output(pinStep, True)
        time.sleep(tiempo)
        GPIO.output(pinStep, False)
        time.sleep(tiempo)

def back(tiempo,numSteps):
    GPIO.output(pinHab,0)
    GPIO.output(pinDir, 1)  
    
    GPIO.output(pinReeset,1)
    GPIO.output(pinSleep,1)       
    
    for x in range(0,numSteps):
        GPIO.output(pinStep, True)
        time.sleep(tiempo)
        GPIO.output(pinStep, False)
        time.sleep(tiempo)

def reset():
    GPIO.output(pinDir,0)
    GPIO.output(pinStep,0)
    GPIO.output(pinHab,1)

    GPIO.output(pinReeset,0)
    GPIO.output(pinSleep,0)

if __name__ == '__main__':
    front(microPausa,numSteps)
    reset()
    time.sleep(2)
    back(microPausa, numSteps)
    reset()