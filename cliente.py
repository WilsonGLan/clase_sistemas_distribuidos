import socket

for entrada in range(6):
    resultado = ""
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_client.connect(('localhost', 8000))
    if entrada <= 4:
        datos_cuenta = input("Por favor ingresar la cuenta: ")
        datos_monto = input("Por favor ingresar el valor: ")
        datos_ingresar = datos_cuenta+","+datos_monto
        bytes_datos = str.encode(datos_ingresar) #Se pasa a bytes
        socket_client.sendall(bytes_datos)
        resultado = socket_client.recv(1024) # Buffer
        resultado = resultado.decode("utf-8")
        print(resultado)
    
    
    """ Se reciben datos del servidor """
    if entrada == 5:
        print("=========================Solicitando datos de servidor========================")
        datos_ingresar = input("Ingresar la cuenta que desea validar: ")
        bytes_datos = str.encode(datos_ingresar)
        socket_client.sendall(bytes_datos)
        resultado = socket_client.recv(1024) # Buffer
        resultado = resultado.decode("utf-8")
        datos_obtenidos = resultado.split(",")        
        print(f"Cuenta: {datos_obtenidos[0]} - Valor: {datos_obtenidos[1]} ")
    
    socket_client.close()
    




