#Solicitar al usuario que ingrese un número entero e informar si es primo o no, utilizando una función booleana que lo decida.

def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

numero = int(input("Ingrese un número entero: "))
if es_primo(numero):
    print("Es primo.")
else:
    print("No es primo.")