## Ejercicio 4
#### Escribir una función de Python que verifique si una cadena pasada es un palíndromo o no.
#### Nota: Un palíndromo es una palabra, frase o secuencia que se lee igual hacia atrás que hacia adelante, por ejemplo: ojo, radar.


def es_capicua(cadena):
    for i in range(len(cadena)):
        if(cadena[i]!=cadena[len(cadena)-1-i]):
            return False
        return True
    
mi_cadena1 = "OPO"
mi_cadena2 = "Holi"

print(es_capicua(mi_cadena1))
print(es_capicua(mi_cadena2))