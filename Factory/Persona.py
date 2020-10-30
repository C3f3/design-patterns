"""
Clase que define a una persona
"""

class Persona(object):

    def __init__(self):
        self.nombre = None
        self.edad = None
        self.genero = None

    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad
    
    def get_genero(self):
        return self.genero

    def __str__(self):
        return "Datos Personales:\n 1.- Nombre: {n} \n 2.- Edad: {e} \n 3.- Genero: {g}".format(n=self.get_nombre(), e=self.get_edad(), g=self.get_genero())