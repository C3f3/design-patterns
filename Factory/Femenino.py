from Persona import Persona

class Femenino(Persona):

    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        
        print (" Hola Sra. " + nombre + " su edad es " + str(edad))