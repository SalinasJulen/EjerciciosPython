## Ejercicio 6:
### Crear una función que admita un número variable de parámetros (sin nombrar). Los parámetros pueden ser palabras o listas de 2/3 palabras. La función debe reconocer para cada parámetro si es una lista o no. 
# Si es una lista, indicar el número de elementos de la lista; si es una palabra, indicar que el parámetro es una palabra.

def mi_funcion(*mis_parametros):
    resultados = []
    for param in mis_parametros:
 
        if(type(param) == list):
            resultados.append(f"Lista con {len(param)} elementos")
        else:
            resultados.append("Este elemento es una Palabra")
    return resultados


resultado = mi_funcion("Holiwi", ["Si", "No"], "Limosna", ["Teclado", "Ratón", "Pantalla"])

print(resultado)