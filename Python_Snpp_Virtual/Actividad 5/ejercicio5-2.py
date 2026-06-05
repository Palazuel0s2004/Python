#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y
# Lengua, Castellano, Geología, Educación Física, etc.) en una lista.
#- Las materias deben insertarse por el método append o insert mediante un input.
#- Demostrar el método pop() o remove() eliminando un elemento de la lista.
#- Recorrer la lista y mostrar en pantalla todos los elementos de la lista
#(“Asignatura:”,listaAsignatura[i]) por cada asignatura de la lista.
#Resultado ejemplo:
#Asignatura: Matemáticas
#Asignatura: Física
#Asignatura: Química
#Asignatura: Historia y Lengua….

asignaturas = []

print("Ingrese las asignaturas del curso (escriba 'fin' para terminar):")
while True:
    materia = input("Asignatura: ")
    if materia.lower() == 'fin':
        break
    asignaturas.append(materia)

print("\nLista de asignaturas:", asignaturas)

eliminar = input("\nIngrese una asignatura a eliminar: ")
if eliminar in asignaturas:
    asignaturas.remove(eliminar)
    print(f"'{eliminar}' eliminada.")
else:
    print("Asignatura no encontrada.")

print("\n--- Lista final de asignaturas ---")
for asig in asignaturas:
    print(f"Asignatura: {asig}")