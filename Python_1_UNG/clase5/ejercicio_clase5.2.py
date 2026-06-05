#EJERCICIO 2
#Ingresar un vector de N elementos.
#Calcular suma de los elementos pares, caso contrario calcular la cantidad de elementos que esten 
#entre 1 y 10, caso contrario contarlos. Imprimir los resultados.

sum = 0
elem = 0
cont = 0
vector = []
n = int(input("Ingrese el tamaño de vector: "))

for i in range(n):
    vector.append(int(input("Ingrese el numero: ")))

for i in range(n):
    if vector[i]% 2 == 0:
        sum += vector[i]
    elif vector[i]>=1 and vector[i]<=10:
        elem +=1
    else:
        cont += 1

print("La suma de los elementos pares es: ", sum)
print("La candidad de elementos entre 1 al 10 es: ", elem)
print("Los numeros que estan fuera del rango son: ", cont) 