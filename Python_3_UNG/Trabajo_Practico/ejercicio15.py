#15. Compra de artículos
#Solicitar:
#• nombre del artículo;
#• cantidad de unidades;
#• precio por unidad.
#El programa deberá:
#• Calcular el subtotal.
#• Aplicar un descuento del 10 % si se compran 10 unidades o más.
#• Calcular el IVA del 10 %.
#• Mostrar el total final.
#• La cantidad y el precio deben ser mayores que cero.

#While para escribir un nombre valido
while True:
    nombre = input("\nIngresa el nombre del producto: ").strip()
    #Elimina espacios en blanco al inicio y al final del nombre
    if nombre.replace(" ", "").isalpha() and len(nombre) > 0:
        break
    else:
        print("Error: Ingrese un nombre válido.")

#While para ingresar el precio del producto
while True:
    try:
        precio = float(input("\nIngrese el precio por unidad del producto: Gs. "))
        if precio > 0:
            break
        else:
            print("Ingrese un número mayor a 0")
    except ValueError:
        print("Error: Ingrese un número válido.")

#While para ingresar la cantidad del producto
while True:
    try:
        cant_prod = int(input("\nIngrese la cantidad comprada del producto: "))
        if cant_prod > 0:
            break
        else:
            print("Ingrese un número mayor a 0")
    except ValueError:
        print("Error: Ingrese un entero válido.")

#Variable para el subtotal
subtotal = precio * cant_prod

# if para evaluar el descuento
if cant_prod >= 10:
    monto_descuento = subtotal * 0.10
    mensaje_desc = "Aplica descuento del 10% por compra mayor o igual a 10 unidades."
else:
    monto_descuento = 0.0
    mensaje_desc = "No aplica descuento (menos de 10 unidades)."

subtotal_con_descuento = subtotal - monto_descuento
# Cálculo del IVA del 10% sobre el valor con descuento
monto_iva = subtotal_con_descuento * 0.10
total_final = subtotal_con_descuento + monto_iva

#Print final
print("\n\tRESUMEN GENERAL DE COMPRA")
print(f"Producto comprado: {nombre}")
print(f"Precio por unidad: Gs. {precio:,.2f}")
print(f"Cantidad comprada: {cant_prod}")
print(f"Subtotal sin descuento: Gs. {subtotal:,.2f}")
print(f"Estado de descuento: {mensaje_desc}")
print(f"Monto descontado: Gs. {monto_descuento:,.2f}")
print(f"Subtotal con descuento: Gs. {subtotal_con_descuento:,.2f}")
print(f"Monto correspondiente al IVA (10%): Gs. {monto_iva:,.2f}")
print("="*40)
print(f"TOTAL FINAL A PAGAR: Gs. {total_final:,.2f}")
print("="*40)

"""El programa procesa la compra de un artículo validando precio y cantidad de positivos
y evalúa si la cantidad alcanza o supera las 10 unidades para otorgar una bonificación del 10% y
calcula el IVA correspondiente y detalla el desglose comercial del monto total a abonar"""