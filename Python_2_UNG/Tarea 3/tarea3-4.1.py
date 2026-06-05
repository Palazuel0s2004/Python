#Ejercicio B1: Encuesta de Colores Favoritos
# Se realizó una encuesta preguntando el color favorito a un grupo de personas.
# Las respuestas fueron: Rojo, Azul, Rojo, Verde, Azul, Azul, Rojo, Amarillo.
#Instrucciones:
#1. Representa esta encuesta como una Bolsa (recuerda, permite duplicados y queremos contar frecuencias).
# 2. Determina cuántas personas votaron por cada color usando la operación contar(color).
#3. Imprime un resumen como: "Rojo: 3, Azul: 3, Verde: 1, Amarillo: 1"

from collections import Counter
colores = []

while True:
    try:
        print("\t-----CUAL ES TU COLOR FAVORITO-----")
        print("1.Rojo | 2.Amarillo | 3.Verde | 4.Azul | 5.Salir");print("")
        c = int(input())
        if c == 1:
            colores.append("Rojo")
        elif c == 2:
            colores.append("Amarillo")
        elif c == 3:
            colores.append("Verde")
        elif c == 4:
            colores.append("Azul")
        elif c == 5:
            total = Counter(colores)
            resumen = []
            for color, cantidad in total.items():
                resumen.append(f"{color}: {cantidad}")
                
            resultado_final = ", ".join(resumen)
            print(f"Resumen de las votaciones: {resultado_final}")
            break
        else:
            print("Ingrese una opcion valida")
    except ValueError:
        print("Ingrese una opcion valida")

