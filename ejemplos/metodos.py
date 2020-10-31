"""
Metodos en python

1.- Métodos Estáticos
@staticmethod
No necesitan una instancia de la clase para ser utilizados
No tienen acceso al exterior, no pueden acceder a otro atributo o
llamar a otra función de la clase


2.- Métodos de clase

3.- Métodos de instancia
"""

# Ejemplo Método Estático
class Imprimir:

    
    # Metodo de instancia
    def info_param(self, param1, param2):
        print("Ejemplo Suma:")
        a = param1 + param2
        print("Result = {a}".format(a=a))

    @staticmethod
    def info():
        print("mi programa")

    @classmethod
    def info_clase(cls):
        return 'metodo clase', cls

if __name__ == "__main__":
    i = Imprimir()
    i.info()

    Imprimir.info()

    i.info_param(5,34)

    m = Imprimir.info_clase()
    print(m)