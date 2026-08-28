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

nombre = []
edad_estudiante = []

while len(nombre)<5:
    nom = input("Ingrese el nombre del estudiante: ").strip()
    nombre.append(nom)
    while True:
        try:
            edad = int(input("Ingrese la edad del estudiante: "))
            if 16<=edad<=100:
                edad_estudiante.append(edad)
                if edad>=18:
                    mayor_edad+=1
                else:
                    menor_edad+=1
                break
            else:
                print("Error, ingrese la edad debe estar entre 16 y 100 años")
        except ValueError:
            print("Error, ingrese una edad valida")

mayor = 0; menor = 100000

for i in range(len(edad_estudiante)):
    if edad_estudiante[i]>mayor:
        mayor = edad_estudiante[i]

    if edad_estudiante[i]<menor:
        menor = edad_estudiante[i]


print("\tResumen General")
for i in range(len(nombre)):
    print(f"Estudiante nro {i+1}: ", nombre[i],", edad: ", edad_estudiante[i])
print("La cantidad de mayores de edad es: ", mayor_edad)
print("La cantidad de menores de edad es: ", menor_edad)
print("La edad mayor es: ", mayor)
print("La edad menor es: ", menor)