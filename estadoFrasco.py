
frascos = {'frasco' : ['1','2','3','4','5','6','7','8'] , 'estado' : ['lleno','vacio','lleno','vacio','vacio','lleno','vacio','vacio']}

def estadoFrasco(client, userdata, msg):
    for i in range(0,8):
        if frascos['frasco'][i] == msg.payload.decode():
            client.publish("trampa/frasco/estado", frascos['estado'][i])
            client.publish("trampa/frasco/actual", f"Frasco: {i+1}")

def estadoFSA(pos,client, userdata, msg):
    for i in range(0,8):
        if frascos['frasco'][i] == str(pos):
            client.publish("trampa/frasco/estado", frascos['estado'][i])
            client.publish("trampa/frasco/actual", f"Frasco: {i+1}")
