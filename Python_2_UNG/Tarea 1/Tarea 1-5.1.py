#Crea un programa que implemente una biblioteca de TDAs con menú principal que permita:
#1. Trabajar con una PILA (menú propio)
#2. Trabajar con una COLA (menú propio)
#3. Trabajar con una LISTA (menú propio)
#. Comparar rendimiento (contar operaciones)
#Requisitos adicionales:
# Cada TDA debe tener su propia especificación comentada al inicio
# Después de cada operación, mostrar el invariante
# Llevar un contador de cuántas operaciones se han realizado en cada TDA
# Permitir "resetear" cada TDA a su estado inicial

max_tam = 5
pila = []
ops_pila = 0
cola = [None] * max_tam
frente = 0
fin = -1
cont_cola = 0
ops_cola = 0
lista = []
ops_lista = 0

while True:
    print("--- MENU PRINCIPAL ---");print("")
    print("1. Pila | 2. Cola Circular | 3. Lista | 4. Rendimiento | 5. Salir")
    opc = int(input("Seleccione: "));print("")

    if opc == 1:
        # Operaciones Pila
        acc = int(input("1. Apilar | 2. Desapilar | 3. Reset: "));print("")

        #Apilar elementos
        if acc == 1 and len(pila) < max_tam:
            pila.append(input("Elemento: "));print("")
            ops_pila += 1 #Contador de operaciones

        #Desapilar elementos
        elif acc == 2 and len(pila) > 0:
            print("Sale:", pila.pop());print("")
            ops_pila += 1 #Contador de operaciones

        #Reset de elementos y operaciones
        elif acc == 3:
            pila = []
            ops_pila = 0
            print("Pila reseteada");print("")
        print("Pila actual:", pila);print("")

        # INVARIANTE DE LA PILA
        invariante_pila = 0 <= len(pila) <= max_tam
        print(f"INVARIANTE: 0 <= {len(pila)} <= {max_tam} -> {invariante_pila}")
        if not invariante_pila: print("ERROR: Invariante roto")

    elif opc == 2:
        # Operaciones Cola 
        acc = int(input("1. Encolar | 2. Desencolar | 3. Reset: "));print("")

        #Encolar datos
        if acc == 1 and cont_cola < max_tam:
            fin = (fin + 1) % max_tam #Verifica si hay espacio en la cola
            cola[fin] = input("Elemento: ");print("") 
            cont_cola += 1 #COntador de la cola
            ops_cola += 1 #Contador de operaciones

        #Desencola datos
        elif acc == 2 and cont_cola > 0:
            print("Sale:", cola[frente]);print("")
            cola[frente] = None #Devuelve un espacio a la cola
            frente = (frente + 1) % max_tam;print("")
            cont_cola -= 1 #Resta el contador de la cola
            ops_cola += 1 #Contador de operaciones

        #Resetea la cola
        elif acc == 3:
            cola = [None] * max_tam #Hace que la cola vuelva a estar vacia
            frente = 0
            fin = -1 
            cont_cola = 0
            ops_cola = 0

        # INVARIANTE DE LA COLA
        print("Cola actual:", cola, "Contador:", cont_cola)
        print(f"Frente: {frente} | Fin: {fin}")
        condicion_cont = 0 <= cont_cola <= max_tam
        condicion_indices = frente < max_tam and fin < max_tam
        invariante_cola = condicion_cont and condicion_indices
        print(f"INVARIANTE: (Contador={cont_cola} y Punteros OK) -> {invariante_cola}")
        if not invariante_cola: print("ERROR: Invariante roto")

    elif opc == 3:
        # Operaciones Lista
        acc = int(input("1. Insertar | 2. Sacar | 3. Reset: "))

        #Insertar elemento en Lista
        if acc == 1 and len(lista) < max_tam:
            lista.append(input("Elemento: "))
            ops_lista += 1 #Contador de operaciones
        
        #Saca elemento de la Lista
        elif acc == 2 and len(lista) > 0:
            print("Sale:", lista.pop(0))
            ops_lista += 1 #Contador de operaciones
        
        #Resetea la lista
        elif acc == 3:
            lista = []; ops_lista = 0
        print("Lista actual:", lista)
        # INVARIANTE DE LA LISTA
        invariante_lista = 0 <= len(lista) <= max_tam
        print(f"INVARIANTE: 0 <= {len(lista)} <= {max_tam} -> {invariante_lista}")
        if not invariante_lista: print("ERROR: Invariante roto")

    #Rendimiento del programa
    elif opc == 4:
        print("RENDIMIENTO");print("");print(f"Operaciones Pila: {ops_pila}");print("")
        print(f"Operaciones Cola: {ops_cola}");print("")
        print(f"Operaciones Lista: {ops_lista}");print("")

    #Fin del programa
    elif opc == 5:
        break
    else:
        print("ERROR. Ingrese un numero del 1 al 5");print("")