secret_number = 777
print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")
n = int(input())

while n != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    n = int(input("Intente adivinar el numero: "))

print("¡Bien hecho, muggle! Eres libre ahora.")