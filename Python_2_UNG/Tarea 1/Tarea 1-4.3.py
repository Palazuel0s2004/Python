#Convertir Especificación a Implementación
#Dada la siguiente especificación del TDA "Bolsa"
# (colección sin orden donde se pueden agregar y quitar elementos, pero no importa cuál se quite):

max = 5
bolsa = []
opc = 0

def messi():
    print("Bolsa actual:", bolsa);print("")
    print(f"ESTADO DEL INVARIANTE: 0 <= {len(bolsa)} <= {max}");print("")
    if 0 <= len(bolsa) <= max:
        print("Invariante OK");print("")
    else:
        print("ERROR: Invariante roto");print("")

while True:
    print("1. Agregar | 2. Sacar | 3. Salir");print("");opc = int(input("Opcion: "));print("")
    
    if opc == 1:
        if len(bolsa) < max:
            bolsa.append(input("Elemento a la bolsa: "));print("");print("Agregado.");print("")
        else:
            print("Bolsa llena");print("")
            
    elif opc == 2:
        if len(bolsa) > 0:
            print("Sacaste:", bolsa.pop());print("")
        else:
            print("Bolsa vacia");print("")   
    elif opc == 3:
        messi()
        break
    messi()   