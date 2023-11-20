import pytest
from calculadoras import *


@pytest.fixture
def calculadora():
    return CalculadoraNumeros()


def test_sumar(calculadora):
    assert calculadora.sumar(1, 1) == 2
    pass


def test_restar(calculadora):
    assert calculadora.restar(10, 2) == 8
    pass


def test_multiplicar(calculadora):
    assert calculadora.multiplicar(5, 5) == 25
    pass


def test_dividir(calculadora):
    assert calculadora.dividir(10, 2) == 5
    pass


def test_raiz(calculadora):
    assert calculadora.raiz(16, 2) == 4
    pass


def test_falla_division_cero(calculadora):
    with pytest.raises(ZeroDivisionError) as error:
        calculadora.dividir(1, 0)
    assert str(error.value) == 'Esto es un error de division'

def test_falla_raiz(calculadora):
    with pytest.raises(Exception) as error:
        calculadora.raiz(-1, 0)

    assert srt(error.value) == 'Error en la raiz'










