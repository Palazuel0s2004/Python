#VECTORES DINÁMICOS (Dynamic Arrays)
#Ejercicio V1: Gestión de Notas de Estudiantes
#Tenemos un vector dinámico que almacena las notas de los exámenes de un estudiante. Realiza las siguientes operaciones y muestra el vector después de
#cada una:
#1. Crear un vector vacío llamado notas.
#2. Añadir las siguientes notas al final: 85, 90, 78.
#3. Mostrar la nota que está en la posición 1 (recuerda que la primera posición suele ser índice 0).
#4. Insertar una nueva nota, 88, en la posición 1 (entre 85 y 90).
#5. Añadir una nota más al final: 95.
#6. Eliminar la nota que está en la posición 2.
#7. Mostrar la nota que está en la posición 0.

notas = []
print(f"Paso 1 (Vacío): {notas}")

notas.append(85)
notas.append(90)
notas.append(78)
print(f"Paso 2 (Añadir 85, 90, 78): {notas}")

print(f"Paso 3 (Nota en posición 1): {notas[1]}")

notas.insert(1, 88)
print(f"Paso 4 (Insertar 88 en pos 1): {notas}")

notas.append(95)
print(f"Paso 5 (Añadir 95 al final): {notas}")

nota_eliminada = notas.pop(2)
print(f"Paso 6 (Eliminar pos 2 - era el {nota_eliminada}): {notas}")

print(f"Paso 7 (Nota en posición 0): {notas[0]}")