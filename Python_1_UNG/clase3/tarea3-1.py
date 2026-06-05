#1.	Realiza un programa ingresar los precios de 5 productos.
#Calcular el promedio de precios. Imprimir los resultados.
sum = 0
cont = 0
while cont < 5:
    precio = int(input("Ingrese el precio del producto: "))
    sum = sum + precio
    cont = cont + 1
    
# Calculamos el promedio de los precios
prom = sum / 5
	
# Imprimimos los resultados
print(f"\nLa suma total de los precios es: ${sum}")
print(f"El promedio de los precios es: ${prom}")
