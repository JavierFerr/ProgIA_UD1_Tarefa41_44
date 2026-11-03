from tarefa41_44.tarefa44 import calculos,suma,lista

def test_suma():
    suma(0, 3) == 3
    suma(-1, 2) == 1
    suma(1,2) == 3

def test_calculos():
    assert calculos(lista, suma) == None
