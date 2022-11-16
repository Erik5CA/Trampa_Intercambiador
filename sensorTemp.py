# ESTE SENSOR SE ALIMENTA CON 5 [V]
# Pines del sensor, vista desde abajo: (V+   Vout    GND)

from gpiozero import MCP3008
import time


def datos(opt):
    """Esta función regresa la temperatura sensada por el LM35 en configuración half

    Args:
        opt (bool): Opción para retornar el valor de temperatura o voltaje y la temperatura

    Returns:
        float | (float, float): Valor de la temperatura o una tupla (Voltaje, Temperatura)
    """
    lm = MCP3008(0)
    V = lm.voltage
    T = lm.voltage*100

    if opt:
        if V >= 0.02 and V <= 1.5 and T == V*100:
            return lm.voltage*100
        else: return TypeError
    else:
        if V >= 0.02 and V <= 1.5 and T == V*100:
            return (lm.voltage, lm.voltage*100)
        else: return TypeError

if __name__ == '__main__':
    
    lm = MCP3008(0)
    try:
        while True:
            try:
                V,T = datos(False)
                print(f"\nEl voltaje es: {V:.4f}\nLa temperatura es: {T:.4f}")
                time.sleep(3)
            except TypeError:
                print('\n\t\tREVISAR CONEXIÓN DEL SENSOR LM35')
    except KeyboardInterrupt:
        lm.close()