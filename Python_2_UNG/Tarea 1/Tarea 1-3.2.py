#Implementa el TDA Cola usando un arreglo circular en PSeInt. Debe incluir:
#1. operaciones: encolar, desencolar, ver frente, estaVacia, tamaño
#2. Usar las variables frente, fin y contador como en el ejemplo
#3. El arreglo debe ser circular (usar operador MOD)
#4. Después de cada operación, mostrar:
# Estado actual de la cola
# Valores de frente, fin y contador
# Verificación del invariante

max = 5 #tamaño maximo de contador
cola = [None] * max #Creacion del vector vacio con el tamaño de la variable max
frente = 0 #variable frente
fin = -1 #variable fin, inicia en menos para que la suma (fin + 1) de 0 
contador = 0

def messi():
    #Estado de la invariante, se imprime despues de cada proceso dado
    print("Estado actual de la cola: ");print("")
    print(cola);print("");print("Frente:", frente);print("")
    print("Fin:", fin);print("")
    print("Contador:", contador);print("")
    if 0 <= contador <= max:
        print("Invariante correcto");print("")
    else:
        print("Error en el invariante")

#Ciclo del procedimiento
while True:
    #interfaz
    print("1. Encolar | 2. Desencolar | 3. Ver frente | 4. Esta vacia | 5. Tamaño | 6. Salir");print("");dat = int(input("Ingrese una opcion: "));print("")
    if dat == 1:
        #Si el contador esta igual a max entonces el vector estara lleno
        if contador == max:
            print("Cola llena");print("")
        #Sino se puede cargar un elemento en el vector
        else:
            dato = input("Ingrese elemento: ");print("")
            fin = (fin + 1) % max
            cola[fin] = dato;contador = contador + 1
            print("Elemento encolado");print("")
    #Eliminar elemento del vector
    elif dat == 2:
        #if por si el vector esta vacio
        if contador == 0:
            print("Cola vacia");print("")
        #Si tiene elementos entonces si se puede eliminar
        else:
            eliminado = cola[frente]
            cola[frente] = None
            frente = (frente + 1) % max
            contador = contador - 1
            print("Elemento eliminado:", eliminado);print("")
    #Verificar frente del vector
    elif dat == 3:
        if contador == 0:
            print("Cola vacia");print("")
        else:
            print("Frente:", cola[frente]);print("")
    #Vericiar si la cola esta vacia o tiene elementos
    elif dat == 4:
        if contador == 0:
            print("La cola esta vacia");print("")
        else:
            print("La cola tiene elementos: ", cola);print("")
    #Tamaño de la cola
    elif dat == 5:
        print("Tamaño de la cola:", contador);print("")
    #Salida del programa
    elif dat == 6:
        print("Saliendo...");print("")
        messi()
        break
    #Else si elige un numero aleatorio
    else:
        print("Opcion incorrecta");print("")
    messi()


