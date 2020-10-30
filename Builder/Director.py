"""
Clase Director
Construir un objeto usando la interface builder

Controla el proceso de construcción.
Delega pequeñas funcionalidades al builder y las ensambla
"""

from Builder import Builder
from automovil import Automovil

_builder = None

class Director():

    def set_builder(self, builder):
        self._builder = builder

    def construct(self):
        auto = Automovil()

        cilindrada = self._builder.get_cilindrada()
        auto.set_cilindrada(cilindrada)

        potencia = self._builder.get_potencia()
        auto.set_potencia(potencia)

        marca = self._builder.get_marca()
        auto.set_marca(marca)

        tipo = self._builder.get_tipo()
        auto.set_tipo(tipo)

        return auto