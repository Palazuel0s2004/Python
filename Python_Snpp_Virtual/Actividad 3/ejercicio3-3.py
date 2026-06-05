#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba
# “salir” que terminará.

while True:
    entrada = input("Escriba algo (o 'Salir' para terminar): ")
    if entrada.lower() == "salir":
        break
    print(entrada)