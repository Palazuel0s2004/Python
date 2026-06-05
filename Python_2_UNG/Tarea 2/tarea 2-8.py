#Ejercicio 8: Sistema de Turnos en una Clínica IPS
#Problema: Una clínica dental necesita un sistema de turnos. Los pacientes llegan y se les
# asigna un número de turno correlativo. El programa debe:
#· Registrar nuevo paciente (asignar siguiente número)
#· Llamar a siguiente paciente (el que lleva más tiempo esperando)
#· Mostrar lista de espera (con sus números de turno)
#· Mostrar cuántos pacientes hay en espera
#Ejemplo
#Acción: Registrar paciente
#Nombre: María → Turno #1 asignado a María
#Acción: Registrar paciente
#Nombre: Juan → Turno #2 asignado a Juan
#Acción: Llamar paciente
#Llamando a: María (Turno #1)
#Acción: Mostrar espera
#En espera: Juan (Turno #2)
#Pregunta: ¿Qué TDA garantiza que el primer paciente registrado sea el primero en ser llamado?

cliente = []
i=1
print("CLINICA DENTAL")
while True:
    try:
        print("1.Registrar paciente | 2.Atender paciente | 3.Salir")
        opc = int(input())
        if opc==1:
            nombre = input("Ingrese nombre del paciente: ")
            cliente.append(f"N° {i} "+ nombre)
            print(f"Paciente {nombre} registrado en el N° {i}")
            i+=1
        elif opc==2:
            if len(cliente)>0:
                atendiendo = cliente.pop(0)
                print(f"Atendiendo al paciente {atendiendo}")
            else:
                print("No hay pacientes en la lista")
        elif opc==3:
            print(f"Lista final: {cliente}")
            break
        else:
            print("Error. Ingrese una opcion valida (1 al 3)")
    except ValueError:
        print("Error en el dato ingresado")
