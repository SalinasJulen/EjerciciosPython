## Ejercicio 3
### Escribir un programa Python para calcular el valor de 'a' elevado a 'b'.
### Ayuda: '0' elevado a 'b' será siempre '0' ; 'a' elevado a '0' será siempre '1'
### Ayuda: $a^5=a*a^4$
### Ejemplo de prueba: potencia(3,2) = 9



def calcular_potencia (n):
    return lambda a : pow(a,n)


elevado_a = calcular_potencia(5)

print(elevado_a(2))
