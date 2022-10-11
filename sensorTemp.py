# ESTE SENSOR SE ALIMENTA CON 5 [V]
# Pines del sensor, vista desde abajo: (V+   Vout    GND)

from gpiozero import MCP3008
import time

lm = MCP3008(0)

def temperatura(opt):
    if opt:
        return lm.voltage*100
    else:
        return lm.voltage, lm.voltage*100

if __name__ == '__main__':
    try:
        while True:
            V,T = temperatura(False)
            print(f"El voltaje es: {V}")
            print(f"La temperatura es: {T}")
            time.sleep(2)
    except KeyboardInterrupt:
        lm.close()