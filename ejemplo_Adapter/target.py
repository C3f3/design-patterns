import json

class Target():

    def __init__(self):
        self.__archivo = ""

    def setArchivo(self, nombre):
        self.__archivo = nombre

    def leerArchivo(self):
        try:
            with open(self.__archivo) as file:
                return json.load(file)
        except:
            print("Error: No es posible cargar el archivo {f}".format( \
                f=self.archivo))

    def imprimirArchivo(self):

        archivo = self.leerArchivo()

        print(archivo)

    def imprimirArchivoTag(self):

        archivo = self.leerArchivo()

        print("Imprimir Matriz conocimiento json")
        print(archivo["lenguajes"])
