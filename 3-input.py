# Utilizando o Input

nome = input ('Digite o nome do filme:\n')
anoLancamento = int(input('Digite o ano de lançamento:\n'))
notafilme = float(input('Digite a nota do filme:\n'))

print(type(nome))
print(type(anoLancamento))
print(type(notafilme))

print(f'Nome:{nome}\n'
      f'Ano de Lançamento:{anoLancamento}\n'
      f'Nota:{notafilme}'
      )
