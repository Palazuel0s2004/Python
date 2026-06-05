#1.	Realiza un programa para calcular el cuadrado de un numero si es impar,
# caso contrario halla el doble del numero si es mayor o igual a 50,
# caso contrario calcular la división entera de dicho número. Imprimir el resultado final. 

num = int(input("Ingrese un numero: "))

if num % 2 != 0:
    res = num ** 2
elif num >= 50:  
    res = num * 2
else:            
    res = num // 2
    
print("Resultado final:", res)
