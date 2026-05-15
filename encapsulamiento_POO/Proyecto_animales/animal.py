class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def setNombre(self, nombre):
        self.nombre = nombre

    def setEspecie(self, especie):
        self.especie = especie

    def getInfo(self):
        return f"{self.nombre} es un {self.especie}"
