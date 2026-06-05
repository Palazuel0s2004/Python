#Ejercicio S1: Amigos en Común
#Dados dos conjuntos de amigos (representados por sus nombres), encuentra qué amigos tienen en común.
#Datos:
#• Amigos de Ana: {"Pedro", "Luis", "Maria", "Juan"}
#• Amigos de Carlos: {"Maria", "Sofia", "Pedro", "Diego"}
#Instrucciones:
#1. Representa cada lista como un Conjunto.
#2. Encuentra la intersección de ambos conjuntos (los amigos en común).
#3. Imprime el resultado.

Ana = {"Pedro", "Luis", "Maria", "Juan"}
Carlos = {"Maria", "Sofia", "Pedro", "Diego"}

print("Amigos de Ana: ", Ana);print(" ")
print("Amigos de Carlos: ", Carlos);print(" ")

Ana_Carlos = Ana & Carlos

print("Los amigos que Ana y Carlos tienen en comun son: ", Ana_Carlos)