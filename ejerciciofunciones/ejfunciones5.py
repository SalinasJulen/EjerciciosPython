## Ejercicio 5: 
### Escribir una función de Python que acepte una cadena como parámetro de entrada y cuente el número de letras mayúsculas y minúsculas.
### Ayuda: utilizar las funciones 'isupper()' - 'islower()'

def contar_mayus_minus(cadena):
    cant_mayus = 0
    cant_minus = 0
    for i in cadena:
        if i.isupper():
            cant_mayus += 1
        if i.islower():
            cant_minus += 1
            
    return f"La cantidad de mayúsculas es: {cant_mayus}, La cantidad de minúsculas es: {cant_minus}"

mi_cadena = "HoLI"
print(contar_mayus_minus(mi_cadena))