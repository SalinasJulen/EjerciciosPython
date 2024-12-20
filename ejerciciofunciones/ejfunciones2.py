## Ejercicio 2
### Escribir un programa Python que utilice una función recursiva para calcular la suma de los elementos de una lista que tiene algunos elementos tipo lista.
### Por ejemplo, que calcule la suma de los elementos de la siguiente lista:
### [1, 2, [3, 4], [6, 4]]


def suma_recursiva(lista_parametro):
    suma = 0
    for i in range(len(lista_parametro)):
        try:
            for j in range(len(lista_parametro[i])):
                suma += lista_parametro[i][j]
        except:
            suma += lista_parametro[i]
    return suma

lista = [1, 2, [3, 4], [6, 4]]
resultado = suma_recursiva(lista)
print(f"La suma total es: {resultado}")


# https://www.youtube.com/watch?v=cdqTTDl_kS8



'''
   try:
       # Código que puede generar una excepción
   except:
       # Maneja cualquier excepción


   try:
       # Código que puede generar un TypeError
   except TypeError:
       # Maneja solo TypeError
'''