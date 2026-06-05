#EJERCICIOS BUCLES Y CONDICIONALES
#EJERCICIO 1
#Una tienda de electrodomésticos desea registrar las ventas de un día.
#El cajero debe ingresar el precio de cada producto vendido y el medio de pago
# (1 = efectivo, 2 = tarjeta).
#El sistema debe terminar cuando el cajero ingrese 0 como precio (fin del día).
#Se debe calcular:
#1. La suma total de las ventas entre 100.000 y 500.000.
#2. La cantidad de productos fuera de ese rango.
#3. La cantidad de productos pagados en efectivo 
#4. La cantidad de productos pagados con tarjeta.
#5. El monto total recaudado en el día.

efe = 0 #Efectivo
tar = 0 #Tarjeta
cont = 0 #Contador de productos fuera de rango
suma = 0 #La suma de los que valen 100.000 y 500.000
suma_total = 0 #La suma de todo

while True:
    pag = int(input("Ingrese el precio: "))
    if pag> 99999 and pag<500000:
        suma += pag
    elif pag != 0:
        cont += 1
    suma_total += pag
    if pag == 0:
        break
    while True:
        met = int(input("Ingrese el metodo de pago 1-Efectivo 2-Tarjeta: "))
        if met == 1:
            efe += 1
        elif met == 2:
            tar += 1
        else:
            print("Ingrese un numero valido por favor")
        if met == 2 or met == 1:
            break

print("La suma total de las ventas entre 100.000 y 500.000 es: ", suma)
print("La cantidad de productos fuera de ese rango es: ", cont)
print("La cantidad de productos pagados en efectivo: ", efe)
print("La cantidad de productos pagados con tarjeta: ", tar)
print("El monto total recaudado en el día: ", suma_total)
    