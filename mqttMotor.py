import motorDriver1
#import motorEmbolo

pasos = 50
tiempo = 0.005

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if msg.payload.decode() == 'front': ##decode() para recibir el string
        motorDriver1.adelante(tiempo,pasos)
        motorDriver1.reset()
    if msg.payload.decode() == 'back':
        motorDriver1.atras(tiempo,pasos)
        motorDriver1.reset() 
    # else:
    #     motorEmbolo.sensorEmbolo()
    #     motorDriver1.reset()