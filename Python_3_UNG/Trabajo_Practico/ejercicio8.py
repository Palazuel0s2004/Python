#8. Tabla de Multiplicar con for
#• Solicitar al usuario un número entero comprendido entre 1 y 20.
#• Utilizando un ciclo for, mostrar su tabla de multiplicar desde 1 hasta 12.
#Al finalizar, el programa deberá:
#• Mostrar la suma de todos los resultados obtenidos.
#• Indicar cuántos resultados son pares.
#• No utilizar listas, arreglos ni funciones avanzadas.

#While para el numero que ingresara el usuario
while True:
    try:
        num = int(input("\nIngrese el numero (Entre 1 y 20): "))
        if 1<=num<=20:
            break
        else:
            print("Ingrese un numero valido (Entre 1 y 20)")
    except ValueError:
        print("Error: Ingrese un número.")

num_par = 0 #Variable para numero par
suma_num = 0 #Variable para almacenar las sumas

print(f"\n\tTABLA DEL MULTIPLICAR DEL {num}")
for i in range(1,12+1):
    multiplicacion = num*i
    print(f"{num} x {i} =",multiplicacion)
    if multiplicacion%2 ==0:
        num_par +=1
    suma_num += multiplicacion
#Prints finales
print(f"La suma de los numeros obtenidos es {suma_num}")
print(f"La cantidad de resultados pares es de {num_par}")

"""Mediante un ciclo for del 1 al 12 el programa muestra la tabla de multiplicar de un número entre 1 y 20 y sin 
utilizar listas ni arreglos calcula de forma directa acumulada la suma total de los productos obtenidos
y contabiliza los resultados pares"""