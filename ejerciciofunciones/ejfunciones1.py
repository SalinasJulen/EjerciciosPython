## Ejercicio 1:
### Escribir un programa Python que utilice una función recursiva para calcular la suma de los enteros positivos de n+(n-2)+(n-4)... (hasta que n-x <= 0).

def calcular_suma(n):
    if n < 1:
        return 0
    else:
        print("n es:" ,n)
        return n + calcular_suma(n-2)
print(calcular_suma(5))
# 5 + 3 + 1 + 0