#Hacer un programa para ingresar el monto mensual y la cantidad de cuotas en 5 ocasiones.
#Hallar el total general sumando la comisión del 5% en cada ocasión ingresada.
#Imprimir el resultado.
total_general = 0
cont = 0
	
while cont < 5:
    monto_mensual = float(input("Ingrese el monto mensual para la ocasión : "))
    cantidad_cuotas = int(input("Ingrese la cantidad de cuotas para la ocasión : "))
    total_ocasion = monto_mensual * cantidad_cuotas
    total_ocasion_con_comision = total_ocasion * 0.05
    total_general += total_ocasion_con_comision
    cont += 1
	
print(f"El total general sumando la comisión del 5% en cada ocasión es: ${total_general}")
