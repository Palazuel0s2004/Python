numeros = []
for i in range(20):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

print("Lista ingresada:", numeros)

mayor = numeros[0]
posicion = 0

for i in range(1, len(numeros)):
    if numeros[i] > mayor:
        mayor = numeros[i]
        posicion = i

print(f"El número mayor es {mayor} y está en la posición {posicion+1} (índice {posicion+1}).")