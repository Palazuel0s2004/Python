#Ejercicio 13: Simulador de Estacionamiento
#Problema:
#Un estacionamiento tiene una entrada y una salida en el mismo lugar (una sola vía). Los autos entran y se estacionan en fila. Cuando un auto del medio quiere salir, los autos que están detrás de él deben moverse temporalmente a una calle auxiliar (que funciona como pila) para dejar salir al auto, y luego regresar en orden.
#Reglas:
#· Los autos llegan y se estacionan en orden de llegada (cola)
#· Para sacar un auto, los que están detrás de él se mueven a una pila auxiliar
#· Luego, los autos de la pila regresan al estacionamiento en el mismo orden
#Ejemplo:
#``` Estacionamiento: [A, B, C, D]  (A es el primero en salir normalmente)
#Quiere salir: C
#1. Mover autos detrás de C a pila auxiliar:
#   - D se mueve a pila
#   Estacionamiento: [A, B, C]
#   Pila auxiliar: [D]
#2. Sale C
#   Estacionamiento: [A, B]
#3. Regresan autos de la pila:
#   - D regresa al estacionamiento
#   Estacionamiento: [A, B, D] ```
#Implementa este simulador permitiendo:
#· Llegada de autos
#· Salida de auto específico
#· Mostrar estado del estacionamiento y pila auxiliar


A = """         ______
         /|_||_`.__
        (   _ A  _ _\\
        =`-(_)--(_)-'  """
B = """         ______
         /|_||_`.__
        (   _ B  _ _\\
        =`-(_)--(_)-'  """
C = """         ______
         /|_||_`.__
        (   _ C  _ _\\
        =`-(_)--(_)-'  """
D = """         ______
         /|_||_`.__
        (   _ D  _ _\\
        =`-(_)--(_)-'  """
# El estacionamiento contiene los dibujos
estacionamiento = [A, B, C, D]
def sacar_auto(auto):
    global estacionamiento
    pila_auxiliar = []
    # Busca el dibujo en la lista
    if auto not in estacionamiento:
        print("Ese auto no está en el estacionamiento.")
        return
    # 1. Movimiento a la PILA auxiliar (LIFO)
    # Mientras el último auto de la fila no sea el que quiero sacar
    while estacionamiento[-1] != auto:
        estorbo = estacionamiento.pop()
        pila_auxiliar.append(estorbo)
        print(">>> Moviendo este auto a la calle auxiliar para abrir paso:")
        print(estorbo)
    # 2. Saca el auto deseado (El que el usuario eligió)
    fuera = estacionamiento.pop()
    print("\n*********************************")
    print("¡EL SIGUIENTE AUTO ESTÁ SALIENDO!")
    print(fuera)
    print("*********************************\n")
    # 3. Regresa los autos de la PILA al estacionamiento
    while len(pila_auxiliar) > 0:
        regresando = pila_auxiliar.pop()
        estacionamiento.append(regresando)
        print(">>> Regresando este auto al estacionamiento:")
        print(regresando)
print("--- BIENVENIDO AL ESTACIONAMIENTO ---")
print(f"Autos estacionados actualmente: {len(estacionamiento)}")
print(f"1. Sacar Auto A\n{A}")
print(f"2. Sacar Auto B\n{B}")
print(f"3. Sacar Auto C\n{C}")
print(f"4. Sacar Auto D\n{D}")
try:
    opcion = int(input("Ingrese el número del auto que desea retirar (1-4): "))
    #mapeo de la variable
    mapeo = {1: A, 2: B, 3: C, 4: D}
    seleccion = mapeo.get(opcion)
    if seleccion:
        sacar_auto(seleccion)
        print("Estado final del estacionamiento (en fila):")
        for auto in estacionamiento:
            print(auto)
    else:
        print("Opción no válida.")
except ValueError:
    print("Por favor, ingrese un número válido.")