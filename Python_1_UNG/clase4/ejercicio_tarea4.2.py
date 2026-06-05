cnm=0
cm=0
n=0
while True:
    n=int(input("ingrese un número cualquiera y 0 para terminar: "))
    if n==0:
        break
    if (n % 7 == 0 and n % 5 == 0):
        print(n, "  es multiplo de 5 y 7 ")
        cm=cm+1
    else:
        print(n, " no es multiplo")
        cnm=cnm+1

print ("el total de numeros que son multiplos de 5 y 7 es", cm)
print ("el total de numeros que no son multiplos de 5 y 7 es", cnm)
