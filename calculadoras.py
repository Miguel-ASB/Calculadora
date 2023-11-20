from abc import ABC, abstractmethod
import math

class Calculadora(ABC):

    @abstractmethod
    def sumar(self, a, b):
        pass

    @abstractmethod
    def restar(self, a, b):
        pass

    @abstractmethod
    def multiplicar(self, a, b):
        pass

    @abstractmethod
    def dividir(self, a, b):
        pass

    @abstractmethod
    def raiz(self, a, b):
        pass



class CalculadoraNumeros(Calculadora):

    def sumar(self, a, b):
        return a + b
    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b
    def dividir(self, a, b):
        try:
            return a / b
        except ZeroDivisionError as z:
            raise ZeroDivisionError ('Esto es un error de division')

    def raiz(self, a, b):
        try:
            return a ** (1/b)
        except Exception as error:
            raise Exception ('Error en la raiz')
