import Factoria

if __name__ == '__main__':

    mi_factoria = Factoria.Factoria()

    persona = mi_factoria.get_persona('Sebastian ', 32, 'M')

    print (persona)

    persona2 = mi_factoria.get_persona('Maria', 25, 'F')

    print(persona2)