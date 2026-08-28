#4. Comparación de 3 números
#Solicitar tres números enteros diferentes o iguales.
#El programa deberá:
#• Determinar cuál es el mayor.
#• Determinar cuál es el menor.
#• Informar si existen dos números iguales.
#• Informar si los tres números son iguales.
#• Calcular la diferencia entre el número mayor y el menor.


#Try y except estan para que el usuario ponga exclusivamente numeros
while True:
    try:
        num1 = int(input("Ingrese el primer número: "))
        break
    except ValueError:
        print("Error: Ingrese un número entero válido.\n")
while True:
    try:
        num2 = int(input("Ingrese el segundo número: "))
        break
    except ValueError:
        print("Error: Ingrese un número entero válido.\n")
while True:
    try:
        num3 = int(input("Ingrese el tercer número: "))
        break
    except ValueError:
        print("Error: Ingrese un número entero válido.\n")
    
#Definicion del numero mayor y menor
mayor = num1
menor = num1
    
#Bloque de if de mayor
if num2 > mayor:
    mayor = num2
if num3 > mayor:
    mayor = num3

#Bloque de if de menor
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3
    
#Bloque de comparaciones
if num1 == num2 and num2 == num3:
    iguales = "Todos los números son iguales"   
elif num1 == num2:
    iguales = f"El primer número ({num1}) y el segundo número ({num2}) son iguales"
elif num1 == num3:
    iguales = f"El primer número ({num1}) y el tercer número ({num3}) son iguales"
elif num2 == num3:
    iguales = f"El segundo número ({num2}) y el tercer número ({num3}) son iguales"
else:
    iguales = "Ninguno de los tres números son iguales"

print("="*40)
print("\tRESULTADO FINAL")
print("="*40)
print("El numero mayor es: ", mayor)
print("El numero menor es: ", menor)
print(iguales)
#Bloque de diferencia
diferencia = mayor - menor
if diferencia!=0:
    print("La diferencia entre el mayor y menor es de: ", diferencia)
else:
    print("Los numeros son iguales por ende no hay diferencia")
print("-"*40)

"""El programa captura tres números enteros asistido por control de excepciones tryexcept y
utiliza condicionales para comparar los 3 numeros detectando si existen numeros
iguales o si los 3 son iguales, para luego calcular la diferencia entre mayor y menor"""