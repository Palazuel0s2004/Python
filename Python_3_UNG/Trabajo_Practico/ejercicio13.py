#13. Resultado de un examen
#Solicitar:
#• Nombre del estudiante;
#• cantidad total de preguntas;
#• cantidad de respuestas correctas.
#El programa deberá:
#• Calcular el porcentaje de respuestas correctas.
#• Indicar si el estudiante aprobó o reprobó.
#• Considerar aprobado al estudiante que alcance al menos el 60 %.
#• La cantidad de respuestas correctas no puede ser mayor que la cantidad total de pregunta

#While para escribir un nombre valido
while True:
        nombre = input("\nIngresa tu nombre: ").strip()
        #Elimina espacios en blanco al inicio y al final del nombre
        if nombre.replace(" ", "").isalpha() and len(nombre) > 0:
            break
        else:
            print("Error: Ingrese un nombre válido.")

#While para ingresar la cantidad de preguntas
while True:
    try:
        cant_preg = int(input("\nIngrese la cantidad de preguntas: "))
        if 0< cant_preg:
            print(f"Recibido, la cantidad de preguntas es: {cant_preg}")
            break
        else:
            print("Ingrese un numero mayor a 0")
    except ValueError:
        print("Error: Ingrese un número entero válido.")

while True:
    try:
        cant_aciertos = int(input("\nIngrese la cantidad de aciertos: "))
        if cant_aciertos>cant_preg:
            print("Error, la cantidad de aciertos no puede ser mayor a la cantidad de preguntas")
        elif cant_aciertos<0:
            print("Error, la cantidad de aciertos no puede ser menor a 0")
        else:
            break
    except ValueError:
        print("Error: Ingrese un número entero válido.")

#Calcular Porcentaje
porcentaje = (cant_aciertos / cant_preg) * 100

print("\n\tRESUMEN GENERAL")
print(f"Nombre del alumno: {nombre}")
print(f"Cantidad de preguntas: {cant_preg}")
print(f"Cantidad de aciertos: {cant_aciertos}")
print(f"Porcentaje de acertados: {porcentaje:.2f}%")
if porcentaje>=60:
    print("El estudiante ha aprobado")
else:
    print("El estudiante ha reprobado")

"""El código evalúa los resultados de un examen tomando el total de preguntas y los aciertos lo que
garantiza que las respuestas correctas no superen al total de preguntas ni sean negativas y
calcula la efectividad porcentual y asigna la aprobación al alcanzar el 60% mínimo exigido"""