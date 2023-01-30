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
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Obtiene el nombre de host local
    host = socket.gethostname()
    port = int(sys.argv[1])    # Puerto que está usando el servidor

    # Enlaza el socket a una dirección y un puerto específicos
    server_socket.bind((host, port))

    # Escucha por nuevas conexiones
    server_socket.listen(5)

    print(f'Servidor escuchando en {host}:{port} ...')

    # Una lista de clientes conectados
    clients = []

    while True:
        # Acepta una nueva conexión
        client_socket, client_address = server_socket.accept()
        print(f'Conexión establecida desde {client_address[0]}:{client_address[1]}')
        clients.append(client_socket)

        # Recibe mensajes del cliente y los transmite a todos los demás clientes conectados
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f'Recibido desde {client_address[0]}:{client_address[1]}: {message}')
            for client in clients:
                client.send(message.encode('utf-8'))

    # Cierra la conexión del cliente
    client_socket.close()
        
if __name__ == "__main__":
    client()
