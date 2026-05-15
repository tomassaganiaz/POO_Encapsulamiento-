# tests/test_animales.py
from gato import Gato

def test_maullar():
    gato = Gato("Mishi")
    assert gato.maullar() == "Mishi dice: ¡Miau!"
