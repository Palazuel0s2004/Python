#Escribir un programa que visualice en pantalla los números pares entre 1 y 25.

print("Numeros pares entre 1 y 25: ")
for i in range(1, 26):
    if i % 2 == 0:
        print(i, end=", ")