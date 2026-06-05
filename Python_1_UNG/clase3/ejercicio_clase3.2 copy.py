#EJERCICIO 2
#Una entidad financiera desea realizar una calculadora de préstamo.
#El oficial de cuenta debe ingresar el préstamo otorgado y
#el tipo de préstamo (1 = ordinario, 2 = emergencia, 3= extraordinario).
#El sistema debe terminar cuando el oficial ingrese 0 como tipo de préstamo (fin del día).
#Se debe calcular:
#1. La suma total de los prestamos desde 1.000.000 y 15.000.000.
#2. El promedio de préstamos que sean menores a 50.000.000.
#3. La cantidad de préstamos extraordinarios mayores a 30.000.000
#4. La cantidad de préstamos emergencia.
#5. El monto total de préstamos otorgado en el día.

prest = 0 #monto del prestamo
tipo = 0 #tipo de prestamo
ord = 0 #prestamo ordinario
emer = 0 #prestamo de emergencia
ext = 0 #prestamo extraordinario
sum = 0 #suma de los prestamos de entre 1.000.000 y 15.000.000
sum_cont = 0 #suma de menores a 50 millones
prom = 0 #promedio de préstamos que sean menores a 50.000.000
cont = 0 #contador de promedio
sum_tot = 0 #suma del monto total de préstamos otorgado en el día

while True:
    prest = int(input("Ingrese el monto del prestamo: "))
    if prest == 0:
        break
    sum_tot += prest
    if prest<50000000:
        cont += 1
        sum_cont += prest
    prom = sum_cont/cont
    if prest>=1000000  and prest<=15000000:
            sum += prest
    while True:
        tipo = int(input("Ingrese el tipo de prestamo 1-Ordinario, 2-Emergencia, 3-Extraordinario: "))
        if tipo == 2:
            emer += 1
        if tipo >= 1 and tipo <= 3:
            break
        else:
            print("Ingrese un numero valido por favor")
    if tipo == 3 and prest>30000000:
        ext += 1
  
print("La suma total de los prestamos desde 1.000.000 y 15.000.000 es de: ",sum)
print("El promedio de préstamos que sean menores a 50.000.000: ",prom)
print("La cantidad de préstamos extraordinarios mayores a 30.000.000: ",ext)
print("La cantidad de préstamos emergencia: ", emer)
print("El monto total de préstamos otorgado en el día: ",sum_tot)