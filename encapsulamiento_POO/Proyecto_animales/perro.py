from animal import Animal

class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "Perro")

    def ladrar(self):
        return f"{self.nombre} dice: ¡Guau!"
