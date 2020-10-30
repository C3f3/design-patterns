from Director import Director
from ConcreteBuilderChev import ConcreteBuilderChev
from ConcreteBuilderNissan import ConcreteBuilderNissan
from ConcreteBuilderKia import ConcreteBuilderKia

if __name__ == '__main__':

    chevrolet = ConcreteBuilderChev()
    nissan = ConcreteBuilderNissan()
    kia = ConcreteBuilderKia()

    director = Director()

    # Build Chev
    print("Chevrolet")
    director.set_builder(chevrolet)
    chevy = director.construct()
    chevy.especificaciones()

    # Build Nissan
    print("Nissan")
    director.set_builder(nissan)
    march = director.construct()
    march.especificaciones()

    # Build Kia
    print("Kia")
    director.set_builder(kia)
    autokia = director.construct()
    autokia.especificaciones()
