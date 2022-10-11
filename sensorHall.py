# Resistencia de cable calibre 22 AWG - 1.31 Ohms/pie
# Longitud del cable 1.40 m 
# Eso representa una caida de tension de 21 mV (Despreciable)
# IMPORTANTE: si se leen valores random, aplica un sudo reboot a la raspberry ;)
# Se alimenta con 5 V
#Sensor pines (-)GND VCC (S)Vout

from gpiozero import MCP3008
import time
import os

hall49e = MCP3008(3)

def intensity_field(opt):
    vol_49e = hall49e.voltage
    if opt:
        return (vol_49e-2.5)/0.015
    else:
        return vol_49e,(vol_49e-2.5)/0.015         # Ecuacion para calcular la intensidad de campo magnetico en [mT]
                                                # E = (V-2.5)/0.015;     m = 0.015 
if __name__ == '__main__':
    list_valores = []                    # BLOQUE PARA HACER PRUEBAS SOLAMENTE, SE COMENTA PARA USAR MQTT CON PIMATIC
    try:    
        while(1):
            V,E = intensity_field(False)
            
            list_valores.append(f"\n{V}\n{E}")

            print("\nEl voltaje es:\t{0:0.4}[V]".format(V))
            print("\nEl campo magnetico es:\t{0:0.4}[mT]".format(E))
            time.sleep(3)
    except KeyboardInterrupt:
        os.system('clear')
        hall49e.close()
        with open('datos_49e.txt','wt') as f:
            for linea in list_valores:
                f.writelines(linea)