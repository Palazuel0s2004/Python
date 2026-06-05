#Ejercicio 9: Buffer de Teclado
#Problema:
#Simula el comportamiento de un buffer de teclado. Cuando el usuario escribe rápido, las teclas se almacenan temporalmente y
# luego el sistema las procesa en el mismo orden en que fueron presionadas.
#El programa debe permitir:
#· Presionar tecla (agregar carácter al buffer)
#· Procesar tecla (tomar el primer carácter del buffer)
#· Mostrar buffer actual
#· Vaciar buffer
#Ejemplo:
#``` Tecla presionada: H
#Tecla presionada: O
#Tecla presionada: L
#Tecla presionada: A
#Buffer: H O L A
#Procesando: H
#Buffer: O L A
#Procesando: O
#Buffer: L A```
#Pregunta: ¿Por qué una COLA es ideal para simular un buffer?

buffer = []
while True:
    try:
        tecla = input("Ingrese una palabra (Enter vacio para finalizar): ");print("")
        if tecla == "":
            break
        else:
            for i in tecla:
                buffer.append(i)
                print("Tecla presionada: ", i);print("")
        print("Buffer: ", buffer)
        while len(buffer) > 0:
            print("Procesando: ", buffer.pop(0));print("Buffer: ", buffer)
    except ValueError:
        print("Ingrese una palabra valida");print("")