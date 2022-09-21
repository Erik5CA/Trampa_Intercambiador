import RPi.GPIO as GPIO
import time
import mqttMotor
import carrusel

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pines = [24,25,8,7]
hab = 21,20
GPIO.setup(hab[0],GPIO.OUT)
GPIO.setup(hab[1],GPIO.OUT)

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

#Secuencia para el motor
sec1 = [[1,0,1,0],
        [0,1,1,0],
        [0,1,0,1],
        [1,0,0,1]]
 
sec2 = [[1,0,0,1],
        [0,1,0,1],
        [0,1,1,0],
        [1,0,1,0]]

#Esta funcion mueve el motor hacia adelante o hacia atras
def movMotor(delay,pasos,direccion,apun):
    GPIO.output(hab[0],1)#Habilitamos los pines del motor
    GPIO.output(hab[1],1)
    print(apun)
    scf = apun
    for i in range(apun,pasos+apun):
        if direccion == False:
            carrusel.dir = 0
            print(str(scf) + " " + str(i+1) + " " + str(sec1[scf]))
            paso(sec1[scf][0],sec1[scf][1],sec1[scf][2],sec1[scf][3])
            scf = (i + 1) % 4
            time.sleep(delay)
        else:
            carrusel.dir = 1
            print(str(scf) + " " + str(i+1) + " " + str(sec2[scf]))
            paso(sec2[scf][0],sec2[scf][1],sec2[scf][2],sec2[scf][3])
            scf = (i + 1) % 4
            time.sleep(delay)
    GPIO.output(hab[0],0)
    GPIO.output(hab[1],0)
    mqttMotor.apu = scf

#opt(true) = conversion a back
#opt(false) = conversion front
def conv(scf,opt):
    if opt:
        if scf == 0:
            mqttMotor.apu = 3
        elif scf == 1:
            mqttMotor.apu = 2
        elif scf == 2:
            mqttMotor.apu = 1
        else:
            mqttMotor.apu = 0
    else:
        if scf == 3:
            mqttMotor.apu = 0
        elif scf == 2:
            mqttMotor.apu = 1
        elif scf == 1:
            mqttMotor.apu = 2
        else:
            mqttMotor.apu = 3

# #7.2 grados por paso
# pasos = 50 
# tiempo = 0.005
#apu = 0

# apu = movMotor(tiempo,pasos,False,apu)
# reset()
# time.sleep(3)
# print("apuntador" + str(apu))
# apu = conv(apu,True)
# apu = movMotor(tiempo,pasos,True,apu)
# reset()
# time.sleep(3)
# print("apuntador" + str(apu))
# apu = conv(apu,False)
# apu = movMotor(tiempo,pasos,False,apu)
# reset()
# time.sleep(3)
# print("apuntador" + str(apu))
# apu = movMotor(tiempo,pasos,True,apu)
# reset()
# time.sleep(3)
# print("apuntador" + str(apu))
# apu = movMotor(tiempo,pasos,False,apu)
# reset()
# time.sleep(3)
# print("apuntador" + str(apu))
# apu = movMotor(tiempo,pasos,False,apu)
# reset()
# time.sleep(3)
# apu = movMotor(tiempo,pasos,False,apu)
# reset()
# time.sleep(3)
# apu = movMotor(tiempo,pasos,False,apu)
# reset()


# GPIO.cleanup()




