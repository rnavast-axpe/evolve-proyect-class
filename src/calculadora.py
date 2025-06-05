"""
Módulo que implementa calculadoras con diferentes operaciones matemáticas.
"""
from typing import Union, Optional
from abc import ABC, abstractmethod
import math

class CalculadoraBase(ABC):
    """
    Clase base abstracta para calculadoras.
    """
    
    def __init__(self):
        """Inicializa la calculadora."""
        self._ultimo_resultado: Optional[float] = None
    
    @property
    def ultimo_resultado(self) -> Optional[float]:
        """Retorna el último resultado calculado."""
        return self._ultimo_resultado
    
    @abstractmethod
    def get_tipo_calculadora(self) -> str:
        """Retorna el tipo de calculadora."""
        pass

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

class CalculadoraTrigonometrica(CalculadoraBase):
    """
    Clase que implementa operaciones trigonométricas.
    """
    
    def get_tipo_calculadora(self) -> str:
        return "Trigonométrica"
    
    def seno(self, angulo_radianes: float) -> float:
        """
        Calcula el seno de un ángulo en radianes.
        
        Args:
            angulo_radianes: Ángulo en radianes
            
        Returns:
            float: Seno del ángulo
        """
        self._ultimo_resultado = math.sin(angulo_radianes)
        return self._ultimo_resultado
    
    def coseno(self, angulo_radianes: float) -> float:
        """
        Calcula el coseno de un ángulo en radianes.
        
        Args:
            angulo_radianes: Ángulo en radianes
            
        Returns:
            float: Coseno del ángulo
        """
        self._ultimo_resultado = math.cos(angulo_radianes)
        return self._ultimo_resultado
    
    def tangente(self, angulo_radianes: float) -> float:
        """
        Calcula la tangente de un ángulo en radianes.
        
        Args:
            angulo_radianes: Ángulo en radianes
            
        Returns:
            float: Tangente del ángulo
            
        Raises:
            ValueError: Si el coseno del ángulo es cero
        """
        if math.cos(angulo_radianes) == 0:
            raise ValueError("La tangente no está definida para este ángulo")
        self._ultimo_resultado = math.tan(angulo_radianes)
        return self._ultimo_resultado
    
    def grados_a_radianes(self, grados: float) -> float:
        """
        Convierte grados a radianes.
        
        Args:
            grados: Ángulo en grados
            
        Returns:
            float: Ángulo en radianes
        """
        self._ultimo_resultado = math.radians(grados)
        return self._ultimo_resultado
    
    def radianes_a_grados(self, radianes: float) -> float:
        """
        Convierte radianes a grados.
        
        Args:
            radianes: Ángulo en radianes
            
        Returns:
            float: Ángulo en grados
        """
        self._ultimo_resultado = math.degrees(radianes)
        return self._ultimo_resultado 