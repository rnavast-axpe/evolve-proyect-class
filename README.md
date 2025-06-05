# Calculadora Matemática

Una librería Python que implementa diferentes tipos de calculadoras con operaciones matemáticas siguiendo buenas prácticas de programación.

## Instalación

```bash
pip install calculadora-matematica
```

## Características

### Calculadora Básica
- Operaciones matemáticas básicas (suma, resta, multiplicación, división)
- Manejo de errores (división por cero)
- Seguimiento del último resultado

### Calculadora Trigonométrica
- Funciones trigonométricas (seno, coseno, tangente)
- Conversión entre grados y radianes
- Manejo de casos especiales (tangente indefinida)
- Seguimiento del último resultado

## Estructura del Proyecto

```
calculadora-matematica/
├── src/
│   └── calculadora/
│       ├── __init__.py
│       ├── base.py
│       ├── basica.py
│       └── trigonometrica.py
├── tests/
│   └── test_calculadora.py
├── setup.py
├── requirements.txt
└── README.md
```

## Uso

### Calculadora Básica
```python
from calculadora import CalculadoraBasica

# Crear una instancia de la calculadora básica
calc_basica = CalculadoraBasica()

# Realizar operaciones
resultado = calc_basica.sumar(5, 3)  # Retorna 8
resultado = calc_basica.restar(10, 4)  # Retorna 6
resultado = calc_basica.multiplicar(2, 3)  # Retorna 6
resultado = calc_basica.dividir(10, 2)  # Retorna 5.0
```

### Calculadora Trigonométrica
```python
from calculadora import CalculadoraTrigonometrica
import math

# Crear una instancia de la calculadora trigonométrica
calc_trig = CalculadoraTrigonometrica()

# Realizar operaciones trigonométricas
resultado = calc_trig.seno(math.pi/2)  # Retorna 1.0
resultado = calc_trig.coseno(0)  # Retorna 1.0
resultado = calc_trig.tangente(math.pi/4)  # Retorna 1.0

# Convertir entre grados y radianes
radianes = calc_trig.grados_a_radianes(180)  # Retorna π
grados = calc_trig.radianes_a_grados(math.pi)  # Retorna 180.0
```

## Desarrollo

1. Clona este repositorio
2. Crea un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
3. Instala las dependencias de desarrollo:
   ```bash
   pip install -r requirements.txt
   ```
4. Instala el paquete en modo desarrollo:
   ```bash
   pip install -e .
   ```

## Ejecutar Pruebas

```bash
python -m unittest tests/test_calculadora.py
```

## Buenas Prácticas Implementadas

1. **Programación Orientada a Objetos**: Uso de herencia y clases abstractas
2. **Modularidad**: Separación de responsabilidades en módulos
3. **Documentación**: Docstrings detallados para clases y métodos
4. **Tipado**: Uso de type hints para mejor mantenibilidad
5. **Pruebas**: Cobertura completa de pruebas unitarias
6. **Manejo de Errores**: Validación de entrada y manejo de excepciones
7. **Encapsulamiento**: Uso de propiedades para acceso controlado
8. **Código Limpio**: Nombres descriptivos y estructura clara

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo LICENSE para más detalles.
