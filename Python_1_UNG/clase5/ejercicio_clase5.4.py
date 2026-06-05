#EJERCICIO 4
#Un supermercado desea llevar un registro de los productos, precios y cantidades de un cliente
#que ingresa 5 veces. A partir de ellos Realizar lo siguiente:
#* Permita ingresar el nombre de los productos en un vector.
#* Permita ingresar el precio de cada producto en otro vector paralelo.
#* Permita ingresar la cantidad de cada producto comprado en un tercer vector.
#Muestre en pantalla un resumen de la compra, indicando:
#* Nombre del producto
#* Precio unitario
#* Cantidad comprada
#* Subtotal por producto
#* Al final, Calcule y muestre el total a pagar.

vector1 = []
vector2 = []
vector3 = []
vector4 = []
total = 0


for i in range(5):
    vector1.append(input("Ingrese el nombre del producto: "))
    vector2.append(int(input("Ingrese el precio del vector: ")))
    vector3.append(int(input("Ingrese la cantidad del producto: ")))
    vector4.append(vector2[i]*vector3[i])
    total += vector4[i]


for i in range(5):
    print("---------RESUMEN DEL PRODUCTO---------")
    print("Nombre del producto: ", vector1[i])
    print("Precio del producto: ", vector2[i])
    print("Cantidad del producto: ", vector3[i])
    print("Subtotal del producto: ", vector4[i])
    print("-----FIN DEL RESUMEN DEL PRODUCTO------")

print("Monto total a pagar: ", total)