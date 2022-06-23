
import time                     #Para las pausas
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)        #Usar la numeracion de GPIO

pinDir = 27                    #Pin DIR
pinStep = 22                    #Pin Step
# numSteps = 200                  #Numero de pasos del motor
# microPausa = 0.005              #Numero de segundos de pausa


GPIO.setup(pinDir,GPIO.OUT)
GPIO.setup(pinStep,GPIO.OUT)


def adelante(tiempo,numSteps):
    GPIO.output(pinDir,0)
    for x in range(0,numSteps):
        GPIO.output(pinStep, True)
        time.sleep(tiempo)
        GPIO.output(pinStep, False)
        time.sleep(tiempo)

def atras(tiempo,numSteps):
    GPIO.output(pinDir, 1)         
    for x in range(0,numSteps):
        GPIO.output(pinStep, True)
        time.sleep(tiempo)
        GPIO.output(pinStep, False)
        time.sleep(tiempo)

def reset():
    GPIO.output(pinDir,0)
    GPIO.output(pinStep,0)
