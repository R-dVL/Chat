import socket
import sys
from datetime import datetime

# Función para escribir mensajes en el log
def Log_Write(timestamp, usr, txt):
    with open("../data/log.txt", 'a') as log:
        try:
            log.write("\n" + str(timestamp) + " " + str(usr) + ": " + str(txt))
        except:
            raise Exception("Error de escritura en el log.")
        finally:
            log.close()

# Cliente
def client():
    # Crea un socket TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Establece una conexión con el servidor
    host = socket.gethostname()
    port = int(sys.argv[1])    # Puerto que está usando el servidor
    client_socket.connect((host, port))

    print(f'Conectado a {host}:{port}')

    # Envía mensajes al servidor y recibe mensajes de otros clientes a través del servidor
    while True:
        message = input('Ingrese su mensaje: ')
        client_socket.send(message.encode('utf-8'))
        data = client_socket.recv(1024).decode('utf-8')
        print(f'Recibido: {data}')

    # Cierra la conexión
    client_socket.close()
        
if __name__ == "__main__":
    client()
