#7. Serie numérica personalizada con while
#Solicitar al estudiante:
#• Un número inicial.
#• Un número final.
#• Un incremento.
#• Utilizando exclusivamente un ciclo while, mostrar todos los números desde el valor
#inicial hasta el valor final.
#Además, el programa deberá:
#• Contar cuántos números fueron mostrados.
#• Calcular la suma de los números generados.
#• Contar cuántos son pares.
#• Contar cuántos son impares.
#• Mostrar el promedio de los números.
#• El incremento debe ser mayor que cero y el número final debe ser mayor que el inicial.

#While para el numero inicial
while True:
    try:
        num_ini = int(input("\nIngrese el numero inicial: "))
        break
    except ValueError:
        print("Error: Ingrese un número.")
        
#While para el numero final
while True:
    try:
        num_fin = int(input("\nIngrese el numero final: "))
        if num_fin > num_ini:
            break
        else:
            print(f"Ingrese un numero mayor al inicial {num_ini}")
    except ValueError:
        print("Error: Ingrese un número.")
        
#While para el incremento
while True:
    try:
        num_inc = int(input("\nIngrese el numero para el incremento: "))
        if num_inc>0:
            break
        else:
            print(f"Ingrese un numero mayor a cero")
    except ValueError:
        print("Error: Ingrese un número.")

#num es la variable para guardar la variable inicial
num = num_ini; num_most = 0; sum_num_most = 0; num_par = 0; num_impar = 0
#While para el ciclo de incremento
while num<=num_fin:
    #la variable num la hice para guardar el numero incrementado
    print(f"Numero incrementado: {num}")
    num_most+=1 #Contador de numeros mostrados
    sum_num_most+=num #Para sumar los numeros mostrados
    if num %2 == 0:
        num_par+=1 #Contador de numero par
    else:
        num_impar+=1 #Contador de numero impar
    num +=num_inc
    
        
promedio = sum_num_most / num_most #promedio de los numeros mostrados

print(f"La cantidad de números fueron mostrados son {num_most}")
print(f"La suma de los números generados es {sum_num_most}")
print(f"La cantidad de numeros pares es {num_par}")
print(f"La cantidad de numeros impares es {num_impar}")
print(f"El promedio de los números mostrados es {promedio}")

"""El algoritmo utiliza exclusivamente un ciclo while para generar una secuencia numérica progresiva
y valida que el incremento sea positivo y el fin supere al inicio y durante laiteración calcula la suma
conteo de pares e impares finalizando con el cálculo del promedio"""