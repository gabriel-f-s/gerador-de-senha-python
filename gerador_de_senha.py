# Gerador de senha randômica

import random
caixa_baixa = "abcdefghijklmnopqrstuvwxyz"
caixa_alta = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
números = "123456789"
símbolos = '!@#$%&*?'

use = caixa_baixa + caixa_alta + números + símbolos
tamanho_da_senha = 8

senha = "".join(random.sample(use, tamanho_da_senha))

print(f'Sua senha é: {senha}')
