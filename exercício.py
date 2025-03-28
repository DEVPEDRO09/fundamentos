""" 1- Escreva um programa que lê dois nomes e retorne uma string formatada no formato Últimonome, primeiroNome."""

primeiroNome = str(input('Digite o nome:\n'))
segundoNome = str(input('Digite o segundo nome:\n'))

formatNome = f'{segundoNome} {primeiroNome}'
print(formatNome)
""" 2 - Inverta a ordem das palvras em uma string fornecida."""

texto = 'Python é muito divertio'
palavra = texto.split()
textoInvertido = ' '.join(palavra[::-1])
print (textoInvertido)

""" 3 - Verifique se uma string fornecida é um palindromo"""

texto1 = 'arara'
texto2 = 'python'

texto1_formt = texto1.lower().replace(' ', '')
texto2_formt = texto2.lower().replace(' ', '')

palindromo1 = texto1_formt == texto1 [ ::-1]
palindromo2 = texto2_formt == texto2 [ ::-1]

print(palindromo1)
print(palindromo2)
