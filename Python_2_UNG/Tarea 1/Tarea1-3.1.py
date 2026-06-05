#Implementa un TDA Pila en PSeInt que verifique el invariante después de cada operación.
#El programa debe:
#1. Permitir apilar, desapilar, ver cima y mostrar pila
#2. Después de cada operación, mostrar el estado del invariante:
# Mostrar valor de tope
# Verificar que 0 ≤ tope ≤ MAX
# Verificar que las posiciones 1..tope contienen elementos
#3. Incluir un mensaje de error si el invariante se rompe (esto no debería
#ocurrir si el código está bien)


vector = []
max=5;tope=0;i=0;cima=0;num=0 #tope es el contador, i esta de mas xd, cima es lo ultimo que se ingreso
# max es el limite del tope y num es la variable para la opcion que elegira el usuario

def fun2(): #Funcion para ver el estado de la Invariante (condicion que debe cumplirse siempre)
    print(f"ESTADO DEL INVARIANTE. El tope vale: {tope}")
    print("")
    if 0<=tope<=max and len(vector) == tope:
        print("La invariante esta intacta");print("");print(f"Invariante verificado: Tope={tope}, Rango 0...{max} aceptable.");print("")
    else:
        print("ERROR. La invariante se rompio, la estructura es inconsistente");print("")

def fun(): #Funcion para realizar los procedimientos pedidos en el ejercicio 
        global tope, num, vector
        if len(vector)==5 and num==1:
            print("Pila llena: ", vector);print("")   
        else:
        #Primer If
            if num==1 and tope<=5:
                vector.append(input("Elemento: "));print("")
                tope+=1
                print("Apilado correctamente");print("")
            #Segundo If
            if tope==0 and len(vector)==0 and num==2:
                print("Pila Vacia");print("")
            elif num==2 and tope<=5:
                tope-=1
                print("Desapilado: ", vector.pop());print("")
            #Tercero If
            if num==3:
                if tope==0:
                    print("Vacia");print("")
                else:
                    print("La pila actualmente es: ", vector);print("")
            #Cuarto If
            if num==4:
                if tope==0:
                    print("Vacia");print("")
                else:
                    print("La cima de la pila actualmente es: ", vector[-1]);print("")
            fun2()
#Ciclo para el cargado y verificacion de datos
while num<5 and tope<=5:
    print("1.Apilar | 2.Desapilar | 3.Mostrar | 4.Cima | 5.Salir");print("");num = int(input("Ingrese un numero: "));print("")
    if 1<= num <= 4:
        fun() #Llamada de Funcion
    elif num == 5:
        fun2() #Llamada de Funcion 2
        print("El proceso ha sido finalizadon. La pila queda asi: ", vector);print("")
    else:
        num = int(input("ERROR. Debe ingresar un numero del 1 al 5: "));print("")

        
        
        