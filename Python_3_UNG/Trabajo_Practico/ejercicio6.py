#6. Tiempo y punto de encuentro de dos móviles
#Dos móviles se desplazan en línea recta, uno hacia el otro.
#Solicitar:
#• Distancia inicial entre los móviles, en kilómetros.
#• Velocidad del primer móvil, en kilómetros por hora.
#• Velocidad del segundo móvil, en kilómetros por hora.
#• Nombre del lugar desde donde parte cada móvil.
#El programa deberá calcular:
#• El tiempo que tardarán en encontrarse.
#• La distancia recorrida por cada móvil.
#• El punto aproximado donde se encontrarán, medido desde el lugar de partida del primer móvil.
#• El tiempo expresado en horas y minutos.
#• El programa deberá validar que la distancia y las velocidades sean mayores que cero.

#While para ingresar la distancia inicial entre los moviles
while True:
    try:
        distancia_inicial = float(input("\nIngrese la distancia inicial: "))
        if distancia_inicial > 0:
            break
        else:
            print("Ingrese un numero mayor a cero")
    except ValueError:
        print("Ingrese un numero valido")

while True:
    #Try para pedir la velocidad del primer vehiculo
    try:
        vel_movil1 = float(input("\nIngrese la velocidad del primer movil: "))
        if vel_movil1 > 0:
            break
        else:
            print("Ingrese un numero mayor a cero")
    except ValueError:
        print("Ingrese un numero valido")

#Nombre de donde parte el movil 1
while True:
    nom_movil1 = input("\nIngresa el nombre del lugar de partida del móvil 1: ").strip()
    if nom_movil1.replace(" ", "").isalpha() and len(nom_movil1) > 0:
        break
    else:
        print("Error: Ingrese un nombre válido.")

while True:
    #Try para pedir la velocidad del segundo vehiculo
    try:
        vel_movil2 = float(input("\nIngrese la velocidad del segundo movil: "))
        if vel_movil2 > 0:
            break
        else:
            print("Ingrese un numero mayor a cero")
    except ValueError:
        print("Ingrese un numero valido")

#Nombre de donde parte el movil 2
while True:
    nom_movil2 = input("\nIngresa el nombre del lugar de partida del móvil 2: ").strip()
    if nom_movil2.replace(" ", "").isalpha() and len(nom_movil2) > 0:
        break
    else:
        print("Error: Ingrese un nombre válido.")

tiempo_encuentro = distancia_inicial / (vel_movil1 + vel_movil2)
dist_movil1 = vel_movil1 * tiempo_encuentro
dist_movil2 = vel_movil2 * tiempo_encuentro

print("La distancia recorrida del movil 1 es: ", dist_movil1)
print("La distancia recorrida del movil 2 es: ", dist_movil2)
print(f"El punto aproximado donde se encontraron medido desde {nom_movil1} es: ", dist_movil1)

hor = int(tiempo_encuentro)
minu = int((tiempo_encuentro - hor) * 60) 
if minu > 0:
    if hor == 0:
        if minu == 1:
            print(f"\nEl tiempo que tardan en encontrarse fue de {minu} minuto")
        elif minu > 1:
            print(f"\nEl tiempo que tardan en encontrarse fue de {minu} minutos")
    elif hor == 1:
        if minu == 1:
            print(f"\nEl tiempo que tardan en encontrarse fue de {hor} hora y {minu} minuto")
        elif minu > 1:
            print(f"\nEl tiempo que tardan en encontrarse fue de {hor} hora y {minu} minutos")
    else:
        print(f"\nEl tiempo que tardan en encontrarse fue de {hor} horas y {minu} minutos")
else:
    if tiempo_encuentro == 1:
        print(f"\nEl tiempo que tardan en encontrarse fue de {int(tiempo_encuentro)} hora")
    elif tiempo_encuentro > 1:
        print(f"\nEl tiempo que tardan en encontrarse fue de {int(tiempo_encuentro)} horas")

"""Se implementan fórmulas cinemáticas para calcular el tiempo de encuentro de dos móviles y la
distancia recorrida por cada uno. Valida que las velocidades y la distancia sean mayores a cero
y convierte el resultado del tiempo a formato de horas y minutos"""