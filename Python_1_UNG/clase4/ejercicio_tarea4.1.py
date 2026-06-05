puntos = 0
while True:
    print("Ingresa el puntaje de tu examen")
    puntos = int(input())
    if puntos == 0:
        break
    if puntos >= 1 and puntos <=20 : 
       print("Reprobado")
    elif puntos >= 21 and puntos <=30:
       print("Aceptable")
    elif puntos >= 31 and puntos <=40: 
       print("Bueno")
    elif puntos >=41 and puntos <=50:
        print("Muy Bueno")
    elif puntos >= 51 and puntos <=60 : 
        print("Excelente")
    else: 
        print("no haz ingresado un numero correcto")
    