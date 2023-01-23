import socket
import sys
from datetime import datetime

IP = str(sys.argv[1])    # IP en la que se encuentra el servidor
PORT = int(sys.argv[2])    # Puerto que está usando el servidor

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
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # Crear socket para la conexión
    try:
        server.connect((IP, PORT))    # Realizar conexión
        Log_Write(datetime.now().strftime("%D %H:%M:%S"), "Client", "Conexión con servidor establecida.")
        while True:
            # Mensaje a servidor
            message = input(">> ")
            # Si el mensaje introducido es "exit" se desconecta el cliente
            if message == "exit":
                server.sendall(message.encode())
                break
            Log_Write(datetime.now().strftime("%D %H:%M:%S"), "Client", message)
            server.sendall(message.encode())

            # Respuesta del servidor
            data = server.recv(1024)
            print("Server: " + data.decode())
            Log_Write(datetime.now().strftime("%D %H:%M:%S"), "Server", data.decode())

    except:
        Log_Write(datetime.now().strftime("%D %H:%M:%S"), "Client", "Error de conexion.")
        raise Exception("Error de conexion.")

    finally:
        print("Fin de la conexion.")
        Log_Write(datetime.now().strftime("%D %H:%M:%S"), "Client", "Fin de la conexion.")
        
if __name__ == "__main__":
    client()