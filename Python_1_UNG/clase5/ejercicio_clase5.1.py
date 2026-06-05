#EJERCICIOS DE VECTORES
#EJERCICIO 1
#Ingresar un vector de 8 elementos.
#Calcular suma de múltiplos de 7 y 5 por separado. Imprimir los resultados

sum = 0
sum1 = 0
vector = []
print("INGRESE LOS ELEMENTOS DEL VECTOR")

for i in range(8):
    vector.append(int(input("Ingrese el numero: ")))

print("Los elementos cargados son: ")
for i in range(8):
    print(vector[i])

for i in range(8):
    if vector[i]%7 == 0:
        sum += vector[i]
    if vector[i]%5 == 0:
        sum1 += vector[i]
    
print("La suma de los multiplos de 7 es: ", sum)
print("La suma de los multiplos de 5 es: ", sum1)


