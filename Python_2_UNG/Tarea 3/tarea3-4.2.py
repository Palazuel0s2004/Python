#Ejercicio B2: Control de Inventario Básico
#En un almacén, recibimos cajas de productos. Llevamos un control de cuántas
#cajas de cada producto tenemos, pero no nos importa su posición, solo la cantidad.
#Operaciones:
#1. Añadir 2 cajas de "Manzanas".
#2. Añadir 3 cajas de "Peras".
#3. Añadir 1 caja de "Manzanas".
#4. Añadir 2 cajas de "Naranjas".
#5. Se venden (eliminan) 2 cajas de "Peras".
#6. Se vende 1 caja de "Manzanas".
#Instrucciones:
#Simula este proceso con una Bolsa. Después de cada operación, muestra el estado
#actual del inventario (qué productos y cuántas cajas hay). Para la venta, asume
#que la bolsa tiene una operación eliminar(producto) que quita una ocurrencia
#del producto (o puedes plantear que la operación recibe la cantidad a eliminar).

from collections import Counter
inventario = Counter()
def mostrar_estado():
    if not inventario:
        print("El inventario está vacío")
    else:
        resumen = [f"{f}: {c}" for f, c in inventario.items()]
        print("Estado Actual:", ", ".join(resumen))
while True:
    try:
        print("\t----- CONTROL DE INVENTARIO -----");print("")
        print("1. Añadir cajas | 2. Vender (Quitar) cajas | 3. Ver Inventario Actual | 4. Salir");print("")
        opcion = int(input("Seleccione una opción: "));print("")
        #Añadir productos
        if opcion == 1:
            print("--- AÑADIR PRODUCTOS ---");print("")
            print("1. Manzana | 2. Pera | 3. Naranja");print("")
            fruta_op = int(input("Elija fruta: "))
            cant = int(input("¿Cuántas cajas añade?: "))
            nombres = {1: "Manzana", 2: "Pera", 3: "Naranja"}
            #Si fruta esta en nombres pasa
            if fruta_op in nombres:
                fruta = nombres[fruta_op]
                inventario[fruta] += cant
                print(f"Se añadieron {cant} cajas de {fruta}.");print("")
                mostrar_estado()
        #Vender (quita de la lista)
        elif opcion == 2:
            print("--- VENDER PRODUCTOS ---");print("")
            print("1. Manzana | 2. Pera | 3. Naranja");print("")
            fruta_op = int(input("Elija fruta: "))
            cant = int(input("¿Cuántas cajas se vendieron?: "))
            #Diccionario
            nombres = {1: "Manzana", 2: "Pera", 3: "Naranja"}
            if fruta_op in nombres:
                fruta = nombres[fruta_op]
                #Si la cantidad de cajas de la fruta elegida es mayor entonces se resta
                if inventario[fruta] >= cant:
                    inventario[fruta] -= cant
                    print(f"Se vendieron {cant} cajas de {fruta}.");print("")
                    mostrar_estado()
                else:
                    print(f"Stock insuficiente. Solo tienes {inventario[fruta]} cajas");print("")
                    mostrar_estado()
        #Mostrar inventario
        elif opcion == 3:
            mostrar_estado()
        #ciERRE DEL PROGRAMA
        elif opcion == 4:
            mostrar_estado()
            break
        else:
            print("Ingrese una opcion valida")
    except ValueError:
        print("Por favor, ingrese solo números.");print("")