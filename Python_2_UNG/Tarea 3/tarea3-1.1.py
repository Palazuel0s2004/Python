#Simula el comportamiento del botón "Atrás" de un navegador. Cuando visitas una página nueva, esta se añade a una pila de historial.
# Al presionar "Atrás", se muestra la página anterior (la que está en la cima) y se elimina de la pila.
#Instrucciones:
#1. Crea una pila vacía llamada historial.
#2. Simula que visitas las siguientes páginas en orden: "google.com", "youtube.com", "facebook.com", "twitter.com". Muestra el estado 
# de la pila después de cada visita.
#3. Simula que el usuario presiona el botón "Atrás" dos veces seguidas. Después de cada presión, muestra qué página se visitó (la que se desapiló)
# y el nuevo estado de la pila.

historial = []; atras = []

while True:
    print("\t----- NAVEGADOR -----");print("")
    print("Elija un de las opciones");print("")
    print("1.Visitar un sitio web | 2.Regresar al sitio anterior | 3.Mostrar historial | 4.Salir");print("")
    opc = int(input());print("")
    #Ingreso de sitio web
    if opc == 1:
        historial.append(input("Ingrese el sitio web: "));print("")
        print(f"Visitando pagina {historial[-1]}");print("")
        print(f"Historial actual: {historial}");print("")
    #Regresar a la pagina anterior
    elif opc == 2:
        if len(historial) == 1:
            print("Solo hay una pagina visitada");print("")
        elif len(historial) == 0:
            print("No hay sitios en el historial");print("")
        else:
            rev = historial.pop()
            atras.append(rev)
            print(f"Saliendo de la pagina {rev}");print("")
            print("Volviendo a la pagina", historial[-1]);print("")
            print(f"Historial actual: {historial}");print("")
        #Mostrar historial
    elif opc == 3:
        print("Historial: ", historial);print("")
    #Salir del programa
    elif opc == 4:
        print("Historial final: ", historial);print("");break
    else: 
        print("Elija una opcion valida");print("")
        
