
import motorDriver1
import carrusel 
import estadoFrasco as edo

pasos = 25
tiempo = 0.0001
apu = 0

def mover(posI,posF,apu):
    if posF == 1 and posI == 8:
        if carrusel.dir == 0:
            motorDriver1.movMotor(tiempo,pasos,False,apu)
        else:
            motorDriver1.conv(apu,False)
            motorDriver1.movMotor(tiempo,pasos,False,apu)
    elif posF == 8 and posI == 1:
        if carrusel.dir == 1:
            motorDriver1.movMotor(tiempo,pasos,True,apu)
        else:
            motorDriver1.conv(apu,True)
            motorDriver1.movMotor(tiempo,pasos,True,apu)
    elif posF < posI:
        dif = posI - posF
        if carrusel.dir == 1:
            motorDriver1.movMotor(tiempo,dif*pasos,True,apu)
        else:
            motorDriver1.conv(apu,True)
            motorDriver1.movMotor(tiempo,dif*pasos,True,apu)
    else:
        dif = posF - posI
        if carrusel.dir == 0:
            motorDriver1.movMotor(tiempo,dif*pasos,False,apu)
        else:
            motorDriver1.conv(apu,False)
            motorDriver1.movMotor(tiempo,dif*pasos,False,apu)

def actualizar_pos(posF):
    posiciones = open("posicion.txt", "wt")
    posiciones.write("1"+"\n"+str(posF)+"\n"+str(carrusel.dir))
    posiciones.close()

def on_message(client, userdata, msg):
    if carrusel.mov:
        client.publish("trampa/frasco/estado", edo.frascos['estado'][0])
        client.publish("trampa/frasco/actual", "Frasco: " + str(1))
        carrusel.mov = False
    print(msg.topic+" "+str(msg.payload))
    if msg.payload.decode() == 'front': ##decode() para recibir el string
        if carrusel.dir == 0:
            motorDriver1.movMotor(tiempo,pasos,False,apu)
        else:
            motorDriver1.conv(apu,False)
            motorDriver1.movMotor(tiempo,pasos,False,apu)
        if carrusel.pos_fin == 8:
            carrusel.pos_fin = 1
        else:
            carrusel.pos_fin += 1
        actualizar_pos(carrusel.pos_fin)
        edo.estadoFSA(carrusel.pos_fin,client, userdata, msg)
        motorDriver1.reset()
    if msg.payload.decode() == 'back':
        if carrusel.dir == 1:
            motorDriver1.movMotor(tiempo,pasos,True,apu)
        else:
            motorDriver1.conv(apu,True)
            motorDriver1.movMotor(tiempo,pasos,True,apu)
        if carrusel.pos_fin == 1:
            carrusel.pos_fin = 8
        else:
            carrusel.pos_fin -= 1
        actualizar_pos(carrusel.pos_fin)  
        edo.estadoFSA(carrusel.pos_fin,client, userdata, msg)
        motorDriver1.reset()
    if msg.payload.decode() == '1':
        mover(carrusel.pos_fin,1,apu)
        carrusel.pos_fin = 1
        actualizar_pos(carrusel.pos_fin)
        edo.estadoFrasco(client,userdata,msg)
        motorDriver1.reset()
    if msg.payload.decode() == '2':
        mover(carrusel.pos_fin,2,apu)
        carrusel.pos_fin = 2
        actualizar_pos(carrusel.pos_fin)
        edo.estadoFrasco(client,userdata,msg)
        motorDriver1.reset()
    if msg.payload.decode() == '3':
        mover(carrusel.pos_fin,3,apu)
        carrusel.pos_fin = 3
        actualizar_pos(carrusel.pos_fin)
        edo.estadoFrasco(client,userdata,msg)
        motorDriver1.reset()
    if msg.payload.decode() == '4':
        mover(carrusel.pos_fin,4,apu)
        carrusel.pos_fin = 4
        actualizar_pos(carrusel.pos_fin)
        edo.estadoFrasco(client,userdata,msg)
        motorDriver1.reset()
    if msg.payload.decode() == '5':
        mover(carrusel.pos_fin,5,apu)
        carrusel.pos_fin = 5
        actualizar_pos(carrusel.pos_fin)
        edo.estadoFrasco(client,userdata,msg)
        motorDriver1.reset()
    if msg.payload.decode() == '6':
        mover(carrusel.pos_fin,6,apu)
        carrusel.pos_fin = 6
        actualizar_pos(carrusel.pos_fin)
        edo.estadoFrasco(client,userdata,msg)
        motorDriver1.reset()
    if msg.payload.decode() == '7':
        mover(carrusel.pos_fin,7,apu)
        carrusel.pos_fin = 7
        actualizar_pos(carrusel.pos_fin)
        edo.estadoFrasco(client,userdata,msg)
        motorDriver1.reset()
    if msg.payload.decode() == '8':
        mover(carrusel.pos_fin,8,apu)
        carrusel.pos_fin = 8
        actualizar_pos(carrusel.pos_fin)
        edo.estadoFrasco(client,userdata,msg)
        motorDriver1.reset()