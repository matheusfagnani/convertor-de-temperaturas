import pytest
from conversores_temp import converter_temperatura

# test_conversor.py
import pytest
from conversores_temp import converter_temperatura

@pytest.mark.parametrize("valor, de_escala, para_escala, esperado", [
    (0, 'Celsius', 'Fahrenheit', 32),
    (100, 'Celsius', 'Kelvin', 373.15),
    (32, 'Fahrenheit', 'Celsius', 0),
    (212, 'Fahrenheit', 'Kelvin', 373.15),
    (273.15, 'Kelvin', 'Celsius', 0),
    (373.15, 'Kelvin', 'Fahrenheit', 212),
    (50, 'Celsius', 'Celsius', 50),
    (50, 'Kelvin', 'Kelvin', 50),
])
def test_converter_temperatura(valor, de_escala, para_escala, esperado):
    resultado = converter_temperatura(valor, de_escala, para_escala)
    # Usando aproximação para floats
    assert resultado == pytest.approx(esperado, abs=1e-4)



    





