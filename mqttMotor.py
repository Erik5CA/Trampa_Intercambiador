import motorDriver2 as M2
import carrusel as car
import estadoFrasco as edo
import mqttSSR as SSR

pasos = 250
tiempo = 0.00125

def move_position(posI,posF):
    if posF == 1 and posI == 8:
        M2.front(tiempo,pasos)
    elif posF == 8 and posI == 1:
        M2.back(tiempo,pasos)
    elif posF < posI:
        dif = posI - posF
        M2.back(tiempo,dif*pasos)
    else:
        dif = posF - posI
        M2.front(tiempo,dif*pasos)

def update_position(posF):
    with open("posicion.txt", "wt") as f:
        f.writelines(f'1\n{posF}')

def on_message_MOTOR(client, userdata, msg):
    if car.act:
        car.act = car.actualizar(car.pos_ini,car.pos_fin,tiempo,pasos)  # Esta linea mueve el frasco a la posicion 1
        update_position('1')
        edo.estadoFSA('1',client, userdata, msg)
    
    print(f'{msg.topic}\t{msg.payload}')

    if msg.payload.decode() == 'front':             # Para recibir el string
        M2.front(tiempo,pasos)
        if car.pos_fin == 6:
            car.pos_fin = 1
        else:
            car.pos_fin += 1
        update_position(car.pos_fin)
        edo.estadoFSA(car.pos_fin,client, userdata, msg)
        M2.reset()

    if msg.payload.decode() == 'back':
        M2.back(tiempo,pasos)
        if car.pos_fin == 1:
            car.pos_fin = 6
        else:
            car.pos_fin -= 1
        update_position(car.pos_fin)  
        edo.estadoFSA(car.pos_fin,client, userdata, msg)
        M2.reset()

    if msg.payload.decode() == '1':
        move_position(car.pos_fin,1)
        car.pos_fin = 1
        update_position(car.pos_fin)
        edo.estadoFrasco(client,userdata,msg)
        M2.reset()

    if msg.payload.decode() == '2':
        move_position(car.pos_fin,2)
        car.pos_fin = 2
        update_position(car.pos_fin)
        edo.estadoFrasco(client,userdata,msg)
        M2.reset()

    if msg.payload.decode() == '3':
        move_position(car.pos_fin,3)
        car.pos_fin = 3
        update_position(car.pos_fin)
        edo.estadoFrasco(client,userdata,msg)
        M2.reset()

    if msg.payload.decode() == '4':
        move_position(car.pos_fin,4)
        car.pos_fin = 4
        update_position(car.pos_fin)
        edo.estadoFrasco(client,userdata,msg)
        M2.reset()

    if msg.payload.decode() == '5':
        move_position(car.pos_fin,5)
        car.pos_fin = 5
        update_position(car.pos_fin)
        edo.estadoFrasco(client,userdata,msg)
        M2.reset()

    if msg.payload.decode() == '6':
        move_position(car.pos_fin,6)
        car.pos_fin = 6
        update_position(car.pos_fin)
        edo.estadoFrasco(client,userdata,msg)
        M2.reset()

    if msg.payload.decode() == '7':
        move_position(car.pos_fin,7)
        car.pos_fin = 7
        update_position(car.pos_fin)
        edo.estadoFrasco(client,userdata,msg)
        M2.reset()
    
    if msg.payload.decode() == '8':
        move_position(car.pos_fin,8)
        car.pos_fin = 8
        update_position(car.pos_fin)
        edo.estadoFrasco(client,userdata,msg)
        M2.reset()
    
    # if msg.payload.decode() == 'on1':
    #     SSR.SSR_operation(21,'on')
    
    # if msg.payload.decode() == 'off1':
    #     SSR.SSR_operation(21,'off')