#Ejercicio 2: Historial de Navegación Web
#Problema: Simula el comportamiento del botón "Atrás" de un navegador web.
# El usuario visita páginas web y puede:
#· Visitar una nueva página (se agrega al historial)
#· Regresar a la página anterior (botón Atrás)
#· Ver la página actual (sin modificar el historial)
#Ejemplo de uso:
#Usuario visita: "google.com"
#Usuario visita: "youtube.com"
#Usuario visita: "github.com"
#Usuario presiona Atrás → Ahora está en "youtube.com"
#Usuario presiona Atrás → Ahora está en "google.com"
#Usuario visita: "facebook.com" → Ahora está en "facebook.com" (no puede ir adelante a github)
#Pregunta: ¿Por qué una PILA es ideal para simular el historial de navegación?
#Porque el historial debe ser un retroceso ordenado

historial = []
rev = []
while True:
    print("--- MENU PRINCIPAL ---");print("");print("1. Ingresar en sitio web | 2. Regresar a la pagina anterior | 3. Mostrar historial | 4. Salir ")
    sit = int(input(" "));print("")
    #Ingreso de sitio web
    if sit == 1:
        historial.append(input("Ingrese la pagina web: "));print("");print("Usuario visita: ", historial[-1]);print("")
    #Regresar a la pagina anterior
    elif sit == 2:
        if len(historial) == 1:
            print("Solo hay un elemento en la lista")       
        elif len(historial) > 0:
            rev.append(historial.pop());print("Volviendo a la pagina anterior: ", historial[-1])
        else:
            print("No hay elementos cargados")
    #Mostrar historial
    elif sit == 3:
        print("Historial: ", historial)
    #Salir del programa
    elif sit == 4:
        print("Historial final: ", historial);break
    else: 
        print("Elija una opcion valida")