"""
Constructor de autos Kia
Concrete builder implementation
"""

from Builder import Builder

class ConcreteBuilderKia(Builder):

    def get_cilindrada(self):
        cilindrada = 1800
        return cilindrada

    def get_potencia(self):
        self.potencia = 22
        return self.potencia

    def get_tipo(self):
        self.tipo = "Suv"
        return self.tipo

    def get_marca(self):
        self.marca = "Kia"
        return self.marca
