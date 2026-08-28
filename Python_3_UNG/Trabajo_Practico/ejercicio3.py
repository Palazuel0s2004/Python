#3. Precio final de una compra con IVA y descuento
#Solicitar:
    #Nombre del producto.
    #Precio unitario.
    #Cantidad comprada.
    #Porcentaje de IVA.
    #Porcentaje de descuento.
#El programa deberá calcular:
    #Subtotal sin IVA.
    #Monto del descuento.
    #Subtotal después del descuento.
    #Monto correspondiente al IVA.
    #Precio final de la compra.
#El descuento solamente se aplicará cuando el subtotal sea superior a G. 500.000. En caso
#contrario, deberá mostrarse un mensaje indicando que la compra no alcanza el monto
#mínimo para obtener descuento.

nombre = []    # Lista para los nombres de los productos
precio = []    # Lista para los precios unitarios
cantidad = []  # Lista para las cantidades compradas
minimo_desc = 500000  # G. 500.000 como umbral para el descuento

while True:
    nom_pro = input("\nIngrese el nombre del producto (escriba 's' para terminar): ").strip()
    
    # Condición de salida
    if nom_pro.lower() == 's' or nom_pro == '':
        break
        
    # Validar Precio Unitario
    while True:
        try:
            pre_uni = float(input(f"Ingrese el precio unitario de '{nom_pro}': Gs. "))
            if pre_uni <= 0:
                print("Error: El precio debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("Error: Debe ingresar un número válido para el precio.")
            
    # Validar tipo de venta (Granel o Unidades)
    while True:
        granel = input("¿El producto se vende por kilo? (s/n): ").strip().lower()
        if granel in ['s', 'n']:
            break
        print("Opción no válida. Ingrese 's' para Sí o 'n' para No.")
        
    # Validar Cantidad
    while True:
        try:
            if granel == 's':
                cant_com = float(input("Ingrese la cantidad en kg: "))
            else:
                cant_com = int(input("Ingrese la cantidad de unidades: "))
                
            if cant_com <= 0:
                print("Error: La cantidad debe ser mayor a cero.")
                continue
            break
        except ValueError:
            print("Error: Ingrese un valor numérico válido para la cantidad.")

    # Guardar datos en las listas
    nombre.append(nom_pro)
    precio.append(pre_uni)
    cantidad.append(cant_com)
    
    print(f"-> '{nom_pro}' agregado correctamente.")

# Verificar si se registraron productos
if len(nombre) == 0:
    print("\nNo se registraron compras.")
else:
    # Bucle para solicitar y validar el porcentaje de IVA (0% a 100%)
    while True:
        try:
            porcentaje_iva = float(input("\nIngrese el porcentaje de IVA (ej. 10): "))
            if 0 <= porcentaje_iva <= 100:
                iva = porcentaje_iva / 100
                break
            print("Error: El IVA debe estar entre 0% y 100%.")
        except ValueError:
            print("Error: Ingrese un número válido.")

    # Bucle para solicitar y validar el porcentaje de Descuento (0% a 100%)
    while True:
        try:
            porcentaje_desc = float(input("Ingrese el porcentaje de Descuento (ej. 5): "))
            if 0 <= porcentaje_desc <= 100:
                descuento = porcentaje_desc / 100
                break
            print("Error: El descuento debe estar entre 0% y 100%.")
        except ValueError:
            print("Error: Ingrese un número válido.")

    # Cálculo del Subtotal inicial
    subtotal_sin_iva = 0.0
    for i in range(len(nombre)):
        subtotal_sin_iva += precio[i] * cantidad[i]

    monto_descuento = 0.0
    
    # Evaluación del monto mínimo para descuento
    if subtotal_sin_iva > minimo_desc:
        monto_descuento = subtotal_sin_iva * descuento
        if monto_descuento > 0:
            mensaje_descuento = f"Descuento aplicado ({porcentaje_desc:.2f}%): -G. {monto_descuento:,.2f}"
        else:
            mensaje_descuento = "Monto mínimo alcanzado, pero el descuento ingresado fue 0%."
    else:
        mensaje_descuento = f"No alcanza el monto mínimo (G. {minimo_desc:,.2f}) para obtener descuento."

    # Cálculos finales
    subtotal_con_descuento = subtotal_sin_iva - monto_descuento
    monto_iva = subtotal_con_descuento * iva
    precio_final = subtotal_con_descuento + monto_iva

    # Mostrar resumen
    print("\n" + "=" * 55)
    print("                RESUMEN DE LA COMPRA")
    print("=" * 55)
    for i in range(len(nombre)):
        item_total = precio[i] * cantidad[i]
        print(f" • {nombre[i]}: {cantidad[i]} x G. {precio[i]:,.2f} = G. {item_total:,.2f}")
    
    print("-" * 55)
    print(f"Subtotal sin IVA:             G. {subtotal_sin_iva:,.2f}")
    print(f"Estado de Descuento:          {mensaje_descuento}")
    print(f"Subtotal tras descuento:      G. {subtotal_con_descuento:,.2f}")
    print(f"Monto correspondiente al IVA: G. {monto_iva:,.2f}")
    print("=" * 55)
    print(f"PRECIO FINAL DE LA COMPRA:    G. {precio_final:,.2f}")
    print("=" * 55)
"""El codigo registra las variables de los productos mediante iteraciones continua, tambien
solicita porcentajes de iva y descuento validando que sean coherentes y al culminar la carga
calcula el subtotal y evalúa si supera los G. 500.000 para aplicar el porcentaje de descuento y
luego calcula el iva proporcional sobre el subtotal resultante e imprime el desglose financiero final
"""