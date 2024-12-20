people = [["Ana", 25], ["Luis", 17], ["Carlos", 20], ["María", 16], ["Lucía", 22]]

# Extraer solo los nombres de las personas mayores de 18 años.
newlist = [x for x, y in people if y>=18 ]
print (newlist)


print ("\n")

# Crear una nueva lista invirtiendo el orden de los elementos en cada sublista
listas_por_edad = [[y, x] for x, y in people]
print(listas_por_edad)
# Ordenar las sublistas
listas_por_edad.sort()
print(listas_por_edad)
# Volver a invertir el orden de los elementos en cada sublista
listas_por_edad = [[y, x] for x, y in listas_por_edad] # lo que antes era x , y (nombre, edad) ahora es y, x (edad, nombre) por eso volvemos a invertir el orden
listas_por_edad.reverse()
print( listas_por_edad)


print ("\n")



# Copiar esta lista ordenada y luego invertir el orden de la copia.
copia_listas_por_edad = listas_por_edad.copy()
copia_listas_por_edad.reverse()
print(copia_listas_por_edad)	



print ("\n")


# Une los nombres en una cadena separada por comas y muestra el resultado final.
nombres_unidos = [x for x,y in copia_listas_por_edad]
resultado_final = ", ".join(nombres_unidos)
print(resultado_final)
