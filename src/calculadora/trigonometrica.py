"""
Módulo que implementa la calculadora trigonométrica.
"""
import math
from .base import CalculadoraBase

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