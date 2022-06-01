from gpiozero import InputDevice, OutputDevice
import motorDriver1
import time

senHerradura = InputDevice(19)

try:
    while(True): 
        while(senHerradura.is_active == False):
            motorDriver1.adelante(0.005,50)
        motorDriver1.reset()

except KeyboardInterrupt:
    senHerradura.close()
    


