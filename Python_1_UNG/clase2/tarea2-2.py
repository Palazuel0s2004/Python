#2.	Hacer un programa para ingresar dos números.Comparar si son distintos.
# Si son distintos al mayor sumarle el cuadrado del otro número, sino preguntar si es impar,
# si es impar calcular el doble de ambos y sumarlos, de no ser así sumar ambos números entre sí.
# Si son iguales multiplicar ambos números entre si. Imprimir el resultado. 

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num1 != num2:
    if num1 > num2:
        res_temp = num1+(num2**2)
    else:
        res_temp = num2+(num1**2)
    if res_temp%2 !=0:
        res = (num1*2)+(num2*2)
    else:
        res = num1+num2
else:
    res = num1*num2

     
print("El resultado es: ", res)
    