#Crea un programa que implemente el mismo TDA Pila de dos formas diferentes:
#1. Versión A: Pila con arreglo (tope como índice)
#2. Versión B: Pila con arreglo pero usando "fondo" y "cima" (los elementos se insertan al principio
#del arreglo y se desplazan)
#El programa debe permitir al usuario elegir qué implementación usar y probar las mismas operaciones.
#Pregunta para responder: ¿Qué ventajas y desventajas tiene cada implementación?

max_tam = 5
pila_a = [None] * max_tam
tope_a = 0
pila_b = [None] * max_tam
tope_b = 0

opc = 0
while True:
    print("--- COMPARATIVA DE PILAS ---");print("")
    print("1. Apilar en Pila A (Al final)  | 2. Desapilar de Pila A  | 3. Apilar en Pila B (Al inicio)\n" \
    "4. Desapilar de Pila B | 5. Salir");print("")
    opc = int(input("Opción: "));print("")

    # Implementacion A: Rápida y directa
    if opc == 1:
        if tope_a < max_tam:
            pila_a[tope_a] = input("Elemento para Pila A: ");print("")
            tope_a += 1
            print("Apilado al final. Pila A:", pila_a);print("")
        else:
            print("Pila A llena");print("")
    elif opc == 2:
        if tope_a > 0:
            tope_a -= 1
            (f"Desapilado: {pila_a[tope_a]}");print("")
            pila_a[tope_a] = None
            print("Pila A:", pila_a);print("")
        else:
            print("Pila A vacía");print("")
# Implementacion B: Lenta (Requiere mover todo)
    elif opc == 3:
        if tope_b < max_tam:
            dato = input("Elemento para Pila B: ");print("")
            # Problema: mueve todos los elementos un lugar a la derecha
            for i in range(tope_b, 0, -1):
                pila_b[i] = pila_b[i-1]
            pila_b[0] = dato
            tope_b += 1
            print("Apilado al inicio (desplazando). Pila B:", pila_b);print("")
        else:
            print("Pila B llena");print("")

    elif opc == 4:
        if tope_b > 0:
            print(f"Desapilado del inicio: {pila_b[0]}");print("")
            # Problema: mueve todos los elementos un lugar a la izquierda para tapar el hueco
            for i in range(0, tope_b - 1):
                pila_b[i] = pila_b[i+1]
            pila_b[tope_b-1] = None
            tope_b -= 1
            print("Pila B:", pila_b);print("")
        else:
            print("Pila B vacía");print("")

    elif opc == 5:
        print("La pila A queda asi: ", pila_a);print("")
        print("La pila B queda asi: ", pila_b);print("")
        break
    else:
        print("Opcion incorrecta");print("")