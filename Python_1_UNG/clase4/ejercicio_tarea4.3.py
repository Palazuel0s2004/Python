
## El programa debe contar la cantidad de numeros pares, impares y nulos. ##
## la cantidad ingresada debe ser definida por el usuario.                ##
#np: contador de números pares 
#ni:contador de números impares
#nf:cantidad de numeros para el bucle
#nn:contador de números nulos
# x: numeros ingresados por el usuario
np = 0 
nn = 0
ni = 0
nf = int(input("Ingrese la cantidad de numeros a ingresar"))
for i in range(nf):
    print("Ingresé un número: ")
    x =  int(input())
    if x == 0:
        nn += 1
    elif x%2 == 0:
        np += 1
    elif x%2 == 1:   
        ni += 1

   
print("Hay" , ni, " números pares")
print("Hay" , nn, " números impares")
print("Hay" , np, " números nulos")


