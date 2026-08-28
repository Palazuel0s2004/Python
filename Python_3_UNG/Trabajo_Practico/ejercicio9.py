#9. Números pares e impares
#• Solicitar al usuario un número entero comprendido entre 10 y 100.
#• Utilizando un ciclo for, recorrer los números desde 1 hasta el límite ingresado.
#El programa deberá:
#• Mostrar los números pares.
#• Mostrar los números impares.
#• Contar cuántos números pares existen.
#• Contar cuántos números impares existen.
#• Mostrar la suma de los números pares.
#• No utilizar listas

#While para el numero que ingresara el usuario
while True:
    try:
        num = int(input("\nIngrese el numero (Entre 10 y 100): "))
        if 10 <= num <= 100:
            break
        else:
            print("Ingrese un numero valido (Entre 10 y 100)")
    except ValueError:
        print("Error: Ingrese un número.")

num_par = 0 #Variable para contador de numero par
num_impar = 0 #Variable para contador de numero impar
suma_num_par = 0 #Variable para almacenar las sumas de pares

#Para almacenar la cantidad de pares e impares
pares = ""
impares = ""
for i in range(1, num + 1):
    if i % 2 == 0:
        pares += str(i) + " "
        num_par += 1
        suma_num_par += i
    else:
        impares += str(i) + " "
        num_impar += 1

#Prints finales
print(f"\nLos numeros pares entre 1 y {num} son: {pares}")
print(f"La cantidad de numeros pares es: {num_par}")
print(f"La suma de los numeros pares obtenidos es: {suma_num_par}")

print(f"\nLos numeros impares entre 1 y {num} son: {impares}")
print(f"La cantidad de numeros impares es: {num_impar}")

"""El programa ejecuta un ciclo for iterando de 1 al límite ingresado y sin hacer uso de listas
concateno la secuencia de números pares e impares en cadenas de texto separadas calculando
a la vez la cantidad de cada uno y la suma exclusiva de los númerospares"""