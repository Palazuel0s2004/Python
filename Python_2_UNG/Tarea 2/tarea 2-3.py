#Ejercicio 3: Invertir una Secuencia
#Problema:
#Dada una secuencia de números ingresados por el usuario, muéstralos en orden inverso al
#que fueron ingresados.
#Ejemplo:
#Ingrese números (0 para terminar):
#Ingrese número: 5
#Ingrese número: 10
#Ingrese número: 15
#Ingrese número: 20
#Ingrese número: 0
#Números en orden inverso: 20 15 10 5
#Pregunta: ¿Qué TDA permite invertir fácilmente el orden de los elementos?

vector = []

while True:
    num = int(input("Ingrese un numero (0 para terminar): "));print()
    if num == 0:
        print("Orden Normal: ", vector)
        print("Orden Inverso: ", vector[::-1]) ;print()       
        break
    else:
        vector.append(num)
        print("Orden Normal: ", vector)
        print("Orden Inverso: ", vector[::-1]);print()