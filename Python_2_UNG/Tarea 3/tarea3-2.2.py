#Ejercicio C2: Simulador de Impresión
#Una impresora tiene una cola de trabajos. Cada trabajo tiene un nombre (ej:
#"Doc1.pdf", "Foto.jpg").
#Implementa las siguientes operaciones mostrando el estado de la cola después de cada una:
#1. Encolar: "Informe.docx"
#2. Encolar: "Presentacion.ppt"
#3. Encolar: "Hoja.xls"
#4. Desencolar (imprimir)
#5. Encolar: "Carta.txt"
#6. Desencolar

impresora = []
print("IMPRESORA")
while True:
    try:
        print("1.Agregar archivos | 2.Imprimir elementos | 3.Mostrar cola | 4.Salir")
        opc = int(input())
        if opc==1:
            impresora.append(input("Ingrese el archivo: "))
            print(f"Trabajos encolados: {impresora}")
        elif opc==2:
            if len(impresora)>0:
                impreso = impresora.pop(0)
                print(f"Imprimiendo {impreso}, cola pendiente: {impresora}")
            else:
                print("No hay elementos en la cola de impresion")
        elif opc==3:
            print(f"Cola de impresion: {impresora}")
        elif opc==4:
            break
        else:
            print("Error. Ingrese una opcion valida (1 al 4)")
    except ValueError:
        print("Error en el dato ingresado")