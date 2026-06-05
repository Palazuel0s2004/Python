# Leer un número y mostrar su cuadrado, repetir el proceso hasta que se introduzca un número negativo.

while True:
    num = int(input("Ingrese un número (negativo para salir): "))
    if num < 0:
        break
    print(f"Cuadrado de {num}: {num ** 2}")