precio_inicial = float(input("Ingrese el costo del producto: "))
iva = float(input("Ingrese el valor de IVA a aplicar producto:"))
precio_final = (precio_inicial * iva) + precio_inicial
print("El precio final a pagar con IVA es: ", precio_final)