#Usando una pila, verifica si una cadena que contiene los símbolos {, }, [, ], (, ) está correctamente balanceada. Debe cumplirse que por
#cada símbolo de apertura exista su correspondiente símbolo de cierre en el orden correcto.
#Ejemplos:
#• "{ [ ( ) ] }" → Balanceado
#• "{ [ ( ] ) }" → No balanceado (el ] cierra antes de que se cierre el ())
#• "{ [ } ]" → No balanceado
#• "()" → Balanceado
#• "(" → No balanceado

vector = []
error_detectado = False
hubo_simbolos = False
# Diccionario para saber quién es pareja de quién
# Facilita verificar si el cierre es correcto
parejas = {")": "(", "]": "[", "}": "{"}
while True:
    cadena = input("Ingrese la operacion: ")
    for i in cadena:
        # 1. Si es un símbolo de apertura se apilara
        if i in "( [{":
            vector.append(i)
            hubo_simbolos = True
        # 2. Si es un símbolo de cierre
        elif i in ") ]}":
            hubo_simbolos = True
            # Error: Si intenta cerrar algo pero la pila está vacía
            if len(vector) == 0:
                print(f"Inválido: El símbolo '{i}' no tiene apertura.")
                error_detectado = True
                break
            else:
                # Verificam si el que vamos a sacar es la pareja correcta del símbolo actual
                ultimo_abierto = vector.pop()
                if ultimo_abierto != parejas[i]:
                    print(f"Inválido: Se intentó cerrar '{i}' pero el último abierto fue '{ultimo_abierto}'")
                    error_detectado = True
                    break
    # Verificación final
    if not error_detectado:
        if not hubo_simbolos:
            print("No se encontraron símbolos de agrupación.")
            break
        elif len(vector) == 0:
            print("Balanceado correctamente.")
            break
        else:
            print(f"Inválido: Quedaron {len(vector)} símbolos sin cerrar: {vector}")
            print("Ingrese una operacion valida")