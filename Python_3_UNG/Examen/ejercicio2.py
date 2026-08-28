#Ejercicio 2: Control de edades en un curso
#El programa debera procesar exactamente 5 estudiantes:
#Por cada estudiante ingresar:
# -Nombre
# -Edad
#El programa debera:
# -Contar mayores de edad
# -Contar menores de edad
# -Mostrar la edad mayor
# -Mostrar la edad menor
#La edad debe estar comprendida entre 16 y 100 años

#Indicadores:
#Indicador                                                  #Puntaje
#Entrada y validacion de Datos                              2 puntos
#Uso correcto del ciclo                                     2 puntos
#Acumuladores y contadores                                  2 puntos
#Mayor y menor edad                                         2 puntos
#Salida correcta                                            2 puntos
#Total                                                      10 puntos

mayor_edad = 0
menor_edad = 0

nombre1 = input("Ingrese el nombre del primer estudiante: ").strip()

while True:
    try:
        edad1 = int(input("Ingrese la edad del primer estudiante: "))
        if 16<=edad1<=100:
            if edad1>=18:
                mayor_edad+=1
            else:
                menor_edad+=1
            break
        else:
            print("Error, ingrese la edad debe estar entre 16 y 100 años")
    except ValueError:
        print("Error, ingrese una edad valida")

nombre2 = input("Ingrese el nombre del segundo estudiante: ").strip()

while True:
    try:
        edad2 = int(input("Ingrese la edad del segundo estudiante: "))
        if 16<=edad2<=100:
            if edad2>=18:
                mayor_edad+=1
            else:
                menor_edad+=1
            break
        else:
            print("Error, ingrese la edad debe estar entre 16 y 100 años")
    except ValueError:
        print("Error, ingrese una edad valida")

nombre3 = input("Ingrese el nombre del tercer estudiante: ").strip()

while True:
    try:
        edad3 = int(input("Ingrese la edad del tercer estudiante: "))
        if 16<=edad3<=100:
            if edad3>=18:
                mayor_edad+=1
            else:
                menor_edad+=1
            break
        else:
            print("Error, ingrese la edad debe estar entre 16 y 100 años")
    except ValueError:
        print("Error, ingrese una edad valida")

nombre4 = input("Ingrese el nombre del cuarto estudiante: ").strip()

while True:
    try:
        edad4 = int(input("Ingrese la edad del cuarto estudiante: "))
        if 16<=edad4<=100:
            if edad4>=18:
                mayor_edad+=1
            else:
                menor_edad+=1
            break
        else:
            print("Error, ingrese la edad debe estar entre 16 y 100 años")
    except ValueError:
        print("Error, ingrese una edad valida")

nombre5 = input("Ingrese el nombre del quinto estudiante: ").strip()

while True:
    try:
        edad5 = int(input("Ingrese la edad del quinto estudiante: "))
        if 16<=edad5<=100:
            if edad5>=18:
                mayor_edad+=1
            else:
                menor_edad+=1
            break
        else:
            print("Error, ingrese la edad debe estar entre 16 y 100 años")
    except ValueError:
        print("Error, ingrese una edad valida")

mayor = edad1; menor = edad1

if edad2>mayor:
    mayor = edad2
if edad3>mayor:
    mayor = edad3
if edad4>mayor:
    mayor = edad4
if edad5>mayor:
    mayor = edad5

if edad2<menor:
    menor = edad2
if edad3<menor:
    menor = edad3
if edad4<menor:
    menor = edad4
if edad5<menor:
    menor = edad5

print("\tResumen General")
print("Estudiante 1: ", nombre1, ", edad: ", edad1)
print("Estudiante 2: ", nombre2, ", edad: ", edad2)
print("Estudiante 3: ", nombre3, ", edad: ", edad3)
print("Estudiante 4: ", nombre4, ", edad: ", edad4)
print("Estudiante 5: ", nombre5, ", edad: ", edad5)
print("La cantidad de mayores de edad es: ", mayor_edad)
print("La cantidad de menores de edad es: ", menor_edad)
print("La edad mayor es: ", mayor)
print("La edad menor es: ", menor)