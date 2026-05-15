from gato import Gato
from perro import Perro
from loro import Loro
from utils import mostrar_animales

def main():
    gato1 = Gato("Mishi")
    perro1 = Perro("Firulais")
    loro1 = Loro("Pepe")

    animales = [gato1, perro1, loro1]
    mostrar_animales(animales)

    print(gato1.maullar())
    print(perro1.ladrar())
    print(loro1.hablar())

if __name__ == "__main__":
    main()
