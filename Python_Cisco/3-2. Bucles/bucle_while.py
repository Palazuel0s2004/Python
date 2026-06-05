bloques = int(input("Ingrese el número de bloques: "))
altura = 0
capa_actual = 1

while capa_actual <= bloques:
    altura += 1
    bloques -= capa_actual  # Resta los bloques usados en la capa
    capa_actual += 1        # La siguiente capa necesita más bloques

print("La altura de la pirámide:", altura)