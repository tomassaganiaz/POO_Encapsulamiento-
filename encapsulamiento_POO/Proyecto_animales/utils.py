def mostrar_animales(animales):
    for a in animales:
        print(a.getInfo())

def buscar_animal(animales, nombre):
    return next((a for a in animales if a.nombre == nombre), None)
