#Ejercicio 12: Editor de Texto Simple
#Problema:
#Simula un editor de texto muy simple con dos funcionalidades:
#· Escribir caracteres: se agregan al final del texto (cola)
#· Deshacer última acción: elimina el último carácter escrito (pila de cambios)
#El programa debe:
#· Permitir escribir caracteres uno por uno
#· Permitir deshacer el último carácter
#· Mostrar el texto actual
#· Mostrar la pila de cambios (para depuración)
#Ejemplo:
#```Escribir: H → Texto: H
#Escribir: O → Texto: HO
#Escribir: L → Texto: HOL
#Escribir: A → Texto: HOLA
#Deshacer → Texto: HOL
#Deshacer → Texto: HO```
#Pregunta: ¿Qué estructura usas para el texto actual y qué estructura para deshacer? ¿Por qué?

texto = []
historial_deshacer = []
while True:
    try:
        print(f"Texto actual: {texto}")
        print("1. Escribir letra | 2. Deshacer | 3. Salir")
        opc = input("Seleccione: ")
        if opc == "1":
            letra = input("Letra: ")
            texto.append(letra)
            historial_deshacer.append(letra) # Guardamos la acción
        elif opc == "2":
            if len(texto)>0:
                accion = historial_deshacer.pop() # Sacamos la última acción (LIFO)
                texto.pop() # Eliminamos del texto
                print(f"Se deshizo: {accion}")
            else:
                print("No hay elementos en la pila")
        elif opc == "3": break
        else:
            ("Ingrese una opcion valida")
    except ValueError:
        print("Ingrese una opcion valida")