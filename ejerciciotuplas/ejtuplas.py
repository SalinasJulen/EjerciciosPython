'''
Una librería tiene un sistema de gestión de inventario que necesita ser mejorado. Actualmente, el inventario se gestiona con listas y tuplas. El objetivo de este ejercicio es realizar diversas operaciones relacionadas con el inventario.
Cada libro en el inventario está representado por una tupla que contiene la siguiente información:

Título del libro (cadena de texto)
Autor (cadena de texto)
Año de publicación (entero)
Precio (float)
Disponibilidad en stock (booleano)
El inventario es una lista que contiene todas las tuplas de libros.

'''


# Define una lista llamada inventario que contenga al menos 5 libros, donde cada libro sea una tupla con la siguiente estructura: (título, autor, año, precio, disponible).
inventario = [("Dracula","Bram Stoker",1897,12,True),("La Metamorfosis","Franz Kafka",1915,15,True),("Guerra y Paz","León Tolstoi",1867,20,True),("Ulises","James Joyce",1922,20,False),("La Odisea","Homero",-800,30,True)]

titulos_disponibles = [a for a,b,c,d,e in inventario if e == True ]
tupla_cambiada = tuple(titulos_disponibles)
print(tupla_cambiada)

print ("\n")

# Escribe un bloque de código que recorra el inventario y guarde en una nueva lista solo los libros cuyo precio esté entre un min_precio y un max_precio definidos por el usuario. Al final, imprime esta lista.
min_precio = 15
max_precio = 25

precios_en_rango = [a for a,b,c,d,e in inventario if d >= min_precio and d <= max_precio ]
tupla_cambiada = tuple(precios_en_rango)
print(tupla_cambiada)

print ("\n")

# Modifica el código de manera que puedas cambiar el valor de disponibilidad (True o False) de un libro específico, identificado por su título. Si el título no está en el inventario, imprime un mensaje de error.

encontrado = False
for i in range(len(inventario)):
    if(inventario[i][0] == "Dracula"): # no podemos hacer libro[4] para cambiar la disponibilidad, ya que se cambia SOLO LA VARIABLE Y NO LA LISTA, TUPLA, por eso hay que modificarlo directamente
        inventario[i] = inventario[i][:4] + (False,) # pilla todos los elementos de antes hasta el 4 y suma la tupla (en este caso es (False,) ya que si no lo hacemos mediante una tupla no funciona)
        encontrado = True
        break

if not encontrado:
    print ("El libro no se ha encontrado")
# con esto recorremos cada elemento de cada tupla de la lista, inventario[i][0]

print(inventario)

print ("\n")


# Implementa un bloque de código que elimine un libro del inventario basado en su título. Si el libro no existe, imprime un mensaje de error.
titulo_a_eliminar = "Ulises" 

libro_encontrado = False
for libro in inventario:
    if libro[0] == titulo_a_eliminar:
        inventario.remove(libro)
        libro_encontrado = True
        print(f"El libro '{titulo_a_eliminar}' ha sido eliminado del inventario.")
        break

if not libro_encontrado:
    print(f"Error: El libro '{titulo_a_eliminar}' no se encuentra en el inventario.")


print("\nInventario actualizado:")
for libro in inventario:
    print(libro)

print ("\n")

#Escribe un bloque de código que:

#Cuente cuántos libros hay en total en el inventario.


i = 0
while i < len(inventario):
  i = i + 1
print("El inventario tiene ",i," libros")

print ("\n")



# Cuente cuántos están disponibles.
cant_disponibles = 0
for a,b,c,d,e in inventario:
    if e == True:
        cant_disponibles = cant_disponibles + 1
        print("El libro ",a," está disponible")
print("El inventario tiene ",cant_disponibles," libros disponibles")

print ("\n")

# Calcule y muestre el precio promedio de todos los libros.
precio_total = 0
cantidad_libros = len(inventario)
for a,b,c,d,e in inventario:
    precio_total = precio_total + d
precio_promedio = precio_total / cantidad_libros
print("El precio promedio de los libros es ",precio_promedio)