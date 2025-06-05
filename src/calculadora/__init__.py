"""
Paquete de calculadoras matemáticas.
"""
from .base import CalculadoraBase
from .basica import CalculadoraBasica
from .trigonometrica import CalculadoraTrigonometrica

__version__ = "0.1.0"
__all__ = ["CalculadoraBase", "CalculadoraBasica", "CalculadoraTrigonometrica"] 