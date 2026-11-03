import pytest

from tarefa41_44.tarefa43 import (
    aplicar10desc,
    aplicar21IVE,
    aplicar4IVE,
    lista_da_compra,
    totalCesta,
)


def test_aplicar21IVE():
    assert aplicar21IVE(100) == pytest.approx(121)


def test_aplicar4IVE():
    assert aplicar4IVE(100) == pytest.approx(104)


def test_aplicar10desc():
    assert aplicar10desc(100) == pytest.approx(90)


def test_totalCesta_coa_lista_da_compra():
    total, ive, desconto = totalCesta(lista_da_compra)

    assert total == pytest.approx(18.9565)
    assert ive == pytest.approx(3.1565)
    assert desconto == pytest.approx(0.85)


def test_totalCesta_baleira():
    assert totalCesta([]) == (0, 0, 0)