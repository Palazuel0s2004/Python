#Diseña un simulador de atención al cliente que utilice tres colas diferentes:
# Cola Normal: FIFO regular
# Cola VIP: Los clientes VIP tienen prioridad y se atienden antes que los normales (pero entre ellos, FIFO)
# Cola de Reclamos: Los reclamos tienen prioridad sobre todo lo demás
# Reglas de atención:
#1. Siempre atender primero la cola de Reclamos
#2. Si no hay reclamos, atender cola VIP
#3. Si no hay VIP, atender cola Normal
#4. Mostrar después de cada atención el estado de las tres colas
# Debes incluir:
# Especificación completa de cada TDA utilizado
# Invariante para cada implementación
# Código en PSeInt completamente funcional

reclamos = []
vip = []
normal = []

opc = 0

while True:
    print("1. Ingresar Cliente | 2. Atender | 3. Salir");print("");opc = int(input("Opcion: "))

    if opc == 1:
        nombre = input("Nombre del cliente: ");print("");tipo = int(input("Tipo (1.Reclamo | 2.VIP | 3.Normal): "))
        
        if tipo == 1:
            reclamos.append(nombre)
        elif tipo == 2:
            vip.append(nombre)
        elif tipo == 3:
            normal.append(nombre)
        else:
            print("Opcion invalida")
            
        print(f"Estado -> Reclamos: {reclamos} | VIP: {vip} | Normal: {normal}")

    elif opc == 2:
        # Reglas de atencion estructuradas con if/elif :v
        if len(reclamos) > 0:
            print("Atendiendo RECLAMO a:", reclamos.pop(0))
        elif len(vip) > 0:
            print("Atendiendo VIP a:", vip.pop(0))
        elif len(normal) > 0:
            print("Atendiendo NORMAL a:", normal.pop(0))
        else:
            print("No hay clientes esperando")
            
        print(f"Estado Post-Atencion -> Reclamos: {reclamos} | VIP: {vip} | Normal: {normal}")
    elif opc == 3:
        break
    else:
        print("Ponga un numero valido")
