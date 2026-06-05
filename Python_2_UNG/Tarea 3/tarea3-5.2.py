#Ejercicio D2: Agenda Telefónica
#Queremos una agenda que guarde nombres y números de teléfono. Implementa un pequeño programa que realice lo siguiente:
#1. Añade los siguientes contactos:
#o "Ana" -> "555-1234"
#o "Luis" -> "555-5678"
#o "Sofia" -> "555-9012"
#2. Muestra el número de Luis.
#3. Ana cambió de número. Actualiza su registro a "555-4321".
#4. Muestra todos los contactos y sus números (recorre el diccionario e imprime cada par).
#5. Elimina el contacto de Sofia.
#6. Intenta buscar a Sofia nuevamente. Muestra un mensaje indicando que no se encontró.

agenda = {"Ana":"555-1234", "Luis":"555-5678", "Sofia":"555-9012"}

print("El número de Luis es:", agenda["Luis"])

agenda["Ana"] = "555-4321"

print("\t--- Lista de contactos actualizada ---")
#.items() da el 'nombre' y el 'numero' en cada vuelta del bucle
for nombre, numero in agenda.items():
    print(f"Contacto: {nombre} | Teléfono: {numero}")

del agenda["Sofia"]

print("\t--- Verificando eliminación de Sofia ---")
if "Sofia" in agenda:
    print("Número de Sofia:", agenda["Sofia"])
else:
    print("Mensaje: El contacto de Sofia no se encontró.")