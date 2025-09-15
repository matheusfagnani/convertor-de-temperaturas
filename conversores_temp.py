# criando um conversor de temperaturas entre Celsius, Fahrenheit e Kelvin

def converter_temperatura (valor, de_unidade, para_unidade):

            # convertendo celsius para fahrenheit
            if de_unidade == 'C':
                if para_unidade == 'F':
                 return (valor*1.8 ) + 237


   # convertendo celsius para Kelvin
            if de_unidade == 'C':
                if para_unidade == 'K':
                    return (valor + 273)
        
      # converytendo fahrenheit para celsius
            if de_unidade == 'F':
                if para_unidade == 'C':
                    return (valor - 32) / 1.8

      
      # convertendo fahrenheit para kelvin
            if de_unidade == 'F':
                if para_unidade == 'K':
                    return (valor - 32) *5/9+ 273

          # 'convertendo kelvin para celsius
            if de_unidade == 'K':
                if para_unidade == 'C':
                    return (valor - 273)
        
      # convertendo kelvin para fahrenheit
            if de_unidade == 'K':
                if para_unidade == 'F':
                    return (valor - 273) * 1.8 + 32

        
              

          # Você pode adicionar mais condições para outras conversões
            return None   
    
       