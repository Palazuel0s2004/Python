#Problema: Simular una fila de banco donde llegan 3 clientes ("Ana", "Bruno","Carlos") y
#luego el cajero atiende a 2 clientes.

print("FILA DE BANCO")
print(" ")
clientes = []
print("Llegan los clientes")
print(" ")
n = int(input("Ingrese la cantidad de nombres que seran cargados: "))
for i in range(n):
    clientes.append(input("Ingrese un nombre: "))
    print(" ")
    print(clientes[i],"llego, Cola actualmente: ", clientes)
    print(" ")

print("COMIENZA LA ATENCION")
print(" ")
print("La cola es: ", clientes)
atendidos = ""
j = 0
#While hecho para una posible carga de clientes dentro del procedimiento de atencion
while j<len(clientes):
    for i in range(n-1):
        atendidos = atendidos + clientes[i] + ", "
        print(" ")
        print("Atendiendo a", clientes[i], "Cola restante: ", clientes[i+1:])
        print(" ")
        clientes.pop()
        #llegada de mas clientes
        var= int(input(("Llegaron mas clientes en la cola? [1-Si, (Cualquier otro numero)-No]: ")))
        if var==1:
            print(" ")
            m = int(input("Ingrese la cantidad de clientes que llegaron a la cola: "))
            if m<=0:
                print(" ")
                print("Ingrese un numero valido (Mayor a Cero): ")
            else:
                for o in range(m):
                    n+=1
                    print(" ")
                    clientes.append(input("Ingrese el nombre del cliente: "))
        else:
            continue          
        if i==n-1:
            print(" ")
            print(f"Fin de la simulacion (atendimos a {n-1} clientes): ", atendidos[:-2])
            break