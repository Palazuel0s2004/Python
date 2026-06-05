#Simula la cola de atención al cliente de un banco. Los clientes llegan y toman un turno (se les asigna un número correlativo).
# El cajero atiende a los clientes en orden estricto de llegada.
#Instrucciones:
#1. Crea una cola vacía llamada turnos.
#2. Llegan los clientes: Ana (turno 1), Carlos (turno 2), Beatriz (turno 3).
#Muestra la cola después de cada llegada.
#3. El cajero atiende a un cliente. Muestra a quién atendió y la cola restante.
#4. Llega un nuevo cliente: David (turno 4). Muestra la cola.
#5. El cajero atiende a dos clientes más (uno tras otro). Muestra cada atención y el estado de la cola.

fila_espera = [];cajero1 = "Libre";cajero2 = "Libre"
while True:
    print("\t--- ESTADO DEL BANCO ---")
    if not fila_espera:
        print("Fila: (Vacía)")
    else:
        print("Fila de espera:")
        for turno, nombre in enumerate(fila_espera, start=1):
            print(f"Turno {turno}: {nombre}")
    print(f"Cajero 1: {cajero1} | Cajero 2: {cajero2}")
    print("1. Llegada de cliente | 2. Atender Cajero 1 | 3. Atender Cajero 2 | 4. Salir");opc = input("Seleccione: ")
    if opc == "1":
        nombre = input("Nombre del cliente: ");fila_espera.append(nombre)
    elif opc == "2":
        if len(fila_espera) > 0:
            cajero1 = f"Atendiendo a {fila_espera.pop(0)}"
            print("Fila restante: ", fila_espera)
        else:
            print("No hay nadie en fila.");cajero1 = "Libre"
    elif opc == "3":
        if len(fila_espera) > 0:
            cajero2 = f"Atendiendo a {fila_espera.pop(0)}"
            print("Fila restante: ", fila_espera)
        else:
            print("No hay nadie en fila.");cajero2 = "Libre"
    elif opc == "4": print(fila_espera); break