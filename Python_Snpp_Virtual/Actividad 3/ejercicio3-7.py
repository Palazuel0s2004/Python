# Dadas 6 notas, escribir la cantidad de alumnos aprobados y los no aprobados. (Aprobados mayores a 1)
# (No aprobados menor o igual a 1)

aprobados = 0
no_aprobados = 0

for i in range(6):
    nota = float(input(f"Ingrese la nota del alumno {i+1}: "))
    if nota > 1:
        aprobados += 1
    else:
        no_aprobados += 1

print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos no aprobados: {no_aprobados}")