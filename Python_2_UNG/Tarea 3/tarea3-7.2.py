# Ejercicio L1: Insertar al Principio
# Simularemos una Lista Enlazada usando una lista de Python

lista_enlazada = []
print(f"Estado inicial: {lista_enlazada}")

lista_enlazada.insert(0, 5)
print(f"1. Insertar 5 al principio: {lista_enlazada}")

lista_enlazada.insert(0, 3)
print(f"2. Insertar 3 al principio: {lista_enlazada}")

lista_enlazada.insert(0, 8)
print(f"3. Insertar 8 al principio: {lista_enlazada}")

print("\n" + "="*30)
print(f"¿Cómo queda la lista finalmente? {lista_enlazada}")
print(f"¿Cuál es el primer elemento? {lista_enlazada[0]}")
print("="*30)