#11. Distancia recorrida
#Solicitar:
#• nombre del conductor;
#• velocidad en metros por segundo;
#• tiempo de recorrido en segundos.
#Calcular:
#• Distancia recorrida en metros.
#• Distancia recorrida en kilómetros.
#• Tiempo expresado en minutos.
#• La velocidad y el tiempo deben ser mayores que cero.
#• distancia = velocidad × tiempo

#While para el nombre para ingresar el nombre del conductor
while True:
    nombre = input("\nIngresa tu nombre: ").strip()
    #Elimina espacios en blanco al inicio y al final del nombre
    if nombre.replace(" ", "").isalpha() and len(nombre) > 0:
        break
    else:
        print("Error: Ingrese un nombre válido.")

#While para validar velocidad mayor a cero
while True:
    try:
        velocidad = float(input("\nIngrese la velocidad del vehículo (m/s): "))
        if velocidad > 0:
            break
        else:
            print("Ingrese un número válido (Mayor a cero)")
    except ValueError:
        print("Error: Ingrese un número numérico.")

#While para validar tiempo mayor a cero
while True:
    try:
        tiempo = float(input("\nIngrese el tiempo del recorrido en segundos: "))
        if tiempo > 0:
            break
        else:
            print("Ingrese un número válido (Mayor a cero)")
    except ValueError:
        print("Error: Ingrese un número numérico.")

#Variables para las formulas
distancia_metros = velocidad * tiempo
distancia_kilometros = distancia_metros / 1000
tiempo_minutos = tiempo / 60

print("\n\tRESUMEN GENERAL")
print(f"Nombre del conductor: {nombre}")
print(f"Velocidad en metros por segundo: {velocidad} m/s")
print(f"Tiempo recorrido en segundos: {tiempo} s")
print(f"Distancia recorrida en metros: {distancia_metros:.2f} m")
print(f"Distancia recorrida en kilómetros: {distancia_kilometros:.2f} km")
print(f"Tiempo expresado en minutos: {tiempo_minutos:.2f} min")

"""El código solicita los datos del conductor y la velocidad y tiempo, tambien valida que ambos
valores sean estrictamente mayores a cero para luego calcular la distancia
total en metros y aplicar las conversiones correspondientes a kilómetros y minutos"""