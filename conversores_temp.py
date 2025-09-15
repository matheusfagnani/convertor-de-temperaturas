# criando um conversor de temperaturas entre Celsius, Fahrenheit e Kelvin

def converter_temperatura (valor, de_unidade, para_unidade):

    # conveersao de celsius para fahrenheit
    if de_unidade == 'C':
        if para_unidade == 'F':
            return (valor * 9/5) + 32
        elif para_unidade == 'K':
            return valor + 273.15



