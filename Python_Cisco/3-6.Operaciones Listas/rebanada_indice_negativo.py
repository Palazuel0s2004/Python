my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

#EL resultado es [8, 6, 4]

my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)
 
#La output del fragmento es []

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3] #es un equivalente más compacto de: my_list[0:end]
print(new_list)

#Su output es: [10, 8, 6]


my_list = [10, 8, 6, 4, 2] 
new_list = my_list[3:] #es un equivalente más compacto de: my_list[start:len(my_list)]
print(new_list)
 
#Su output es: [4, 2]


#La instrucción del descrita anteriormente puede eliminar más de un elemento de la lista a la vez - también puede eliminar rebanadas:


my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)
 
#Nota: En este caso, la rebanada ¡no produce ninguna lista nueva
#La output del fragmento es: [10, 4, 2].