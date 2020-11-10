from adaptee import Adaptee
from target import Target

if __name__ == '__main__':

    xml = Adaptee()

    xml.set_archivo("datos.xml")

    xml.imprimir_elemento()

    xml.imprimirByTagName()

    xml.imprimirAllTagName()

    # ============

    json = Target()

    json.setArchivo("datos.json")

    json.imprimirArchivoTag()
