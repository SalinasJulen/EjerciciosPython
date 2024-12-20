'''
### Los métodos pueden llamar a otros métodos de la instancia usando el argumento self.
### Ejercicio: hacer una clase 'calculadora' que defina en su constructor dos Atributos de instancia: 
'num1' y 'num2'. Hay que hacer un método de instancia 'suma' que sume los dos números. 
Hay que hacer un segundo método 'sumax5' que use el método anterior para calcular la suma, 
y que luego haga el producto de la suma por 5. Luego crear un objeto 'objCalc' de la clase 'calculadora', 
y llamar a sus métodos.
'''
class Calculadora:
     def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

     def suma (self):
         return self.n1+self.n2
    
     def sumax5 (self):
         return self.suma() * 5

    
objCalc = Calculadora(2,5)
print(objCalc.suma())
print(objCalc.sumax5())
