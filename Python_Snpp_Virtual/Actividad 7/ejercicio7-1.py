def año_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False

año = int(input("Ingrese un año: "))
if año_bisiesto(año):
    print(f"{año} es bisiesto.")
else:
    print(f"{año} no es bisiesto.")