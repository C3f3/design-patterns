"""
Metodos en python
Haciendo uso de diferentes decorators (decoradores) es posible crear diferentes
tipos de  de métodos.

1.- Métodos Estáticos
decorator -> @staticmethod
No necesitan una instancia de la clase para ser utilizados
No tienen acceso al exterior, no pueden acceder a otro atributo o
llamar a otra función de la clase


2.- Métodos de clase
decorator -> @classmethod
Reciben el argumento cls, que hace referencia a la clase, por lo tanto, es
posible acceder a la clase y no a la instancia.
No pueden acceder a los atributos de la instancia
Si pueden modificar los atributos de la clase

3.- Métodos de instancia
Son los métodos normales, reciben como parámetro de entrada self que hace
referencia a la instancia que llama al método. También reciben otros argumentos
como entrada.

"""

# Ejemplo
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
