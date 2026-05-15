from animal import Animal

class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "Gato")

    def maullar(self):
        return f"{self.nombre} dice: ¡Miau!"
