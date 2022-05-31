
import time                     #Para las pausas
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)        #Usar la numeracion de pines de la placa

pinDir = 11                    #Pin DIR
pinStep = 7                    #Pin Step
numSteps = 200                  #Numero de pasos del motor
microPausa = 0.005              #Numero de segundos de pausa


GPIO.setup(pinDir,GPIO.OUT)
GPIO.setup(pinStep,GPIO.OUT)
try: 
    while True:

            GPIO.output(pinDir,0)           #Establezco una direccion (0 o 1)

            for x in range(0,numSteps):
                    GPIO.output(pinStep, True)
                    time.sleep(microPausa)
                    GPIO.output(pinStep, False)
                    time.sleep(microPausa)

            time.sleep(microPausa)

            GPIO.output(pinDir, 1)          #Cambio de direccion

            for x in range(0,numSteps):
                    GPIO.output(pinStep, True)
                    time.sleep(microPausa)
                    GPIO.output(pinStep, False)
                    time.sleep(microPausa)
except KeyboardInterrupt:
    GPIO.cleanup()