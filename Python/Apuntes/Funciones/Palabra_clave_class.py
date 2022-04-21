# class crea una clase donde se pueden agregar objetos, metodos etc.

class Persona:

    # La funcion __init__ siempre se inicializa al usar la clase como se ve en las variables david y kevin

    def __init__(self, nombre, edad):
        # Se guardan los nombres y edades de cada persona
        self.nombre = nombre
        self.edad = edad
    
    def saluda(self, otra_persona):
        # Otra persona es la variable david a la que se le asigna el nombre y self es la persona que ejecuta el metodo saluda() el cual es kevin
        print(f"Hola {otra_persona.nombre}, mi nombre es {self.nombre}")

david = Persona("David", 16)
kevin = Persona("Kevin", 15)

kevin.saluda(david)