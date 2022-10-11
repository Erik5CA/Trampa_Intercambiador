# Se alimentan con 5 [V]
from math import sqrt
from gpiozero import MCP3008
import time
import os

senI_1 = MCP3008(1)
senI_2 = MCP3008(2)

muestras = 1000          # Numero de muestras
delay = 0.005         # Tiempo entre cadada muestra, doble de la frecuencias 100 kHz
relacion_1 = 100        # Relacion del sensor 100A/1V
relacion_2 = 20         # Relacion del sensor 20A/1V


def Corriente(senI,relacion,opt):
    """Esta función retorna el valor de la corriente sensada en el SCT013

    Args:
        senI (MCP3008): Objeto que cotiene el voltaje leido por el MCP3008
        relacion (int): Relación de amperaje/voltaje del sensor SCT013
        opt (bool): Opción para retornar un valor o una tupla de valores

    Returns:
        float|tuple[float, list]: Valor de corriente o tupla de corriente y lista de voltajes
    """
    sumCor = 0
    vol = []
    for i in range(muestras):
        volSen = senI.voltage
        vol.append(volSen)
        corSen = volSen*relacion
        corSen2 = corSen*corSen
        sumCor = sumCor + corSen2
        time.sleep(delay)
    sumTot = sumCor*2
    if opt:
        return sqrt(sumTot/muestras)
    else: 
        return sqrt(sumTot/muestras), vol

if __name__ == '__main__':
    try:
        os.system("clear")
        while True:
            Irms_1,vol_list_1 = Corriente(senI_1, relacion_1,False)
            Irms_2,vol_list_2 = Corriente(senI_2, relacion_2,False)

            with open('Muestras1.txt','wt') as f:
                for v in vol_list_1:
                    f.writelines(str(v) + '\n')
                print('\nArchivo 1 escrito cramck')

            with open('Muestras2.txt','wt') as f:
                    for v in vol_list_2:
                        f.writelines(str(v) + '\n')
                    print('\nArchivo 2 escrito cramck')
        
            print('\nCorriente sensor 100A/1V: {0:0.4f} [A]'.format(Irms_1))
            print('\nCorriente sensor 20A/1V: {0:0.4f} [A]'.format(Irms_2))

            time.sleep(5)

    except KeyboardInterrupt:
        senI_1.close()
        senI_2.close()