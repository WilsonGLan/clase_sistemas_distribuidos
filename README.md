# clase_sistemas_distribuidos

Integrantes:

WILSON GUTIERREZ LANCHEROS-1621024374
ALEXANDER CACAIS UMBARILA-100233393
LUZ ANGELA RAYO PALENCIA-1921980146
MARIA PAULA HOYOS ORTIZ - 1810010181






Este repositorio se creó para la clase de sistemas distribuidos dictado en la universidad politecnico grancolombiano


Proceda a desarrollar una aplicación cliente-servidor para un taller transaccional
utilizando sockets, así:
a. Monte el compilador de Java. Cree un archivo llamado datos.txt usando la utilidad
manejo de archivos en Java.
b. Elabore un programa socket server que recoja las peticiones de un programa cliente.
c. Elabore un programa socket cliente que solicite capture por consola, el número de
cuenta y un valor en tipo de dato String, arme un mensaje por concatenación de
cadenas de caracteres en la variable mensaje y envíela al programa socket servidor,
el cual debe recibir el mensaje, extraer las subcadenas cuenta y valor y convertirlas
a valores numéricos, así podrá ingresar al archivo y grabar los datos separados por
comas. Si pudo grabar, el socket server debe enviar un mensaje al cliente diciendo:
Registro grabado OK, o un NO-OK si la operación falló. El cliente recibe el mensaje,
publica el resultado y cierra la transacción, pero el socket server queda abierto
esperando por si otro cliente solicita un servicio.
d. Repita el proceso hasta grabar 5 registros diferentes en los campos (cuenta y valor).
• Ejemplo: 245812345678,100000, (el valor unas veces puede ser 100000 o
10000000).
e. Después el socket cliente hace una consulta, como lo hace un cajero automático,
dando el número de cuenta y el servidor devuelve el valor si encontró la cuenta.
