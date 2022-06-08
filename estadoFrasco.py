frascos = {'frasco' : ['1','2','3','4','5','6'] , 'estado' : ['lleno','vacio','lleno','vacio','vacio','lleno']}


def estadoFrasco(client, userdata, msg):
    for i in range(0,6):
        if frascos['frasco'][i] == msg.payload.decode():
            client.publish("trampa/frasco/estado", frascos['estado'][i])
            client.publish("trampa/frasco/actual", "Frasco: " + str(i+1))

def estadoFSA(pos,client, userdata, msg):
    for i in range(0,6):
        if frascos['frasco'][i] == str(pos):
            client.publish("trampa/frasco/estado", frascos['estado'][i])
            client.publish("trampa/frasco/actual", "Frasco: " + str(i+1))
