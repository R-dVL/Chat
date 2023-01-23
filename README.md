# Cliente
Script para iniciar cliente que conectará con un servidor para intercambiar mensajes.

Para ello he usado:
- "socket" para crear las conexiones del servidor y el cliente. 
- "sys" para introducir los argumentos IP y Puerto al llamar al programa (he estado usando el localhost y el puerto 8000 para las pruebas).

## Log
Consta con un log en el que se guardará desde la conversación hasta las conexiones y errores.

He usado datetime para el timestamp y un context manager para abrir y cerrar el archivo "log.txt".

(se podría haber depurado más el formato y los errores recogidos pero no creo que fuera la finalidad).