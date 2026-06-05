#Problema: Dada la palabra "HOLA", usar una pila para obtener "ALOH"}

palabra = "HOLA"
#Forma yo
pal_inv = ""

pila = []

n = len(palabra)

for i in palabra:
    pila.append(i)

for i in range(len(palabra)-1, -1, -1):
        letra = pila[i]
        pal_inv = pal_inv + letra

print(palabra)
print(pal_inv)
#Forma MoureDev
pal_inver = palabra[::-1]
print(pal_inver)