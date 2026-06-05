#Usando una pila, verifica si una cadena que contiene los símbolos {, }, [, ], (, ) está correctamente balanceada. Debe cumplirse que por
#cada símbolo de apertura exista su correspondiente símbolo de cierre en el orden correcto.
#Ejemplos:
#• "{ [ ( ) ] }" → Balanceado
#• "{ [ ( ] ) }" → No balanceado (el ] cierra antes de que se cierre el ())
#• "{ [ } ]" → No balanceado
#• "()" → Balanceado
#• "(" → No balanceado

cadena = input("Ingrese la secuencia: ")
pila = []
# Diccionario: la clave es el cierre, el valor es la apertura
parejas = {')': '(', ']': '[', '}': '{'}

error = False
for caracter in cadena:
    if caracter in "([{":  # Si es de apertura
        pila.append(caracter)
    elif caracter in ")]}": # Si es de cierre
        # Si la pila está vacía o el último no coincide con su pareja
        if not pila or pila.pop() != parejas[caracter]:
            error = True
            break

if not error and not pila:
    print("¡Balanceado!")
else:
    print("No balanceado.")