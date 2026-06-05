#Diseña un sistema de turnos para un banco que utilice dos TDAs diferentes:
# Una cola para clientes generales (FIFO)
# Una cola con prioridad para clientes preferenciales (prioridad 1 = preferencialprioridad 2 = general)
# El sistema debe:
# 1. Permitir registrar llegada de clientes (elegir tipo)
# 2. Atender al siguiente cliente (siempre preferenciales primero, luego generales)
# 3. Mostrar el estado de ambas colas
# 4. Mostrar el invariante de cada TDA
# Especificación adicional: Cuando un cliente preferencial es atendido, debe mostrarse "ATENDIENDO PREFERENCIAL: [nombre]

cola_preferencial = [] # Prioridad 1
cola_general = []      # Prioridad 2

def fun(): #Funcion para ver el estado de la Invariante (condicion que debe cumplirse siempre)
    print(f"Cola Preferencial: ", cola_preferencial)
    print("")
    print(f"Cola General: ", cola_general)
    print("")

while True:
    print("1. Llegada Cliente | 2. Atender | 3. Ver Colas | 4. Salir");print("")
    opc = int(input("Opción: "));print("")

    if opc == 1:
        nombre = input("Nombre: ");print("");tipo = int(input("Tipo (1-Preferencial, 2-General): "));print("")
        if tipo == 1:
            cola_preferencial.append(nombre)
        else:
            cola_general.append(nombre)

    elif opc == 2:
        # Lógica de atención: Siempre preferenciales primero
        if len(cola_preferencial) > 0:
            atendido = cola_preferencial.pop(0)
            print(f"ATENDIENDO PREFERENCIAL: {atendido}");print("")
        elif len(cola_general) > 0:
            atendido = cola_general.pop(0)
            print(f"Atendiendo General: {atendido}");print("")
        else:
            print("No hay nadie en espera.");print("")

    elif opc == 3:
        print("VIP:", cola_preferencial);print("");print("Normal:", cola_general);print("")

    elif opc == 4:
        print("Proceso Finalizado, las colas quedan asi: ")
        fun()
        break
    fun()