#Ejercicio V2: Invertir una Lista
#Dado el siguiente vector dinámico: [10, 20, 30, 40, 50]
#Crea un nuevo vector que contenga los elementos en orden inverso. No uses
#funciones de reversión incorporadas, hazlo manualmente recorriendo el vector original.
#Resultado esperado: [50, 40, 30, 20, 10]

v = [10, 20, 30, 40, 50]
vector = v[:]
rever = []

while len(vector)>0:
    elem = vector.pop();rever.append(elem)
print("Orden principal: ", v);print("")
print("Orden Inverso: ", rever);print("")   