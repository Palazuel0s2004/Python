#Ejercicio D1: Traductor Simpĺe
#Crea un diccionario que sirva como traductor de español a inglés. Añade las
#siguientes palabras y sus traducciones:
#• "perro" -> "dog"
#• "gato" -> "cat"
#• "casa" -> "house"
#• "coche" -> "car"
#Instrucciones:
#1. Crea el diccionario traductor.
#2. Añade los pares clave-valor.
#3. Busca y muestra la traducción de "gato".
#4. Busca y muestra la traducción de "casa".
#5. Intenta buscar la palabra "pájaro". ¿Qué ocurre? ¿Cómo manejarías ese caso?

dic = {"perro":"dog","gato":"cat", "casa":"house","coche":"car"}

pal = input("Ingrese una palabra: ").lower()

if pal in dic:
    print(f"Palabra ingresada: {pal} | Traduccion: {dic[pal]}");print("")
    traduccion = dic[pal]
    print(f"La traducción de {pal} es {traduccion}")
else:
    print(f"La palabra '{pal}' no está en el diccionario")