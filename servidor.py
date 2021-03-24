import socket

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind(('localhost', 8000)) # Establezco la conexión en la máquina local con el puerto 8000
socket_server.listen(5) #Cantidad de peticiones en cola


while True:
    conexion, direccion = socket_server.accept() # Aceptamos las peticiones
    print("La conexión se ha establecido en el servidor")
    print(direccion)
    conexion.sendall(b"Mensaje enviado desde el servidor")

    resultado = conexion.recv(1024) # Buffer
    print(resultado)

    conexion.close()
    print("servidor cerrado")
