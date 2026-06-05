#Ejercicio 3: Completar el Código de Pila
vector = []
max=5;tope=0;i=0;cima=0;num=0 #tope es el contador, i esta de mas xd, cima es lo ultimo que se ingreso
# max es el limite del tope y num es la variable para la opcion que elegira el usuario
#Interfaz
print("1. Apilar")
print("2. Desapilar")
print("3. Mostrar pila")
print("4. Salir")

#Ingreso de datos
while num<4 and tope<=5:
    num = int(input("Ingrese un numero: "))
    #if para verificar cantidad de elementos del vector y el valor del numero ingresado
    if len(vector)==5 and num==1:
        print("Pila llena: ", vector)   
    else:
    #Primer If, verifica el numero
        if num==1 and tope<=5:
            vector.append(input("Elemento: "))
            tope+=1
            print("Apilado correctamente")
        #Segundo If
        if tope==0 and len(vector)==0 and num==2:
            print("Pila Vacia")
        elif num==2 and tope<=5:
            tope-=1
            print("Desapilado: ", vector.pop())
        #Tercero If
        if num==3:
            if tope==0:
                print("Vacia")
            else:
                print("La pila actualmente es: ", vector)
        #Cuarto If
        if num==4:
            print("El proceso ha sido finalizadon. La pila queda asi: ", vector)
    
