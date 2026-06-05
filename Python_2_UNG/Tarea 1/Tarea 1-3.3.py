#Implementa el TDA Lista en PSeInt con las siguientes operaciones:
#1. Insertar al final
#2. Insertar en posición específica (validar posición)
#3. Eliminar por posición
#4. Obtener elemento por posición
#5. Mostrar lista completa
#6. Verificar invariante (tamaño entre 0 y MAX)
#Requisito especial: Después de cada inserción o eliminación, muestra el proceso de
# desplazamiento de elementos

max_tam = 5
lista = [None] * max_tam
contador = 0

def messi():
    #Estado de la invariante, se imprime despues de cada proceso dado
    print(f"INVARIANTE: Contador={contador} | 0 <= {contador} <= {max_tam}");print("")
    if 0 <= contador <= max_tam:
        print("Invariante OK");print("")
    else:
        print("ERROR: Invariante roto");print("")

while True:
    print(f"LISTA (Elementos: {contador}/{max_tam})");print("")
    print("1. Insertar al final | 2. Insertar en posicion | " \
    "3. Eliminar por posicion | 4. Mostrar | 5. Salir");print("")
    opc = int(input("Opción: "));print("")

    if opc == 1: # Insertar al final
        if contador < max_tam:
            dato = input("Elemento: ");print("")
            lista[contador] = dato;contador += 1
            print("Agregado al final.");print("")
        else:
            print("Lista llena.");print("")
# Insertar en posición específica
    elif opc == 2: 
        pos = int(input(f"Posición (0 a {contador}): "));print("")
        if 0 <= pos <= contador and contador < max_tam:
            dato = input("Elemento: ");print("")
            # Desplazamiento, corre a todos los elementos a la derecha
            for i in range(contador, pos, -1):
                lista[i] = lista[i-1];print("")
                print(f"Desplazando {lista[i]} a la derecha...");print("")
            lista[pos] = dato;contador += 1
        else:
            print("Posición inválida o lista llena.");print("")
# Eliminar por posición
    elif opc == 3: 
        pos = int(input(f"Posición a eliminar (0 a {contador-1}): "));print("")
        if 0 <= pos < contador:
            print(f"Eliminando: {lista[pos]}");print("")
            # Desplazamiento, corre a todos los elementos a la izquierda
            for i in range(pos, contador - 1):
                lista[i] = lista[i+1]
                print(f"Desplazando {lista[i]} a la izquierda...");print("")
            lista[contador-1] = None;contador -= 1
        else:
            print("Posición vacía.");print("")

    elif opc == 4:
        print("Lista actual:", lista);print("")

    elif opc == 5:
        messi()
        break
    else:
        print("Opcion incorrecta");print("")
    messi()    