from math import sqrt
from gpiozero import MCP3008
import time
import os

senI_1 = MCP3008(1)
senI_2 = MCP3008(2)

muestras = 300 #Numero de muestras
delay = 0.00001 #Tiempo entre cadada muestra, doble de la frecuencias 900 Hz
#sumCor = 0 #Inicio del contador
# opt = input('\nIngrese una opción: \n1) Relación de 20\n2) Relación de 100\n')
# if opt == '1':
relacion_1 = 100 #Relacion del sensor 100A/1V
# elif opt == '2':
relacion_2 = 20
# else:   print('Elige una opcion correcta crack')


def Corriente(senI,relacion):
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
    return sqrt(sumTot/muestras), vol

try:
    os.system("clear")
    while(1):
        Irms_1,vol_list_1 = Corriente(senI_1, relacion_1)
        Irms_2,vol_list_2 = Corriente(senI_2, relacion_2)

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
