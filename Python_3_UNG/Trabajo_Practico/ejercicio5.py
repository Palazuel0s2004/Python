#5. Clasificación de una puntuación
#Solicitar una puntuación numérica comprendida entre 0 y 100.
#Clasificarla de acuerdo con los siguientes rangos:
#• De 0 a 20: Nivel inicial.
#• De 21 a 40: Nivel básico.
#• De 41 a 60: Nivel intermedio.
#• De 61 a 80: Nivel avanzado.
#• De 81 a 100: Nivel excelente.
#Además, el programa deberá:
#• Indicar si la puntuación es par o impar.
#• Mostrar cuántos puntos le faltan para llegar al siguiente nivel.
#• Informar cuando el valor ingresado sea menor que 0 o mayor que 100.
#• Si la puntuación pertenece al nivel excelente, deberá mostrar un mensaje especial de
#felicitación con el nombre del estudiante. (Usar tu nombre y apellido en esta prueba)

#While para el nombre
while True:
        nombre = input("\nIngresa tu nombre: ").strip()
        #Elimina espacios en blanco al inicio y al final del nombre
        if nombre.replace(" ", "").isalpha() and len(nombre) > 0:
            print(f"¡Nombre válido!")
            break
        else:
            print("Error: Ingrese un nombre válido.")

#Funcion while para ingresar la puntuacion de forma correcta
while True:
    try:
        puntuacion = int(input("\nIngrese la puntuacion (entre 0 a 100): "))
        if 0> puntuacion:
            print("La puntuacion es menor a 0, por favor ingrese una puntuacion mayor o igual a 0")
        elif 100<puntuacion:
            print("La puntuacion es mayor a 100, por favor ingrese una puntuacion menor o igual a 100")    
        else:
            break
    except ValueError:
        print("Error: Ingrese un número.")

#if y elif para las puntuaciones
if 0<= puntuacion <= 20:
    print("Esta clasificado en el nivel inicial")
    print(f"Para llegar a la siguiente puntuación te faltan {21-puntuacion} puntos")
elif 21<= puntuacion <= 40:
    print("Esta clasificado en el nivel basico")
    print(f"Para llegar a la siguiente puntuación te faltan {41-puntuacion} puntos")
elif 41<= puntuacion <= 60:
    print("Esta clasificado en el nivel intermedio")
    print(f"Para llegar a la siguiente puntuación te faltan {61-puntuacion} puntos")
elif 61<= puntuacion <= 80:
    print("Esta clasificado en el nivel avanzado")
    print(f"Para llegar a la siguiente puntuación te faltan {81-puntuacion} puntos")
elif 81<= puntuacion <= 100:
    print("Esta clasificado en el nivel excelente")
    print(f"Felicidades {nombre}, haz alcanzado el nivel excelente con {puntuacion} puntos")
    if puntuacion < 100:
        print(f"Te faltan {100-puntuacion} puntos para llegar al total de puntos")

#if para ver si la puntuacion fue par o impar
if puntuacion%2 ==0:
    print("La puntuacion es par")
else:
    print("La puntuacion es impar")

"""El código valida una puntuación del 0 al 100 y la categoriza en cinco niveles y
verifica si el número es par o impar mediante el % 2 y calcula los puntos
requeridos para el siguiente nivel y al alcanzar el nivel excelentemuestra un saludo especial"""