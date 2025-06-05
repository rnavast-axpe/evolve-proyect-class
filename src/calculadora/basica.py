"""
Módulo que implementa la calculadora básica.
"""
from typing import Union
from .base import CalculadoraBase

class CalculadoraBasica(CalculadoraBase):
    """
    Clase que implementa operaciones matemáticas básicas.
    """
    
    def get_tipo_calculadora(self) -> str:
        return "Básica"
    
    def sumar(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        Realiza la suma de dos números.
        
        Args:
            a: Primer número
            b: Segundo número
            
        Returns:
            float: Resultado de la suma
        """
        self._ultimo_resultado = float(a + b)
        return self._ultimo_resultado
    
    def restar(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        Realiza la resta de dos números.
        
        Args:
            a: Primer número
            b: Segundo número
            
        Returns:
            float: Resultado de la resta
        """
        self._ultimo_resultado = float(a - b)
        return self._ultimo_resultado
    
    def multiplicar(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        Realiza la multiplicación de dos números.
        
        Args:
            a: Primer número
            b: Segundo número
            
        Returns:
            float: Resultado de la multiplicación
        """
        self._ultimo_resultado = float(a * b)
        return self._ultimo_resultado
    
    def dividir(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        Realiza la división de dos números.
        
        Args:
            a: Primer número
            b: Segundo número
            
        Returns:
            float: Resultado de la división
            
        Raises:
            ZeroDivisionError: Si el divisor es cero
        """
        if b == 0:
            raise ZeroDivisionError("No se puede dividir por cero")
        self._ultimo_resultado = float(a / b)
        return self._ultimo_resultado 