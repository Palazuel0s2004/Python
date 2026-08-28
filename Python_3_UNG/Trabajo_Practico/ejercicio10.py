#10. Clase Persona y mayoría de edad
#Crear una clase llamada Persona con los siguientes atributos:
#• nombre;
#• apellido;
#• cédula;
#• año de nacimiento;
#• ciudad.
#Implementar métodos para:
#• Mostrar los datos personales.
#• Calcular la edad aproximada.
#• Indicar si la persona es mayor o menor de edad.
#• Utilizar los datos personales del estudiante para realizar la prueba.
#• El año de nacimiento no puede ser mayor que el año actual.

class Persona:
    def __init__(self, nombre, apellido, cedula, año_nacimiento, ciudad):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.año_nacimiento = año_nacimiento
        self.ciudad = ciudad

    def edad(self):
        return 2026 - self.año_nacimiento

    def legalidad(self):
        if self.edad() >= 18:
            return "Es mayor de edad"
        else:
            return "Es menor de edad"

    #Funcion para mostrar los datos
    def mostrar_datos(self):
        print("\n\tDatos de la Persona")
        print(f"Nombre completo: {self.nombre} {self.apellido}")
        print(f"Cedula: {self.cedula}")
        print(f"El año de nacimiento es: {self.año_nacimiento}")
        print(f"Su edad es: {self.edad()}")
        print(f"Situación legal: {self.legalidad()}")
        print(f"Es de la ciudad: {self.ciudad}")


#Variables para datos personales de la persona
nombre = input("\nIngrese el nombre de la persona: ").strip()
apellido = input("\nIngrese el apellido de la persona: ").strip()
cedula = input("\nIngrese la cédula: ").strip()
ciudad = input("\nIngrese la ciudad: ").strip()

#While para validar la edad
while True:
    try:
        año_nacimiento = int(input("\nIngrese su año de nacimiento: "))
        if 0 < año_nacimiento <= 2026:
            break
        else:
            print("Ingrese un año válido (entre 1 y 2026).")
    except ValueError:
        print("Error: Ingrese un número entero válido.")

persona1 = Persona(nombre, apellido, cedula, año_nacimiento, ciudad)
persona1.mostrar_datos()

"""El programa crea la clase Persona instanciando los atributos del estudiante mediante métodos
internos calcula la edad tomando como base el año actual y determina la mayoría de edad con >=18
e incluye validación try except para asegurar que el año ingresado no sea futuro ni negativo"""