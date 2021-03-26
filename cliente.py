import socket

for _ in range(5):
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_client.connect(('localhost', 8000))
    datos_cuenta = input("Por favor ingresar la cuenta: ")
    datos_monto = input("Por favor ingresar el valor: ")
    datos_ingresar = datos_cuenta+","+datos_monto
    print(datos_ingresar)
    bytes_datos = str.encode(datos_ingresar) #Se pasa a bytes
    print(bytes_datos)
    socket_client.sendall(bytes_datos)
    resultado = socket_client.recv(1024) # Buffer
    socket_client.close()
    print(resultado)
    




