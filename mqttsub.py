import paho.mqtt.client as mqtt
import carrusel as car
import RPi.GPIO as GPIO
import mqttSSR as SSR                   # Este archivo ejecuta las acciones en el SSR

import mqttSensores as mqtts            # Este archivo contiene la configuracion de todos los sensores para mqtt

import mqttMotor as MOTOR
import motorDriver2 as M2

# broker = "132.248.51.251"
broker = "test.mosquitto.org"

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("trampa/#") 

try:
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = MOTOR.on_message_MOTOR

    client.connect(broker, 1883, 60)
    client.message_callback_add("trampa/control/ssr", SSR.on_message_SSR)

    client.message_callback_add("trampa/boton/ssr", SSR.on_message_SSR)
    
    client.message_callback_add("trampa/boton/posicion", MOTOR.on_message_MOTOR)
    
    client.message_callback_add("trampa/sensor/dato/dht11", mqtts.on_message_sensores_dht11)
    client.message_callback_add("trampa/sensor/dato/bmp", mqtts.on_message_sensores_bmp)
    client.message_callback_add("trampa/sensor/dato/49e", mqtts.on_message_sensores_Hall)
    client.message_callback_add("trampa/sensor/dato/lm", mqtts.on_message_sensores_LM)
    
    client.loop_forever()
    
except KeyboardInterrupt:
    with open("posicion.txt", "wt") as f:
        f.writelines(f"{car.pos_ini}\n{car.pos_fin}")
    M2.reset()
    GPIO.cleanup()