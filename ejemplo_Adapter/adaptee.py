from xml.dom import minidom

class Adaptee():
    """
    Clase que permite leer información desde un archivo de tipo XML
    """

    def __init__(self):
        self.__archivo = ""

    def set_archivo(self, nombre):
        self.__archivo = nombre

    def leer_xml(self):
        # uso de la funcion parse() para cargar y parsear un archivo XML
        try:
            return minidom.parse(self.__archivo)
        except:
            print("Error: no es posible cargar el archivo {a}".format(a=self.__archivo))

    def imprimir_elemento(self):

        archivo = self.leer_xml()

        print(archivo.nodeName)
        print(archivo.firstChild.tagName)

    def imprimirByTagName(self):

        archivo = self.leer_xml()

        lenguajes = archivo.getElementsByTagName('lenguajes')

        print("Matriz de conocimiento")
        print(lenguajes[2].attributes['name'].value)

    def imprimirAllTagName(self):

        archivo = self.leer_xml()

        listado = archivo.getElementsByTagName('lenguajes')

        print("Imprimir Matriz de conocimiento completa")
        for i in listado:
            print(i.firstChild.data)
