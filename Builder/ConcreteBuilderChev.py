"""
Constructor de autos Chevrolet
Concrete builder implementation
"""
from Builder import Builder 

class ConcreteBuilderChev(Builder):

    def get_cilindrada(self):
        cilindrada = 1600
        return cilindrada

    def get_potencia(self):
        self.potencia = 20
        return self.potencia

    def get_tipo(self):
        self.tipo = "Suv"
        return self.tipo

    def get_marca(self):
        self.marca = "Chevrolet"
        return self.marca