import socket
from io import open

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Se declaran los sockets (familia, tipo)
socket_server.bind(('localhost', 8000)) # Establezco la conexión en la máquina local con el puerto 8000
socket_server.listen(5) #Cantidad de peticiones en cola
print("puerto creado")
contador = 0
numero_lineas = 0

while True:
    conexion, direccion = socket_server.accept() # Aceptamos las peticiones
    print("****************************************************\n")
    print("La conexión se ha establecido en el servidor")    
    print(direccion)
    try:        
        resultado = conexion.recv(1024) # Buffer --> se recibe el mensaje del cliente y se almacena en variable        
        resultado = resultado.decode("utf-8") # Convertir tipo bytes a tipo cadena        
    except:
        resultado = ""        

    try:
        with open("datos.txt","r") as leer_texto:
            texto = leer_texto.readlines()
            numero_lineas = len(texto)
    except:
        print("Archivo no encontrado, Esperamos crearlo")
        numero_lineas = 1

    if contador == 5 and numero_lineas == contador:        
        contador = 0        
        if "," not in resultado:            
            for cuenta in texto:
                if resultado+"," in cuenta:
                    bytes_archivo = str.encode(cuenta)
                    conexion.sendall(bytes_archivo) # Enviamos el mensaje mediante la conexión
                    break
    
    elif numero_lineas <= 5 and  contador != numero_lineas:
        contador = 0
        with open("datos.txt","w") as archivo_texto:
                texto = f"{resultado}\n"
                if texto != "\n":
                    archivo_texto.write(texto)
                conexion.sendall(b"Registro Ok truncando")                

    else:    
        with open("datos.txt","a") as archivo_texto:
            texto = f"{resultado}\n"
            archivo_texto.write(texto)
            conexion.sendall(b"Registro Ok agregando")                    
    
    contador += 1
    conexion.close()    