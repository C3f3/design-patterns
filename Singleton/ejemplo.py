"""
Ejemplo Singleton
"""

from singleton import Singleton

class ejemplo:

    def get_nombre(self):
        return "Wagner"

    def set_operacion(self):
        print("Ejmeplo con Singleton")
        x = Singleton.get_instance()
        y = Singleton.get_instance()

        print(x is y)

        y.set_value(10)

        print(x.get_value())

        print(y.get_value())

        print(x is y)

if __name__ == "__main__":
    e = ejemplo()

    e.set_operacion()