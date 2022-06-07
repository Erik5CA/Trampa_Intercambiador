
#Control del carrusel
import motorDriver2 as M2

posiciones = open("posicion.txt", "rt")
pos_ini = int(posiciones.readline())
pos_fin = int(posiciones.readline())
posiciones.close()

tiempo = 0.005
numSteps = 33

def default(x,y):
    diferencia = y - x
    return diferencia

dif = default(pos_ini,pos_fin)

if dif != 0:
    pos_fin = 1
    M2.adelante(tiempo,dif*numSteps)
    posiciones = open("posicion.txt", "wt")
    posiciones.write(str(pos_ini)+"\n"+str(pos_fin))
    posiciones.close()
else:
    print("Ya estas en la posición 1")