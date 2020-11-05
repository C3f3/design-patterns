
import fabrica

class Ejemplo_prototype:

    def operacion(self):
        print("Ejemplo Proptotype")
        creador = fabrica.Creador()
        animales = []

        for i in range(4):
            print("Clonando Gatos...")
            animales.append(creador.clonacion_animal("Gato"))

        for i in range(4):
            print("Clonando Perros...")
            animales.append(creador.clonacion_animal("Perro"))

        for i in animales:
            print("Desplegar valores:")
            print(i.saludo())

        animales[3].cambiar_propietario("Marta")
        print("Cambio de propietario a del clon 4 a Marta")

        for i in animales:
            print("Desplegar valores:")
            print(i.saludo())

