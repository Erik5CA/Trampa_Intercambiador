import sensorHall as _49e

def on_message_sensores_Hall(client, userdata, msg):
    client.publish("trampa/sensor/49e/intensidad", _49e.intensity_field())
    print("\nActualizado")