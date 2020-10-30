"""
Constructor de autos Nissan
Concrete builder implementation
"""

from Builder import Builder

class ConcreteBuilderNissan(Builder):

    def get_cilindrada(self):
        self.cilindrada = 2000
        return self.cilindrada

    def get_potencia(self):
        self.potencia = 30
        return self.potencia

    def get_tipo(self):
        self.tipo = "Sedan"
        return self.tipo

    def get_marca(self):
        self.marca = "Nissan"
        return self.marca