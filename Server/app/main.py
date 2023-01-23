import socket
import sys
from datetime import datetime

IP = str(sys.argv[1])    # IP usada por el server
PORT = int(sys.argv[2])    # Puerto que usará el server

# Función para escribir mensajes en el log
def Log_Write(timestamp, usr, txt):
    with open("../data/log.txt", 'a') as log:
        try:
            log.write("\n" + str(timestamp) + " " + str(usr) + ": " + str(txt))
        except:
            raise Exception("Error de escritura en el log.")
        finally:
            log.close()
    
# Servidor
def server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # Crear Socket
    try:
        server.bind((IP, PORT))    # Alojar servidor en IP y Puerto introducidos
        server.listen()    # Esperar conexión
        print(f'Esperando conexiones en: {IP}:{PORT}...')
        client, addr = server.accept()    # Aceptar conexión entrante
        with client:
            print(f"{addr} se ha conectado.")
            Log_Write(datetime.now().strftime("%D %H:%M:%S"), addr, "Nueva conexión")

            while True:
                # Datos recibidos del cliente
                data = client.recv(1024)
                # Si recibe "exit" anota la desconexión del cliente
                if data.decode() == "exit":
                    Log_Write(datetime.now().strftime("%D %H:%M:%S"), addr, "Desconexion.")
                    break
                # Muestra por consola y anota el texto recibido
                print(f"{addr} dice: {data.decode()}")
                Log_Write(datetime.now().strftime("%D %H:%M:%S"), addr, data.decode())

                # Respuesta al cliente
                data = input(">> ")
                # Si el usuario introduce "exit" se cerrará el servidor
                if data == "exit":
                    client.sendall(data.encode())
                    break
                # Anota el texto enviado al client en el log
                Log_Write(datetime.now().strftime("%D %H:%M:%S"), "Server", data)
                client.sendall(data.encode())
    except:
        Log_Write(datetime.now().strftime("%D %H:%M:%S"), "Server", "Fallo en el servidor.")
        raise Exception("Fallo en el servidor.")
    
    finally:
        Log_Write(datetime.now().strftime("%D %H:%M:%S"), addr, "Fin de la conexion.")
        print("Fin de la conexion.")
            
if __name__ == "__main__":
    server()