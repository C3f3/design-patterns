from Femenino import Femenino
from Masculino import Masculino

class Factoria(object):

    def get_persona(self, nombre, edad, genero):

        if (genero is 'F'):
            return Femenino(nombre, edad, genero)
        elif (genero is 'M'):
            return Masculino(nombre, edad ,genero)


