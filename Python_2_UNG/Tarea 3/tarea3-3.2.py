#Ejercicio S2: Correos Únicos
#Se tiene una lista de correos electrónicos, pero algunos están repetidos.
#Queremos obtener una lista con los correos únicos (sin duplicados).
#Lista original:
#text
#["ana@gmail.com", "carlos@hotmail.com", "ana@gmail.com", "pedro@yahoo.com", "
#luis@gmail.com", "carlos@hotmail.com"]
#Instrucciones:
#1. Crea un Conjunto vacío.
#2. Recorre la lista de correos y añade cada uno al conjunto.
#3. Al final, imprime el contenido del conjunto. ¿Qué observas? ¿Qué ha pasado con los duplicados?

correos = ["ana@gmail.com", "carlos@hotmail.com", "ana@gmail.com", "pedro@yahoo.com",
           "luis@gmail.com", "carlos@hotmail.com"]
print("Correos ingresados: ", correos);print("")
cor_ori = set() #Conjunto
cor_dup = [] #correos duplicados

for i in correos:
    if i in cor_ori:
        cor_dup.append(i)
    else:
        cor_ori.add(i)

print("Correos sin duplicados: ", cor_ori);print("")
print("Correos duplicados: ", cor_dup);print("")