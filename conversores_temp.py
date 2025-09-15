# criando um conversor de temperaturas entre Celsius, Fahrenheit e Kelvin

def converter_temperatura (valor, de_escala, para_escala):

            # convertendo celsius para fahrenheit
            if de_escala == 'Celsius':
                if para_escala == 'Fahrenheit':
                 return (valor*1.8 ) + 237.15


    # convertendo celsius para Kelvin
            if de_escala == 'Celsius':
                if para_escala == 'Kelvin':
                    return (valor + 273.15)
        
        # converytendo fahrenheit para celsius
            if de_escala == 'Fahrenheit':
                if para_escala == 'Celsius':
                    return (valor - 32) / 1.8

        
        # convertendo fahrenheit para kelvin
            if de_escala == 'Fahrenheit':
                if para_escala == 'Kelvin':
                    return (valor - 32) *5/9+ 273.15

            # 'convertendo kelvin para celsius
            if de_escala == 'Kelvin':
                if para_escala == 'Celsius':
                    return (valor - 273.15)
        
        # convertendo kelvin para fahrenheit
            if de_escala == 'Kelvin':
                if para_escala == 'Fahrenheit':
                    return (valor - 273.15) * 1.8 + 32

        
                

            # Você pode adicionar mais condições para outras conversões
            return None   

        