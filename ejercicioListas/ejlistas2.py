list1 = [12, 43, 56, 7, 22, 98, 34] 
list2 = [65, 34, 89, 21, 24, 78, 56]

# Usa 'comprensión de listas' para filtrar solo los números pares de ambas listas. 
# Une las dos listas filtradas.
    # (son 2 ejercicios)
newlist = [x for x in list1 + list2 if x % 2==0]
print(newlist)

# Ordena la lista combinada en orden descendente.
newlist.sort()
newlist.reverse()
print(newlist)

# Haz una copia de la lista resultante y elimina los números duplicados de la copia.
converted = list(set(newlist))

print(converted)

print ("\n")

# Muestra ambas listas (original y copia).
print(newlist)
print(converted)
