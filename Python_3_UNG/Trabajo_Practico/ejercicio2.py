#2. Clase Alumno y evaluación académica (Probar con tus datos personales)
#Crear una clase llamada Alumno con los siguientes atributos:
#• Nombre y apellido del estudiante.
#• Número de cédula.
#• Primera nota.
#• Segunda nota.
#• Tercera nota.
#Implementar métodos para:
#• Inicializar los atributos.
#• Calcular el promedio de las tres notas.
#• Mostrar todos los datos del alumno.
#Indicar su situación académica de acuerdo con la siguiente escala:
#• Promedio menor que 2: Reprobado.
#• Promedio desde 2 hasta menos de 3: Debe rendir recuperación.
#• Promedio desde 3 hasta 5: Aprobado.
#Las notas deben estar comprendidas entre 1 y 5. Si alguna nota no pertenece a ese rango, el
#programa deberá mostrar un mensaje de error.


#Clase de Alumno
class Alumno:
    def __init__(self, nombre, apellido, cedula, nota1, nota2, nota3):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
    #Funcion para calcular promedio
    def calcular_promedio(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3
    #Funcion del mensaje de retorno
    def situacion_academica(self):
        prom = self.calcular_promedio()
        if prom < 2:
            return "Reprobado"
        elif 2 <= prom < 3:  
            return "Debe rendir recuperación"
        elif 3 <= prom <= 5:
            return "Aprobado"
    #Funcion para mostrar los datos
    def mostrar_datos(self):
        print("\n\tResultado Final")
        print(f"Nombre completo: {self.nombre} {self.apellido}")
        print(f"Cedula: {self.cedula}")
        print(f"Nota 1: {self.nota1}")
        print(f"Nota 2: {self.nota2}")
        print(f"Nota 3: {self.nota3}")
        print(f"Promedio: {self.calcular_promedio():.2f}")
        print(f"Situación: {self.situacion_academica()}")

#Variables para datos personales del alumno
nombre = input("\nIngrese el nombre del alumno: ").strip()
apellido = input("\nIngrese el apellido del alumno: ").strip()
cedula = input("\nIngrese la cédula: ").strip()

#Funciones while para ingresar las notas del alumno
while True:
    try:
        nota1 = int(input("\nIngrese la primera nota: "))
        if 1<= nota1 <= 5:
            print("Nota Recibida con Exito")
            break
        else:
            print("Ingrese una nota valida (Del 1 al 5)")
    except ValueError:
        print("Error: Ingrese un número entero válido.")
while True:
    try:
        nota2 = int(input("\nIngrese la segunda nota: "))
        if 1<= nota2 <= 5:
            print("Nota Recibida con Exito")
            break
        else:
            print("Ingrese una nota valida (Del 1 al 5)")
    except ValueError:
        print("Error: Ingrese un número entero válido.\n")
while True:
    try:
        nota3 = int(input("\nIngrese la tercera nota: "))
        if 1<= nota3 <= 5:
            print("Nota Recibida con Exito")
            break
        else:
            print("Ingrese una nota valida (Del 1 al 5)")
    except ValueError:
        print("Error: Ingrese un número entero válido.\n")


#Objeto del alumno con las variables
alumno1 = Alumno(nombre, apellido, cedula, nota1, nota2, nota3)

#Llamada al objeto
alumno1.mostrar_datos()

"""Se define la clase Alumno implementando POO para empaquetar los datos personales y las tres
calificaciones del estudiante. Incluye métodos para obtener el promedio y determinar la condición basada en la escala.
Las notas se ingresan y validan entre 1 y 5 en un bucle procediendo a la impresión de la ficha del alumno
"""