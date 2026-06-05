turno = input("Turno (diurno/nocturno): ").lower()
horas = float(input("Horas trabajadas: "))
dia = input("Día de la semana: ").lower()

if turno == "diurno":
    tarifa = 5
    if dia == "domingo":
        tarifa += 2
elif turno == "nocturno":
    tarifa = 8
    if dia == "domingo":
        tarifa += 3
else:
    print("Turno no válido.")
    tarifa = 0

jornal = tarifa * horas
print(f"Jornal diario: {jornal} euros")