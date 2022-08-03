
#Control del carrusel
#import motorDriver2 as M2
#impor motorDriver1 
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
