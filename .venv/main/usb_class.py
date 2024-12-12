import serial
import time
import serial.tools.list_ports

comando = 'AT'
respuesta_esperada = 'OK'
tension = 'TSNACTT'

class USB:

    def __init__(self):
        self.COM = ''
        self.conecttion = False

    def list_port(self):
        puertos = serial.tools.list_ports.comports()
        return [puerto.device for puerto in puertos]

    def find_port(self):
        puertos = self.list_port()
        if len(puertos) > 0:
            print("Cantidad de Puertos: " + str(len(puertos)))
            for puerto in puertos:
                if self.comunication(puerto, comando, respuesta_esperada):
                    print("Comunicacion Exitosa con: " + puerto)
                    self.conecttion = True
                    self.COM = puerto
                    return puerto
            return 'No se encontró un puerto con comunicación exitosa.'
        else:
            return 'Sin Puertos Disponibles.'

    def comunication(self, puerto, comando, respuesta_esperada):
            try:
                ser = serial.Serial(port=puerto, baudrate=9600, timeout=2)
                ser.write(comando.encode())
                time.sleep(2)
                respuesta = ser.read(ser.in_waiting).decode()
                ser.close()
                return respuesta_esperada in respuesta
            except (serial.SerialException, OSError) as e:
                print(f'Error en el puerto {puerto}: {e}')
                return False

    def sendData(self, puerto):
        if self.conecttion == True:
            try:
                ser = serial.Serial(port=puerto, baudrate=9600, timeout=2)
                print(f'Comunicandome con: {puerto}')
                ser.write(tension.encode())
                time.sleep(2)
                respuesta = ser.read(ser.in_waiting).decode()
                ser.close()
                return respuesta
            except (serial.SerialException, OSError) as e:
                return f'Error en el puerto {puerto}: {e}'
        else:
            return 'Establecer Conexion Primero'

    def getCOM(self):
        return self.COM
