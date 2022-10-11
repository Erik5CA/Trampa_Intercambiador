# Control del carrusel para la posicion inicial
import motorDriver2 as M2

with open("posicion.txt", "rt") as f:
    lis_pos = f.readlines()
    pos_ini = int(lis_pos[0])
    pos_fin = int(lis_pos[1])

# tiempo = 0.005
# numSteps = 250

act = True

def default(x,y):
    diferencia = y - x
    return diferencia

def actualizar(pos_ini,pos_fin,tiempo,numSteps):
    dif = default(pos_ini,pos_fin)
    if dif != 0:
        pos_fin = 1
        M2.front(tiempo,dif*numSteps)           # Hay que mandar la diferencia y manejarla desde el mqttMotor2

        with open("posicion.txt", "wt") as f:
            f.writelines(f'{pos_ini}\n{pos_fin}')
        return False
    else:
        print("\nYa estas en la posicion 1")
        return False