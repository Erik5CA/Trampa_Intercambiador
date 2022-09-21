
from gpiozero import MCP3008
import time

lm = MCP3008(1)

try:
    while(1):
        volLm = lm.voltage
        tempLm = lm.voltage*100
        print("El voltaje es: " + str(volLm)+ " V \n")
        print("La temperatura es: " + str(tempLm)+ " °C \n")
        time.sleep(2)

except KeyboardInterrupt:
    lm.close()