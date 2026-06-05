#Ejercicio 4: Convertir Número Decimal a Binario
#Problema: Escribe un programa que convierta un número decimal (entero positivo) a su representación
# en binario utilizando una pila.
#Método:
#· Divide el número entre 2 repetidamente
#· Guarda los residuos en una pila
#· Cuando el número sea 0, desapila los residuos para formar el binario
#Ejemplo:
#Número decimal: 13
#Proceso:
#13 ÷ 2 = 6, residuo 1 → apilar 1
#6 ÷ 2 = 3, residuo 0 → apilar 0
#3 ÷ 2 = 1, residuo 1 → apilar 1
#1 ÷ 2 = 0, residuo 1 → apilar 1
#Desapilar: 1 1 0 1
#Resultado binario: 1101
#Pregunta: ¿Por qué una PILA es perfecta para este algoritmo?
#Es perfecta porque el proceso matemático genera los dígitos en el orden inverso al que se escriben.
#Como la Pila es LIFO (Last In, First Out) al sacar los elementos estos salen en el orden correcto
# para formar el número binario.

bin = []
num = int(input("Ingrese un numero positivo: "))
orig = num
while num>0:
        res = num%2
        bin.append(res)
        num = num//2
print(f"La representacion binaria de {orig} es {bin}")
while len(bin) > 0:
    # Desapilado, se saca de la cima
    digito = bin.pop()
    print(digito, end=" ")

       
        


