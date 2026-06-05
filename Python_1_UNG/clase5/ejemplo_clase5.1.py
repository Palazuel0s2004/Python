sum=0
vector= []
print("INGRESE LOS ELEMENTOS DEL VECTOR")
for i in range(4):
    vector.append(int(input("Ingresa el número")))
print("Los elementos cargados son: ")
for i in range(4):
    print(vector[i])
for i in range(4):
    if vector[i] % 3 == 0:
        sum = sum + vector[i]

print("La suma de multiplos de 3 es: ", sum)