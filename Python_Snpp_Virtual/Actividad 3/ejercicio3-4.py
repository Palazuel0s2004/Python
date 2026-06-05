#Pedir por teclado 10 números. Indicar cuántos de ellos son números positivos, cuantos son números negativos
# y la cantidad de ceros.

positivos = 0
negativos = 0
ceros = 0

for i in range(10):
    num = float(input(f"Ingrese el número {i+1}: "))
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        ceros += 1

print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Ceros: {ceros}")