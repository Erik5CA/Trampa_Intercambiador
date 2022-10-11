import RPi.GPIO as GPIO

pin_SSR1 = 21
pin_SSR2 = 20

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin_SSR1, GPIO.OUT)
GPIO.setup(pin_SSR2, GPIO.OUT)

# Funcion para activar o desactivar el SSR
def SSR_operation(pin,opt):
    if opt == 'on':
        GPIO.output(pin, GPIO.HIGH)
    elif opt == 'off':
        GPIO.output(pin, GPIO.LOW)
    else: print('Error 404')

# Funcion que lee el mensaje publicado en el topic boton y actua sobre los SSR
def on_message_SSR(client, userdata, msg):
    message = msg.payload.decode()
    if message == 'on1':
        SSR_operation(pin_SSR1,'on')
    elif message == 'off1':
        SSR_operation(pin_SSR1,'off')
    elif message == 'on2':
        SSR_operation(pin_SSR2,'on')
    elif message == 'off2':
        SSR_operation(pin_SSR2,'off')
    else:   print('\nEsperando...')

if __name__ == '__main__':
    SSR_operation(pin_SSR1,'on')
    SSR_operation(pin_SSR2,'on')