#EJERCICIO 3
#Hacer un vector de 10 valores. Determinar el número mayor y el número menor del vector.
#Imprimir ambos resultados.

max = 0
min = 100000000000000000000
vector = []

print("INGRESE LOS NUMEROS")

for i in range(10):
    vector.append(int(input("Ingrese el numero: ")))

for i in range(10):
    if vector[i]>max:
        max = vector[i]
    if vector[i]<min:
        min = vector[i]

print("El numero mayor es: ", max)
print("El numero menor es: ", min)
