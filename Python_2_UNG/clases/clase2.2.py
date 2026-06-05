#Problema: Simular una fila de banco donde llegan 3 clientes ("Ana", "Bruno","Carlos") y
#luego el cajero atiende a 2 clientes.

print("FILA DE BANCO")

clientes = []
print("Llegan los clientes")

a = "Ana"
clientes.append(a)
print(a,"llego, Cola actualmente: ", clientes)

b = "Bruno"
clientes.append(b)
print(b, "llego, Cola actualmente: ", clientes)

c = "Carlos"
clientes.append(c)
print(c, "llego, Cola actualmente: ", clientes)

print("COMIENZA LA ATENCION")
atendidos = ""
for i in range(len(clientes)):
    atendidos = atendidos + clientes[i] + ", "
    print("Atendiendo a", clientes[i], "Cola restante: ", clientes[i+1:])
    if i==1:
        print("Fin de la simulacion (atendimos a 2 clientes): ", atendidos[:-2])
        break
        