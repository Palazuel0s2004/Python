#Escribir un programa que pregunte al usuario los números ganadores de un sorteo, los almacene
# en una lista y los muestre por pantalla ordenados de menor a mayor.

ganadores = []
n = int(input("¿Cuántos números ganadores hay? "))

for i in range(n):
    num = int(input(f"Ingrese el número ganador {i+1}: "))
    ganadores.append(num)

ganadores.sort()
print("Números ganadores ordenados:", ganadores)