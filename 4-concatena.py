# Concatenando Valores 

nome = input('digite o nome do filme:\n')
anoLancamento = int(input('Digite o ano de lançamento:\n'))
notaFilme = float(input('Digite a nota do filme:\n'))

print('------ Dados do filme ------')
print()
# tipo 1
print('Nome do filme:',nome)
print('Ano de lançamento:',anoLancamento)
print('Nota do filme',notaFilme)
print()
# tipo 2
print('Nome do filme:',nome, '\nAno lançamento:',anoLancamento, '\nNota do filme:',notaFilme)
print()
# tipo 3
print(f'Nome:{nome}\n'
      f'Ano de lançamento:{anoLancamento}\n'
      f'Nota do filme:{notaFilme}\n'
      )
