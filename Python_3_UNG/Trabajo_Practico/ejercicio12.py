#12. Promedio académico
#Solicitar:
#• Nombre del estudiante; (usa tus datos personales)
#• Tres notas comprendidas entre 1 y 5.
#El programa deberá:
#• Calcular el promedio simple.
#• Indicar si el estudiante aprobó o reprobó.
#• Mostrar la nota más alta.
#• Mostrar la nota más baja.
#Se considera aprobado con promedio igual o mayor que 3

#While para escribir un nombre valido
while True:
    nombre = input("\nIngresa tu nombre: ").strip()
    #Elimina espacios en blanco al inicio y al final del nombre
    if nombre.replace(" ", "").isalpha() and len(nombre) > 0:
        break
    else:
        print("Error: Ingrese un nombre válido.")

#While para insertar las notas en numeros validos (Del 1 al 5)
while True:
    try:
        nota1 = float(input("\nIngrese la primera nota (1 a 5): "))
        if 1 <= nota1 <= 5:
            print("Nota Recibida con Éxito")
            break
        else:
            print("Ingrese una nota válida (Del 1 al 5)")
    except ValueError:
        print("Error: Ingrese un número válido.")

while True:
    try:
        nota2 = float(input("\nIngrese la segunda nota (1 a 5): "))
        if 1 <= nota2 <= 5:
            print("Nota Recibida con Éxito")
            break
        else:
            print("Ingrese una nota válida (Del 1 al 5)")
    except ValueError:
        print("Error: Ingrese un número válido.\n")

while True:
    try:
        nota3 = float(input("\nIngrese la tercera nota (1 a 5): "))
        if 1 <= nota3 <= 5:
            print("Nota Recibida con Éxito")
            break
        else:
            print("Ingrese una nota válida (Del 1 al 5)")
    except ValueError:
        print("Error: Ingrese un número válido.\n")

#Variable para calcular el promedio de las notas
prom = (nota1 + nota2 + nota3) / 3

#Condicional para ver si el estudiante aprobo o no
if prom >= 3:
    res_prom = "Aprobado"
else:
    res_prom = "Reprobado"

#Definicion del numero mayor y menor
mayor = nota1
menor = nota1

#Bloque de if de mayor
if nota2 > mayor:
    mayor = nota2
if nota3 > mayor:
    mayor = nota3

#Bloque de if de menor
if nota2 < menor:
    menor = nota2
if nota3 < menor:
    menor = nota3

#Prints de salida
print("\n\tRESUMEN GENERAL")
print(f"Nombre del estudiante: {nombre}")
print(f"Notas del estudiante: {nota1}, {nota2}, {nota3}")
print(f"El promedio del alumno es: {prom:.2f}")
print(f"El estudiante ha resultado: {res_prom}")
print(f"La nota más baja fue: {menor}")
print(f"La nota más alta fue: {mayor}")

"""El programa registra las tres notas del estudiante con validación estricta en la escala de
1 a 5 y calcula el promedio  determinando la condición de Aprobado con promedio >= 3 o Reprobado
e identifica la nota máxima y mínima mediante comparaciones"""