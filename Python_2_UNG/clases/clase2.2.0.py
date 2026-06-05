#Problema: Simular una fila de banco donde llegan 3 clientes ("Ana", "Bruno","Carlos") y
#luego el cajero atiende a 2 clientes.

print("FILA DE BANCO")

clientes = []
print("Llegan los clientes")

for i in range(3):
    clientes.append(input("Ingrese un nombre: "))
    print(clientes[i],"llego, Cola actualmente: ", clientes)

print("COMIENZA LA ATENCION")

print("La cola es: ", clientes)

atendidos = ""
for i in range(2):
    atendidos = atendidos + clientes[i] + ", "
    print("Atendiendo a", clientes[i], "Cola restante: ", clientes[i+1:])
    if i==1:
        print("Fin de la simulacion (atendimos a 2 clientes): ", atendidos[:-2])
        break
        