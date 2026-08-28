#1. Operaciones con tus datos personales
#Solicitar los siguientes datos:
#• Nombre y Apellido. (Tu nombre y apellido)
#• Dia de nacimiento. (numérico corresponde a tu cumpleaños)
#• Mes de nacimiento. (numérico)
#• Dos últimos dígitos de tu año de nacimiento.
#Con los tres últimos valores, el programa deberá:
#• Calcular la suma de los tres números.
#• Multiplicar el día por el mes.
#• Restar al año de nacimiento la suma del día y el mes.
#• Calcular el promedio de los tres valores.
#• Indicar cuál de los tres números es el mayor y cuál es el menor.
#• Mostrar un mensaje si dos o más valores son iguales.

#While para el nombre para que el usuario ingrese un nombre válido
while True:
        nombre = input("\nIngresa tu nombre: ").strip()
        #Elimina espacios en blanco al inicio y al final del nombre
        if nombre.replace(" ", "").isalpha() and len(nombre) > 0:
            print(f"¡Nombre válido! Bienvenido/a, {nombre.title()}.") #Para poner la priemra letra en mayuscula
            break
        else:
            print("Error: Ingrese un nombre válido.")
#While para el apellido para que el usuario ingrese un apellido válido
while True:
        apellido = input("\nIngrese su apellido; ").strip()
        #Elimina espacios en blanco al inicio y al final del apellido
        if apellido.replace(" ", "").isalpha() and len(apellido) > 0:
            print(f"¡Apellido válido! Bienvenido/a, {nombre.title()} {apellido.title()}.") #Para poner la priemra letra en mayuscula
            break
        else:
            print("Error: Ingrese un apellido válido.")
while True:
    try:
        dia_nac = int(input("\nIngrese su fecha de nacimiento (En numero): "))
        if 1 <= dia_nac <= 31:
            print(f"¡Fecha de nacimiento válida!")
            break 
        else:
            print("Error: El día debe estar entre 1 y 31.")
    except ValueError:
        print("Error: Ingrese un día de nacimiento válido.")
while True:
    try:
        mes_nac = int(input("\nIngrese su mes de nacimiento (En numero): "))
        if 1 <= mes_nac <= 12:
            print(f"¡Mes de nacimiento válido!")
            break
        else:
            print("Error: El mes debe estar entre 1 y 12.")
    except ValueError:
        print("Error: Ingrese un mes de nacimiento válido.")
while True:
    try:
        año_nac = int(input("\nIngrese los dos últimos dígitos de su año de nacimiento: "))
        if 0 <= año_nac <= 99:
            print(f"¡Año de nacimiento válido!")
            break
        else:
            print("Error: El año debe estar entre 0 y 99.")
    except ValueError:
        print("Error: Ingrese un año de nacimiento válido.")

print("")
print("="*40)
print(f"\tBIENVENIDO/A {nombre.title()} {apellido.title()}")
print("="*40)
print(f"Su fecha de nacimiento es: {dia_nac}/{mes_nac}/{año_nac}")
print("-"*40)
print("La suma de los tres ultimos valores es: ", dia_nac + mes_nac + año_nac)
print("La multiplicación del dia por el mes es: ", dia_nac * mes_nac)
print("La resta del año de nacimiento con la suma del día y el mes da: ", año_nac - (dia_nac+mes_nac))
print("El promedio de los tres valores es: ", (dia_nac+mes_nac+año_nac)/3)
#Definicion del numero mayor y menor
mayor = dia_nac
menor = dia_nac
    
#Bloque de if de mayor
if mes_nac > mayor:
    mayor = mes_nac
if año_nac > mayor:
    mayor = año_nac

#Bloque de if de menor
if mes_nac < menor:
    menor = mes_nac
if año_nac < menor:
    menor = año_nac
    
#Bloque de comparaciones
if dia_nac == mes_nac and mes_nac == año_nac:
    iguales = "Todos los números son iguales"   
elif dia_nac == mes_nac:
    iguales = f"La fecha de nacimiento ({dia_nac}) y el mes de nacimiento ({mes_nac}) son iguales"
elif dia_nac == año_nac:
    iguales = f"La fecha de nacimiento ({dia_nac}) y el año de nacimiento ({año_nac}) son iguales"
elif mes_nac == año_nac:
    iguales = f"El mes de nacimiento ({mes_nac}) y el año de nacimiento ({año_nac}) son iguales"
else:
    iguales = "Ninguno de los tres números son iguales"
    
print("El numero mayor es: ", mayor)
print("El numero menor es: ", menor)
print(iguales)

"""El programa solicita el nombre, apellido y datos de nacimiento del estudiante validando cada entrada mediante ciclos while y
bloques try except para evitar valores negativos o fuera del rango de días y meses, tambien ejecuta los cálculos pedidos
y verifica cual valor es mayor y menor, tambien tiene condicionales para comparar los valores e identificar igualdades"""