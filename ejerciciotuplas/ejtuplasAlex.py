inventario = [("Dracula","Bram Stoker",1897,12,True),("La Metamorfosis","Franz Kafka",1915,15,True),("Guerra y Paz","León Tolstoi",1867,20,True),("Ulises","James Joyce",1922,20,False),("La Odisea","Homero",-800,30,True)]

# 2. Buscar libros disponibles
print("Libros disponibles:")
for libro in inventario:
    if libro[4] == True:  # Disponibilidad es el quinto elemento en la tupla
        print(libro[0])   # Título es el primer elemento en la tupla

# 3. Filtrar libros por rango de precios
min_precio = 7.00
max_precio = 13.00
libros_en_rango = []
for libro in inventario:
    if min_precio <= libro[3] <= max_precio:  # Precio es el cuarto elemento
        libros_en_rango.append(libro)

print("\nLibros en el rango de precio:")
for libro in libros_en_rango:
    print(libro[0])


# 4. Actualizar disponibilidad de un libro
titulo_a_cambiar = "1984"
nueva_disponibilidad = False
encontrado = False
'''
Este código cambia la tupla 'libro' pero no cambia la tupla correspondiente de 'inventario' 
for libro in inventario:
    if (libro[0] == titulo_a_cambiar):
        libro = libro[:4] + (nueva_disponibilidad,)
'''
for i in range(len(inventario)):
    if inventario[i][0] == titulo_a_cambiar:  # Título es el primer elemento
        inventario[i] = inventario[i][:4] + (nueva_disponibilidad,)  # Modificar la disponibilidad
        encontrado = True
        break
if not encontrado:
    print(f"\nEl libro '{titulo_a_cambiar}' no se encontró en el inventario.")



print(inventario)



# 5. Eliminar un libro
titulo_a_eliminar = "Don Quijote"
eliminado = False
for libro in inventario:
    if libro[0] == titulo_a_eliminar:
        inventario.remove(libro)
        eliminado = True
        break
if not eliminado:
    print(f"\nEl libro '{titulo_a_eliminar}' no se encontró en el inventario.")

print(inventario)



# 6. Mostrar resumen del inventario
# sum -> Sums the items of an iterator
total_libros = len(inventario)
x = [1 for libro in inventario if libro[4]]
print("x: ",x)
libros_disponibles = sum(x)
precio_promedio = sum(libro[3] for libro in inventario) / total_libros if total_libros > 0 else 0

print(f"\nResumen del inventario:")
print(f"Total de libros: {total_libros}")
print(f"Libros disponibles: {libros_disponibles}")
print(f"Precio promedio: {precio_promedio:.2f}")