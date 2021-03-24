import socket

socket_client = socket.socket()
socket_client.connect(('localhost', 8000))

socket_client.sendall(b"Mensaje enviado del cliente")
resultado = socket_client.recv(1024) # Buffer

print(resultado)
socket_client.close()