#Ejercicio 11: Validar Secuencia de Entrada/Salida
#Problema:
#En un almacén, los paquetes llegan en un camión y se apilan (uno encima de otro). Luego, para despacharlos, se deben sacar en orden inverso al que llegaron (el último en llegar es el primero en salir). Sin embargo, antes de despachar, algunos paquetes se revisan y se pasan a una cola de control de calidad.
#Simula este proceso donde:
#· Llegan paquetes a la pila del camión
#· Se revisan paquetes: se sacan de la pila y se pasan a la cola de calidad
#· Se despachan paquetes: se sacan de la cola de calidad (en orden FIFO)
#· Se muestran ambas estructuras
#Ejemplo:
#``` Llega paquete: A
#Llega paquete: B
#Llega paquete: C
#Pila: C, B, A (C es la cima)
#Revisando paquete: C (pasa a calidad)
#Pila: B, A
#Cola calidad: C
#Revisando paquete: B (pasa a calidad)
#Pila: A
#Cola calidad: C, B
#Despachando paquete: C (sale de calidad)
#ola calidad: B ```
#Pregunta: ¿Por qué en este problema necesitamos TANTO una pila como una cola?

pila_camion = [];cola_calidad = []
while True:
    print(f"Pila Camión: {pila_camion} | Cola Calidad: {cola_calidad}");print("1. Llega paquete | 2. Pasar a Calidad | 3. Despachar | 4. Salir")
    opc = input("Seleccione: ")
    if opc == "1":
        pkg = input("ID Paquete: ");pila_camion.append(pkg) # Se apila
    elif opc == "2":
        if len(pila_camion)>0:
            paquete = pila_camion.pop() # Sale el último que llegó (cima)
            cola_calidad.append(paquete) # Entra a la fila
            print(f"Revisando: {paquete}")
        else:
            print("No hay elementos en la pila")
    elif opc == "3":
        if cola_calidad:
            print(f"Despachando: {cola_calidad.pop(0)}") # Sale el primero de la fila
    elif opc == "4": break