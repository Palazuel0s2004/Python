#Ejercicio 1: Revisar Paréntesis Balanceados
#Problema: Un programador novato está escribiendo código y quiere verificar si los paréntesis ( y )
# están correctamente balanceados. Debe asegurarse de que:
#· Cada paréntesis que abre ( tiene su correspondiente que cierra )
#· Los paréntesis se cierran en el orden correcto
#Ejemplos:
#· Entrada: "(a + b)" → VÁLIDO
#· Entrada: "((a + b) * c)" → VÁLIDO
#· Entrada: "(a + b" → INVÁLIDO (falta cerrar)
#· Entrada: "a + b)" → INVÁLIDO (falta abrir)
#· Entrada: ")(" → INVÁLIDO (cierra antes de abrir)
#Pregunta: ¿Por qué conviene usar una PILA para este problema?

vector =[];hubo_parentesis = False ("Detector de parentesis");error_detectado = False ("Detector de errores");par = input("Ingrese la operacion: ")
#CIclo For
for i in par:
    #Abre parentesis
    if i=="(":
        vector.append("(");hubo_parentesis = True #Detecto el parentesis
    #Cierra parentesis
    elif  i==")":
        hubo_parentesis = True #Detecto el parentesis
        #Hay cierre sin apertura
        if len(vector) == 0:
            print("Invalido, falta abrir");rror_detectado = True #Detecto el error
        else:
            vector.pop() #Vacia el vector si encuentra un cierre
    
if not error_detectado: #Si no hubo error pasa el programa
    if not hubo_parentesis: #SI no hubo parentesis
        print("No se encontraron paréntesis en la operación.")
    elif len(vector) == 0:
        print("Operación válida.")
    else:
        print(f"Inválido: Faltan cerrar {len(vector)} paréntesis")