import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ciclo = 50 
frec = 30

GPIO.setup(22, GPIO.OUT)
azul = GPIO.PWM(22, frec)
azul.start(ciclo)    

while True:
    if frec > 10:
        frec = frec - 3
        print(frec)
        azul.ChangeFrequency(frec)
        time.sleep(0.02)
    else:
        break
    time.sleep(4)


# for i in range(ciclo,9,-1):
#     print(f'{i}')
    
#     azul.ChangeDutyCycle(ciclo - i)
#     time.sleep(0.02)           
# azul.stop()
# print("Ciclo completo")