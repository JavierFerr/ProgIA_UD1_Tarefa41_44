from tarefa41_44.tarefa41 import calcular_suma


def test_suma_con_valores_conocidos():
    assert calcular_suma(0) == 0
    assert calcular_suma(1) == 1
    assert calcular_suma(5) == 15
    assert calcular_suma(100) == 5050


def test_suma_con_numeros_negativos():
    assert calcular_suma(-1) is None
    assert calcular_suma(-10) is None
