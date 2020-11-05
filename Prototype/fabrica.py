
from prototipos import Gato, Perro, Owner

class Creador():
    def __init__(self):
        self.__gato = Gato()
        self.__perro = Perro()

        self.__gato.set_propietario(Owner("Sebastian"))
        self.__gato.set_descripcion("Gatito plomizo")
        self.__gato.set_nombre("Merlín")

        self.__perro.set_propietario(Owner("Esteban"))
        self.__perro.set_descripcion("Perrito destroza patios")
        self.__perro.set_nombre("Flow")

    def clonacion_animal(self, tipo_animal):
            if "Gato" == tipo_animal:
                return self.__gato.clone()
            elif "Perro" == tipo_animal:
                return self.__perro.clone()
            return None
