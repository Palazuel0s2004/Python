#Ejercicio 1: Control de ventas diarias
#El programa debera procesar exactamente 3 ventas:
#Solicitar:
# -Nombre del vendedor
#Por cada venta ingresar:
# -Importe de la venta
#El programa debera:
# -Calcular el total vendido
# -Calcular cuantas ventas superan 1 millon de guaranies
# -Mostrar la venta mayor
# -Mostrar la venta menor
#El importe de cada venta debe ser mayor que 0

#Indicadores:
#Indicador                                                  #Puntaje
#Entrada y validacion de Datos                              2 puntos
#Uso correcto del ciclo                                     2 puntos
#Acumuladores y contadores                                  2 puntos
#Mayor y menor venta                                        2 puntos
#Salida correcta                                            2 puntos
#Total                                                      10 puntos


millon = 0
nombre = input("Ingrese el nombre del vendedor: ").strip()



#Venta1
while True:
    try:
        venta1 = float(input("Ingrese el importe de la primera venta: "))
        if venta1>0:
            if venta1>1000000:
                millon = millon + 1
            break
        else:
            print("Error, ingrese un monto mayor a 0")
    except ValueError:
        print("Error, ingrese un monto valido")

#Venta2
while True:
    try:
        venta2 = float(input("Ingrese el importe de la segunda venta: "))
        if venta2>0:
            if venta2>1000000:
                millon = millon + 1
            break
        else:
            print("Error, ingrese un monto mayor a 0")
    except ValueError:
        print("Error, ingrese un monto valido")

#Venta3
while True:
    try:
        venta3 = float(input("Ingrese el importe de la tercera venta: "))
        if venta3>0:
            if venta3>1000000:
                millon = millon + 1
            break
        else:
            print("Error, ingrese un monto mayor a 0")
    except ValueError:
        print("Error, ingrese un monto valido")


total_venta = venta1 + venta2 + venta3

mayor = venta1; menor = venta1

if venta2>mayor:
    mayor = venta2
if venta3>mayor:
    mayor = venta3

if venta2<menor:
    menor = venta2
if venta3<menor:
    menor = venta3



print("\tResumen General")
print("\nNombre del vendedor: ", nombre)
print("Total de las ventas: ", total_venta)
print("La cantidad de ventas que superan un millon es: ", millon)
print("La venta mayor es: ", mayor)
print("La venta menor es: ", menor)