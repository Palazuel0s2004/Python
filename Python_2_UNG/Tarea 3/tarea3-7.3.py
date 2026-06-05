# Ejercicio L3: Buscar un Elemento
lista_enlazada = [10, 20, 30, 40, 25, 50]
objetivo = 25

def buscar_elemento(lista, numero):
    pasos = 0
    for elemento in lista:
        pasos += 1
        print(f"Paso {pasos}: ¿Es {elemento} igual a {numero}?")
        if elemento == numero:
            return pasos
    return pasos # Si no lo encuentra

saltos = buscar_elemento(lista_enlazada, objetivo)
print(f"\nEncontrado, necesito {saltos} pasos para hallar el {objetivo}")