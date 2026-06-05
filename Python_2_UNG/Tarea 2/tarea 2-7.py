#Ejercicio 7: Turnos en una Imprenta
#Problema:
#En una imprenta, los trabajos de impresión llegan y se procesan en orden de llegada.
# Cada trabajo tiene un nombre (ej: "Documento1", "Fotos", "Tesis"). Simula el proceso donde:
#· Se agregan trabajos a la cola de impresión
#· La impresora procesa un trabajo (lo saca de la cola)
#· Se muestra la cola de trabajos pendientes
#Ejemplo:
#TRABAJOS ENCOlADOS: Tesis, Documento1, Fotos
#Imprimiendo: Tesis
#TRABAJOS PENDIENTES: Documento1, Fotos
#Imprimiendo: Documento1
#TRABAJOS PENDIENTES: Fotos
#Pregunta: ¿Por qué una COLA es la estructura adecuada?

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
                impreso = impresora.pop()
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