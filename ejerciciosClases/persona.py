'''
## Ejercicio 1:
### Crear una clase padre Persona (que contenga como atributos: identificacion (DNI), nombre, apellido), y crear una clase Alumno que extienda a Persona y agregue un nuevo atributo de instancia 'ciudad'.
### Crear dos objetos de clase Alumno y mostrar sus atributos.
'''


class Persona:
    def __init__(self, DNI,nombre,apellido):
        self.DNI = DNI
        self.nombre = nombre
        self.apellido = apellido

class Alumno(Persona):
    def __init__(self, DNI,nombre,apellido,ciudad):

        # Opción 2
        super().__init__(DNI, nombre, apellido)
        self.ciudad = ciudad


alumo1 = Alumno('37227835T','Pedro','Gartiburu','París')
alumo2 = Alumno('99372645H','Luis','García','Ankara')


print(alumo1.nombre)
print(alumo2.DNI)