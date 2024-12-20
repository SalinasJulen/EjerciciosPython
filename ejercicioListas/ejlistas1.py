# Crear una lista con tres items, en la que cada item sea una lista de dos elementos (['nombre', 'apellido'], uno de los apellidos el vuestro


lista1 = ["Luis","Aramburu"]
lista2 = ["Julen","Salinas"]
lista3 = ["García","Vaquero"]

mylist = [lista1, lista2, lista3]
print(mylist)

new_list = []

# Crear un bucle for que recorra la lista 'padre', y si es el apellido es el vuestro, crear una nueva lista que contenga la lista 'hijo' con vuestro nombre y apellido.
for x in mylist:
  if "Salinas" in x:
    print("Yes, 'Salinas' is in mylist list")
    new_list.append(x)
  else:
    print("No, 'Salinas' is not in mylist list")

  print (new_list)