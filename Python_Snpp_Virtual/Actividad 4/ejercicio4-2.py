#Escribir un programa que simule una calculadora y que contenga las siguientes funciones.
#1º) Muestre un menú con 5 opciones:
#1. Sumar dos números. ( Función Suma)
#2. Restar dos números. (Función Resta)
#3. Multiplicar dos números. (Función Multiplicación)
#4. Dividir dos números.(Función División)
#5. Salir.
#2º) Pida por teclado la opción deseada (dato carácter). Deberá ser introducida, mientras que, no sea mayor
# o igual que '1' y menor o igual que '5'.
#3º) Ejecute la opción seleccionada del menú.
#4º) Repita los pasos 1º, 2º y 3º, mientras que, el usuario no seleccione la opción 5 (Salir)del menú.

def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"
while True:
    print("\n--- Calculadora ---")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Salir")  
    opcion = input("Seleccione una opción (1-5): ") 
    if opcion == '5':
        print("Saliendo del programa...")
        break
    if opcion in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")
            continue
        if opcion == '1':
            print(f"Resultado: {suma(num1, num2)}")
        elif opcion == '2':
            print(f"Resultado: {resta(num1, num2)}")
        elif opcion == '3':
            print(f"Resultado: {multiplicacion(num1, num2)}")
        elif opcion == '4':
            print(f"Resultado: {division(num1, num2)}")
    else:
        print("Opción inválida. Intente de nuevo.")