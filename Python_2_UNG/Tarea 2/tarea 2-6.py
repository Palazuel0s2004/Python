#Simula la fila de atención de un banco con un solo cajero. El programa debe permitir:
#· Llegada de cliente (agregar nombre al final de la fila)
#· Atención de cliente (atender al primero de la fila)
#· Mostrar fila actual (quiénes están esperando)
#· Mostrar cuántos clientes hay en fila
#Pregunta: ¿Qué TDA modela naturalmente una fila de personas?

fila = []
aten = []
num = 0
while True:
    print(f"Fila: {fila}, Clientes: {num}");print("")
    print("1.Ingresar cliente | 2.Atender Cliente | 3.Salir")
    opc = int(input());print("")
    if opc==1: 
        cliente = input("Ingrese el nombre del paciente: ");print("")
        fila.append(cliente)
        num+=1
        print(f"El cliente {cliente} ha sido ingresado a la fila");print("")
    elif opc==2:
        if len(fila)>0:
            atendidos = fila.pop(0)
            aten.append(atendidos)
            num-=1
            print(f"El cliente {atendidos} ha sido atentido");print("")
        else:
            print("No hay clientes en la fila");print("")
    elif opc == 3:
        print("Programa finalizado");print("")
        break
    else:
        print("Opcion no valida, favor ponga un numero valido (1 al 3)");print("")
    
    