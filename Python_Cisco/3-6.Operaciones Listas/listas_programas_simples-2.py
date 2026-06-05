#Encontrar la ubicacion de un elemento

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False
 
for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break
 
if found:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")
 
# Nota:
#El valor buscado se almacena en la variable to_find;
#El estado actual de la búsqueda se almacena en la variable found (True/False).
#Cuando found se convierte en True, se sale del bucle for.

