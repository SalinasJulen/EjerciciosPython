## Ejercicio 2, juego:
'''
- Importar la librería random para trabajar con datos aleatorios
- Definir la clase Personaje que más tarde va a ser heredada por la clase Jugador() y Enemigo(). En la clase Personaje() se define el constructor \__init__ y se inicializan sus parámetros (nombre='', salud=1, saludMax=1), también se define el método hacerDaño(objetoEnemigo) que nos dará un valor aleatorio del daño provocado en el ataque. 
Definir el método de instancia hacerDaño(objetoEnemigo) que obtiene un valor aleatorio del daño provocado en el ataque (entre 0 y 5) y calcula la nueva salud del enemigo restándole el daño a la salud del enemigo antes del ataque. 
El método devuelve un valor booleano que indica si la salud del enemigo es <= 0.
- Se crea la clase Enemigo que hereda la clase Personaje, con un constructor que inicializa el nombre del enemigo (='Orco') y la salud (entero aleatorio entre 6 y 10). Tiene el método 'estadoEnemigo' que devuelve el estado del enemigo.
- Se crea la clase Jugador que hereda la clase Personaje:
    - Su constructor inicializa el actitud='normal', la salud=10 y la salud máxima del jugador saludMax=10
    - Tiene el método de instancia estadoJugador que nos devuelve la salud del jugador.
    - Tiene el método cansancio: cuando este método es llamado, se despliega un mensaje de "siente cansancio" y la propiedad salud del jugador bajará 5 puntos. Se cambia la actitud a 'lucha'
    - Tiene el método atacar: cuando este método es llamado, se plantea una condición: si la actitud del jugador es distinta de "lucha", se muestra un mensaje y el método cansancio() es llamado. De lo contrario se plantea otra condición: si el método hacerDaño() es True, el enemigo es destruido y la actitud cambia a normal. De lo contrario, en caso de tener suerte la salud y salud_maxima suben a 1, y el método ataque_enemigo es llamado.
    - método ataque_enemigo: este método es llamado cuando el Jugador ataca al enemigo, pero no lo mata. Entonces el enemigo responde y ataca al jugador, que es lo que hace este método. Si el enemigo mata al jugador, se imprime mensaje por pantalla.
- Por último se crean el objeto 'jugador1' de clase Jugador y el objeto 'enemigo1' de clase Enemigo, y se crea un bucle para jugar mientras la salud del jugador sea > 0.
'''

import random

class Personaje:
    
    def __init__(self):
        self.nombre = ""
        self.salud = 1
        self.saludMax = 10

    def hacerDano(self,objetoEnemigo):
        
        aleatorio = random.randint(0, 5)
        objetoEnemigo.salud = objetoEnemigo.salud - aleatorio
        if self.salud > 0:
            print(f"{objetoEnemigo.nombre} evade el ataque de {self.nombre}")
        else:
            print(f"{objetoEnemigo.nombre} acierta el ataque de {self.nombre}")
        return objetoEnemigo.salud <= 0 # si no está muerto devuelve true?
        

class Enemigo(Personaje):
    def __init__(self):
        Personaje.__init__(self) # heredamos el constructor del padre
        self.nombre = "Orco"
        self.salud = random.randint(6, 10)
        # self.saludMax = 10
        
    def estadoEnemigo(self):
        print(f"{self.nombre} - salud : {self.salud}/{self.saludMax}")
        

class Jugador(Personaje):
    def __init__(self):
        Personaje.__init__(self)

        self.salud = 10
        self.saludMax = 10

        super().__init__()
        self.actitud = "Normal"

    def estadoJugador(self):
        print(f"{self.nombre} - salud : {self.salud}/{self.saludMax}")

    def cansancio(self):
        print ("Siente cansancio")
        self.salud = self.salud - 5
        if (self.salud <= 0) : print(f"{self.nombre} ha muerto")
        self.actitud = "Lucha"


   
        

    def atacar(self,enemigo):
        if self.actitud != "Lucha":
            print(f"{self.nombre} no está en modo lucha, a descansar")
            self.cansancio()
        elif self.hacerDano(enemigo):
            print(f"{self.nombre} aniquila a {enemigo.nombre}")
            self.actitud = "Normal"
                
        else:
            if random.randint(0, 6) < 3:
                self.salud = self.salud + 1
                self.saludMax = self.saludMax
                print (f"salud de {self.nombre} : {self.salud}, se siente más fuerte")
            self.ataque_enemigo(enemigo) # contra ataca

    def ataque_enemigo(self,enemigo):
        if enemigo.hacerDano(self):
           print (f"{self.nombre} fue sacrificado por {enemigo.nombre}")
   

jugador1 = Jugador()
enemigo1 = Enemigo ()

jugador1.nombre = input("Introduzca el nombre del jugador: ")
accionesValidas = ["estadoJ", "estadoE", "cansancio", "atacar"]
while(jugador1.salud > 0):
    accion = input("Introduzca la acción que quiere ejecutar (estadoJ, estadoE,      \
                   cansancio o atacar), * para terminar: ")    
    if accion == '*':
        break
    elif accion in accionesValidas:
        if accion == 'estadoJ':
            jugador1.estadoJugador()
        elif accion == 'estadoE':
            enemigo1.estadoEnemigo()
        elif accion == 'cansancio':
            jugador1.cansancio()
        else:
            jugador1.atacar()
           
    else:
        print (f"{jugador1.nombre} no se entiende la accion.")