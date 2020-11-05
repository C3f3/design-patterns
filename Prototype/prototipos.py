from abc import ABC, abstractmethod
from copy import copy, deepcopy

class Animal(ABC):

    def __init__(self):
        self.__descripcion__ = ""
        self.__nombre__ = ""
        self.__propietario__ = None

    # setters
    def set_propietario(self, propietario):
        self.__propietario__ = propietario

    def set_descripcion(self, descripcion):
        self.__descripcion__ = descripcion

    def set_nombre(self, nombre):
        self.__nombre__ = nombre

    # getters
    def get_descripcion(self):
        return self.__descripcion__

    def get_nombre(self):
        return self.__nombre__

    def get_propietario(self):
        return self.__propietario__

    # Otros Metodos
    def saludo(self):
        return "Animal: " + self.__nombre__ + ", propiedad de: " + \
                self.__propietario__.get_name()

    def cambiar_propietario(self, nombre):
        self.__propietario__.set_name(nombre)

    def clone(self):
        return deepcopy(self)

class Perro(Animal):
    pass

class Gato(Animal):
    pass

class Owner():
    def __init__(self, nombre):
        self.__name__ = nombre

    def set_name(self, nombre):
        self.__name__ = nombre

    def get_name(self):
        return self.__name__


