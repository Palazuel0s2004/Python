def factorial(n):
    if n < 0:
        return "No existe factorial de números negativos."
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

num = int(input("Ingrese un número para calcular su factorial: "))
print(f"Factorial de {num} = {factorial(num)}")