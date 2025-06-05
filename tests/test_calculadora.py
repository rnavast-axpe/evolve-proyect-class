"""
Pruebas unitarias para las calculadoras.
"""
import unittest
import math
from calculadora import CalculadoraBasica, CalculadoraTrigonometrica

class TestCalculadoraBasica(unittest.TestCase):
    """Clase de pruebas para la calculadora básica."""
    
    def setUp(self):
        """Configuración inicial para cada prueba."""
        self.calc = CalculadoraBasica()
    
    def test_suma(self):
        """Prueba la operación de suma."""
        self.assertEqual(self.calc.sumar(2, 3), 5)
        self.assertEqual(self.calc.sumar(-1, 1), 0)
        self.assertEqual(self.calc.sumar(0, 0), 0)
    
    def test_resta(self):
        """Prueba la operación de resta."""
        self.assertEqual(self.calc.restar(5, 3), 2)
        self.assertEqual(self.calc.restar(1, 1), 0)
        self.assertEqual(self.calc.restar(0, 5), -5)
    
    def test_multiplicacion(self):
        """Prueba la operación de multiplicación."""
        self.assertEqual(self.calc.multiplicar(2, 3), 6)
        self.assertEqual(self.calc.multiplicar(-2, 3), -6)
        self.assertEqual(self.calc.multiplicar(0, 5), 0)
    
    def test_division(self):
        """Prueba la operación de división."""
        self.assertEqual(self.calc.dividir(6, 2), 3)
        self.assertEqual(self.calc.dividir(5, 2), 2.5)
        self.assertEqual(self.calc.dividir(0, 5), 0)
    
    def test_division_por_cero(self):
        """Prueba que la división por cero lance una excepción."""
        with self.assertRaises(ZeroDivisionError):
            self.calc.dividir(5, 0)
    
    def test_ultimo_resultado(self):
        """Prueba que el último resultado se almacene correctamente."""
        self.calc.sumar(2, 3)
        self.assertEqual(self.calc.ultimo_resultado, 5)
        
        self.calc.restar(10, 5)
        self.assertEqual(self.calc.ultimo_resultado, 5)
    
    def test_tipo_calculadora(self):
        """Prueba que el tipo de calculadora sea correcto."""
        self.assertEqual(self.calc.get_tipo_calculadora(), "Básica")

class TestCalculadoraTrigonometrica(unittest.TestCase):
    """Clase de pruebas para la calculadora trigonométrica."""
    
    def setUp(self):
        """Configuración inicial para cada prueba."""
        self.calc = CalculadoraTrigonometrica()
    
    def test_seno(self):
        """Prueba la función seno."""
        self.assertAlmostEqual(self.calc.seno(0), 0)
        self.assertAlmostEqual(self.calc.seno(math.pi/2), 1)
        self.assertAlmostEqual(self.calc.seno(math.pi), 0)
    
    def test_coseno(self):
        """Prueba la función coseno."""
        self.assertAlmostEqual(self.calc.coseno(0), 1)
        self.assertAlmostEqual(self.calc.coseno(math.pi/2), 0)
        self.assertAlmostEqual(self.calc.coseno(math.pi), -1)
    
    def test_tangente(self):
        """Prueba la función tangente."""
        self.assertAlmostEqual(self.calc.tangente(0), 0)
        self.assertAlmostEqual(self.calc.tangente(math.pi/4), 1)
    
    def test_tangente_indefinida(self):
        """Prueba que la tangente lance error para ángulos indefinidos."""
        with self.assertRaises(ValueError):
            self.calc.tangente(math.pi/2)
    
    def test_conversion_angulos(self):
        """Prueba la conversión entre grados y radianes."""
        self.assertAlmostEqual(self.calc.grados_a_radianes(180), math.pi)
        self.assertAlmostEqual(self.calc.radianes_a_grados(math.pi), 180)
    
    def test_ultimo_resultado(self):
        """Prueba que el último resultado se almacene correctamente."""
        self.calc.seno(math.pi/2)
        self.assertAlmostEqual(self.calc.ultimo_resultado, 1)
        
        self.calc.coseno(0)
        self.assertAlmostEqual(self.calc.ultimo_resultado, 1)
    
    def test_tipo_calculadora(self):
        """Prueba que el tipo de calculadora sea correcto."""
        self.assertEqual(self.calc.get_tipo_calculadora(), "Trigonométrica")

if __name__ == '__main__':
    unittest.main() 