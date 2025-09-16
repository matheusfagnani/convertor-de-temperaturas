import pytest
from conversores_temp import converter_temperatura

def test_celsius_para_fahrenheit():
    assert converter_temperatura(0, "Celsius", "Fahrenheit") == 32.0
    assert converter_temperatura(100, "Celsius", "Fahrenheit") == 212.0

def test_celsius_para_kelvin():
    assert converter_temperatura(0, "Celsius", "Kelvin") == 273.15
    assert converter_temperatura(100, "Celsius", "Kelvin") == 373.15

def test_fahrenheit_para_celsius():
    assert converter_temperatura(32, "Fahrenheit", "Celsius") == 0.0
    assert converter_temperatura(212, "Fahrenheit", "Celsius") == 100.0

def test_fahrenheit_para_kelvin():
    assert converter_temperatura(32, "Fahrenheit", "Kelvin") == 273.15
    assert converter_temperatura(212, "Fahrenheit", "Kelvin") == 373.15

def test_kelvin_para_celsius():
    assert converter_temperatura(273.15, "Kelvin", "Celsius") == 0.0
    assert converter_temperatura(373.15, "Kelvin", "Celsius") == 100.0

def test_kelvin_para_fahrenheit():
    assert converter_temperatura(273.15, "Kelvin", "Fahrenheit") == 32.0
    assert converter_temperatura(373.15, "Kelvin", "Fahrenheit") == 212.0

# Teste de mesma escala
def test_mesma_escala():
    assert converter_temperatura(100, "Celsius", "Celsius") == 100.0
    assert converter_temperatura(212, "Fahrenheit", "Fahrenheit") == 212.0
    assert converter_temperatura(273.15, "Kelvin", "Kelvin") == 273.15

# Testes de escalas inválidas
def test_escalas_invalidas():
    with pytest.raises(ValueError, match="Escala de temperatura inválida"):
        converter_temperatura(100, "Celsio", "Fahrenheit")
    with pytest.raises(ValueError, match="Escala de temperatura inválida"):
        converter_temperatura(100, "Celsius", "Kelv")
    with pytest.raises(ValueError, match="Escala de temperatura inválida"):
        converter_temperatura(100, "X", "Y")

# Teste de valor inválido para Kelvin
def test_kelvin_negativo():
    with pytest.raises(ValueError, match="Temperatura em KELVIN não pode ser negativa"):
        converter_temperatura(-1, "Kelvin", "Celsius")



    





