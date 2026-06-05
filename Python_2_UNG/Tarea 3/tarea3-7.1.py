#Ejercicio L1: Insertar al Principio
#Tenemos una lista enlazada vacía.
#Describe paso a paso (con dibujos mentales o en papel) qué sucede cuando insertamos los siguientes números siempre al principio de la lista:
#1. Insertar 5.
#2. Insertar 3.
#3. Insertar 8.
#Pregunta: ¿Cómo queda la lista finalmente? ¿Cuál es el primer elemento?


lista_enlazada = []
print("Estado inicial:", lista_enlazada)

lista_enlazada.insert(0, 5)
print("1. Insertamos 5:", lista_enlazada)

lista_enlazada.insert(0, 3)
print("2. Insertamos 3:", lista_enlazada)

lista_enlazada.insert(0, 8)
print("3. Insertamos 8:", lista_enlazada)

print("\t--- RESULTADOS ---")
print(f"¿Cómo queda la lista finalmente? {lista_enlazada}")
print(f"¿Cuál es el primer elemento? {lista_enlazada[0]}")