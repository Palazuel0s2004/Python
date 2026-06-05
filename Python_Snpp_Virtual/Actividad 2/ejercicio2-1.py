#1.Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
n = int(input("Escriba un número entero: "))
if n % 2 == 0:
    print("El numero " + str(n) + " es par")
else:
    print("El numero " + str(n) + " es impar")