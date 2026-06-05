#Ejercicio 10: Atención en una Tienda
#Problema:
#En una pequeña tienda, los clientes llegan y forman una sola fila. Hay dos cajeros que atienden. Cuando un cajero se desocupa, atiende al cliente que ha estado esperando más tiempo.
#El programa debe:
#· Registrar llegada de cliente (nombre)
#· Atender cliente con cajero 1 (si está libre)
#· Atender cliente con cajero 2 (si está libre)
#· Mostrar fila de espera
# Mostrar cajeros ocupados/libres
#Ejemplo: ``` Llega: Ana
#Llega: Bruno
#Llega: Carlos
#Cajero 1 libre → Atiende a Ana
#Cajero 2 libre → Atiende a Bruno
#Fila de espera: Carlos ```
#Pregunta: Aunque hay dos cajeros, ¿qué TDA sigue siendo útil para la fila de espera? ¿Por qué?

fila_espera = [];cajero1 = "Libre";cajero2 = "Libre"
while True:
    print(f"Fila: {fila_espera}");print(f"Cajero 1: {cajero1} | Cajero 2: {cajero2}")
    print("1. Llegada de cliente | 2. Atender Cajero 1 | 3. Atender Cajero 2 | 4. Salir");opc = input("Seleccione: ")
    if opc == "1":
        nombre = input("Nombre del cliente: ");fila_espera.append(nombre)
    elif opc == "2":
        if len(fila_espera) > 0:
            cajero1 = f"Atendiendo a {fila_espera.pop(0)}"
        else:
            print("No hay nadie en fila.");cajero1 = "Libre"
    elif opc == "3":
        if len(fila_espera) > 0:
            cajero2 = f"Atendiendo a {fila_espera.pop(0)}"
        else:
            print("No hay nadie en fila.");cajero2 = "Libre"
    elif opc == "4": break
