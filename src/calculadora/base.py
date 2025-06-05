"""
Módulo base para las calculadoras.
"""
from typing import Optional
from abc import ABC, abstractmethod

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