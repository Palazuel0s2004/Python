#Ejercicio 4
#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.


'''
while True:
    frase = ("Introduce algo: ")
    if frase <> "salir":
    break
    print(frase)
'''

while True:
    frase = input("Introduce algo: ")
    if frase.lower() == "salir":
        break
    print(frase)