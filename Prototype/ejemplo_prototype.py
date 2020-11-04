
from fabrica import Creador

class Ejemplo_prototype:

    def operacion(self):
        print("Ejemplo Proptotype")
        creador = Creador()
        animales = []

        for i in range(4):
            animales.append(creador.clonacion_animal("Gato"))
        for i in range(4):
            animales.append(creador.clonacion_animal("Perro"))

        for i in animales:
            print(i.saludo())

        animales[3].cambiar_propietario("Marta")

        for i in animales:
            print(i.saludo())

