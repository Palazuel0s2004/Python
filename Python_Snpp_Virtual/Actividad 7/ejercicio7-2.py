def divisores(num):
    if num <= 0:
        return []
    lista_div = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            lista_div.append(i)
    lista_div.append(num)
    return lista_div

numero = int(input("Escriba un número entero mayor que cero: "))
if numero > 0:
    resultado = divisores(numero)
    print(f"Los divisores de {numero} son {resultado}")
else:
    print("El número debe ser mayor que cero.")