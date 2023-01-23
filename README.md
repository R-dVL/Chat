# Chat
Terminal Client-Server Chat built in Python with chat log.

## Description
The chat is divided in two scripts, **Server** and **Client**. Both of them needs two arguments when calling the main.py, IP and Port.

>$ python3 main.py 127.0.0.1 8000

Server will start to listen to connections in this IP and Port, while Client will try to start a connection in the IP and Port introduced.

Once the connection is stablished, they will alternate to send messages:

>Client -> Server -> Client...
___
    $ Client: Hi!
    $ >...
___
    $ You: Hi!
    $ Server: Sup.
    $ >...
___

Type exit in order to finish the server or client connection.