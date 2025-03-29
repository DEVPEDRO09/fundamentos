# informações  sobre o filme
nome = input('Digite o nome do filme:\n')
anoLancamento = int(input('Digite o ano de lançamento:\n'))
avaliacao = float(input('Digite a avaliação do filme:\n'))

# verificar se o filme é recomendado 
if avaliacao > 8.0 and anoLancamento > 2015:
    print(f'O filme {nome} é muito bom, recomendo.')

else:
    print(f'O filme {nome} ainda não atingiu uma nota boa.')

"""-----------------------------------------------------------"""

num1 = float(input('Digite o primeiro número:\n'))
num2 = float(input('Digite o segundo número:\n'))
operacao = input('Digite a operacão a ser realizada: ( + - * / )\n')

if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    if num2 != 0:
        resultado = 0
else:
    print('Operção Invalida...')
    resultado = 0

print(f'O resultado é:{resultado:.2f}')