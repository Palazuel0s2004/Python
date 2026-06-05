#Ejercicio 5: Verificar Palíndromos
#Problema: Un palíndromo es una palabra que se lee igual al derecho y al revés
# (ej: "ANNA", "RADAR", "OSO"). Escribe un programa que determine si una palabra ingresada
# es palíndromo usando una pila.
#Ejemplos:
#· Entrada: "ANNA" → ES PALÍNDROMO
#· Entrada: "RADAR" → ES PALÍNDROMO
#· Entrada: "HOLA" → NO ES PALÍNDROMO (HOLA vs ALOH)
#Pista: Apila cada letra y luego compárala con la palabra original.

vector = []
alap = ""
pala = input("Ingrese la palabra: ")
for i in pala:
    vector.append(i)
    print("Apilado: ", i)
while len(vector)>0:
    alap += vector.pop()
    print("Apilando Inversa: ", alap)

if pala == alap:
    print(f"La palabra es un palindromo: {pala} <---> {alap}")
else:
    print(f"La palabra no es un palindromo: {pala} <---> {alap}")
