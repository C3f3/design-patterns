"""
Clase para definir un automovil
"""

class Automovil():
    
    def __init__(self):
        self._cilindrada = None
        self._potencia = None
        self._tipo = None
        self._marca = None
 
    # Setters
    def set_cilindrada(self, cilindrada):
        self._cilindrada = cilindrada

    def set_potencia(self,potencia):
        self._potencia = potencia

    def set_tipo(self,tipo):
        self._tipo = tipo

    def set_marca(self, marca):
        self._marca = marca


    # Salida de especificaciones
    def especificaciones(self):
        print("marca: {m}".format(m=self._marca))
        print("cilindrada: {c}".format(c=self._cilindrada))
        print("potencia: {p}".format(p=self._potencia))
        print("tipo: {t}".format(t=self._tipo))