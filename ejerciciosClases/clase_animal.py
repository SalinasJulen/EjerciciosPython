'''
## Ejercicio de múltiples instancias
### Crear la clase 'animal', que recoja el tipo de animal en su constructor (perro, gato...), 
en el atributo de instancia 'tipo'. Al crear el animal se debe imprimir el mensaje, por ejemplo para un gato, 
'gato creado'. También se debe inicializar el atributo de instancia 'recuento' a uno. Crear el método de instancia 'añadir' que aumente el atributo recuento en una unidad, 
y que escriba el recuento de animales de ese tipo.
### Suponer ahora que abrís una protectora de animales y os llegan el primer gato y el primer perro. 
Una vez creada la clase 'animal', podemos crear un objeto 'gato' y otro objeto 'perro'. 
Suponer ahora que llegan otro perro y otros dos gatos, llamar al método correspondiente las veces necesarias para actualizar el atributo 'recuento' de cada objeto.
'''

class Animal:
     # hacemos el modo de si recuento fuera un atributo de clase:
     # recuento = 1
     def __init__(self, tipo):
        self.tipo = tipo
        self.recuento = 1 # Asignamos por defecto este parámetro

        print(self.tipo, "creado")
    
     def anadir(self):
         self.recuento = self.recuento + 1
         return f"La cantidad total es: {self.recuento}"
     
'''
Si usamos el recuento como atributo de clase, tenemos que hacer también el método de clase:
     @classmethod
     def anadir(cls):
         cls.recuento += 1
         return f"La cantidad total es: {cls.recuento}"

      def addNew(self):
         self.recuento = self.recuento + 1
         return f"La cantidad total es: {self.recuento}"
      
hacemos un método de instancia también para que la variable de recuento se desvincule de la variable de clase     
 '''
# SI HACEMOS EL RECUENTO COMO ATRIBUTO DE CLASE, SI AÑADIMOS UN PERRO, ESTAMOS AÑADIENDO TAMBIÉN 1 DROMEDARIO, YA QUE ESTÁN TRABAJANDO LOS 2 SOBRE LA MISMA VARIABLE 'GLOBAL' Y SI AÑADIMOS UNO DE ESTOS, EN EL RESTO LO HARÁ IGUAL
   
perro1 = Animal("Golden")
dromedario1 = Animal("Desierto")


print(perro1.anadir())

print(dromedario1.anadir())
print(dromedario1.anadir())