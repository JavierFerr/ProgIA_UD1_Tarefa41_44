from math import pi

from tarefa41_44.tarefa42 import areaCir, volumCil

def test_areaCir():
    assert areaCir(0) == 0
    assert areaCir(5) == pi * 5**2

def test_volumCil():
    assert volumCil(0,0) == 0
    assert volumCil(5,5) == (pi * 5**2)*5