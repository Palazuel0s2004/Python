#14. Conversión de guaraníes a dólares
#• Solicitar una cantidad de dinero en guaraníes.
#• Convertir el monto a dólares utilizando la siguiente cotización:
#• 1 dólar = G. 7.920
#El programa deberá:
#• Validar que el monto sea mayor que cero.
#• Mostrar el equivalente en dólares.
#• Calcular una comisión del 2 %.
#• Mostrar el monto restante después de descontar la comisión.


#While para ingresar el dinero
while True:
    try:
        dinero = int(input("\nIngrese la cantidad de dinero: "))
        if dinero>0: 
            print("\n\tRESUMEN GENERAL")
            print(f"El dinero recibido fue {dinero:,} Gs.")
            break
        else:
            print("Ingrese un numero mayor a 0")
    except ValueError:
        print("Ingrese un numero entero valido")

#Convertidor de guaranies a Dolares
conv_dolar = dinero / 7920

#Comision
comision = conv_dolar * 0.02

#Monto recibido descontando la comision
total_recibido = conv_dolar - comision

print(f"{dinero} Gs en dolares es: {conv_dolar:,.2f} $")
print(f"La comision a descontar es: {comision:,.2f} $")
print(f"El monto total a recibir es: {total_recibido:,.2f} $")

"""El algoritmo realiza el cambio de divisas de Guaraníes a Dólares según la tasa fija de 7.920
y verifica que la suma ingresada sea mayor a cero y determina la conversión bruta, tambien calcula el cobro
de comisión del 2% y presenta la liquidación final neta a entregar al usuario"""