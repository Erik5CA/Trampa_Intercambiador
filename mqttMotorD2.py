import motorDriver2
import carrusel 
import estadoFrasco as edo

pasos = 33
tiempo = 0.001

def mover(posI,posF):
    if posF == 1 and posI == 6:
        motorDriver2.adelante(tiempo,pasos)
    elif posF == 6 and posI == 1:
        motorDriver2.atras(tiempo,pasos)
    elif posF < posI:
        dif = posI - posF
        motorDriver2.atras(tiempo,dif*pasos)
    else:
        dif = posF - posI
        motorDriver2.adelante(tiempo,dif*pasos)

def actualizar_pos(posF):
    posiciones = open("posicion.txt", "wt")
    posiciones.write("1"+"\n"+str(posF))
    posiciones.close()


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if msg.payload.decode() == 'front': ##decode() para recibir el string
        motorDriver2.adelante(tiempo,pasos)
        if carrusel.pos_fin == 6:
            carrusel.pos_fin = 1
        else:
            carrusel.pos_fin += 1
        actualizar_pos(carrusel.pos_fin)
        edo.estadoFSA(carrusel.pos_fin,client, userdata, msg)
        motorDriver2.reset()
    if msg.payload.decode() == 'back':
        motorDriver2.atras(tiempo,pasos)
        if carrusel.pos_fin == 1:
            carrusel.pos_fin = 6
        else:
            carrusel.pos_fin -= 1
        actualizar_pos(carrusel.pos_fin)  
        edo.estadoFSA(carrusel.pos_fin,client, userdata, msg)
        motorDriver2.reset()
    if msg.payload.decode() == '1':
        mover(carrusel.pos_fin,1)
        carrusel.pos_fin = 1
        actualizar_pos(carrusel.pos_fin)
        edo.estadoFrasco(client,userdata,msg)
        motorDriver2.reset()
    if msg.payload.decode() == '2':
        mover(carrusel.pos_fin,2)
        carrusel.pos_fin = 2
        actualizar_pos(carrusel.pos_fin)
        edo.estadoFrasco(client,userdata,msg)
        motorDriver2.reset()
    if msg.payload.decode() == '3':
        mover(carrusel.pos_fin,3)
        carrusel.pos_fin = 3
        actualizar_pos(carrusel.pos_fin)
        edo.estadoFrasco(client,userdata,msg)
        motorDriver2.reset()
    if msg.payload.decode() == '4':
        mover(carrusel.pos_fin,4)
        carrusel.pos_fin = 4
        actualizar_pos(carrusel.pos_fin)
        edo.estadoFrasco(client,userdata,msg)
        motorDriver2.reset()
    if msg.payload.decode() == '5':
        mover(carrusel.pos_fin,5)
        carrusel.pos_fin = 5
        actualizar_pos(carrusel.pos_fin)
        edo.estadoFrasco(client,userdata,msg)
        motorDriver2.reset()
    if msg.payload.decode() == '6':
        mover(carrusel.pos_fin,6)
        carrusel.pos_fin = 6
        actualizar_pos(carrusel.pos_fin)
        edo.estadoFrasco(client,userdata,msg)
        motorDriver2.reset()