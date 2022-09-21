#Control del carrusel
<<<<<<< HEAD
import motorDriver1 as M2
import mqttMotor
import estadoFrasco as edo

=======
#import motorDriver2 as M2
#impor motorDriver1 
>>>>>>> 873427da58346f8373ef90663db049f564c3553f
posiciones = open("posicion.txt", "rt")
pos_ini = int(posiciones.readline())
pos_fin = int(posiciones.readline())
#dir = int(posiciones.readline()) #Variable a leer para obtener direccion del carruser y comparara para hacer la conversion
posiciones.close()

tiempo = 0.0001
numSteps = 25

def default(x,y):
    diferencia = y - x
    return diferencia

dif = default(pos_ini,pos_fin)

<<<<<<< HEAD
if dif != 0:
    pos_fin = 1
    M2.movMotor(tiempo,dif*numSteps,False,0)
    posiciones = open("posicion.txt", "wt")
    posiciones.write(str(pos_ini)+"\n"+str(pos_fin)+"\n"+'0')
    posiciones.close()
    #mov = True
else:
    print("Ya estas en la posición 1")
    #mov = False
=======
def actulizarpos():
    if dif != 0:
        pos_fin = 1
        motorDriver1.movMotor(tiempo,dif*numSteps,False,apu)
        #M2.adelante(tiempo,dif*numSteps)
        posiciones = open("posicion.txt", "wt")
        posiciones.write(str(pos_ini)+"\n"+str(pos_fin))
        posiciones.close()
    else:
        print("Ya estas en la posición 1")
>>>>>>> 873427da58346f8373ef90663db049f564c3553f
