from Persona import Persona

class Masculino(Persona):

    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

        print (" Hola Sr. " + nombre + "su edad es " + str(edad))