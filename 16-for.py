listaFilme = ['Titanic','Jurassic Park','Vingadores']
numeros = [ 10 , 20 , 30 , 40 , 50]


# 1 - Interando valores de uma lista 
for filme in listaFilme:
    print(filme)


# 2 - Quando a condição for atendida, o loop será encerrado
for numero in numeros:
    if numero == 40:
        break
    print(numero)

# 3 - Quando a condição for atendida, o loop vai para proxima interação
for filme in listaFilme:
    if filme == 'Jurassic Park':
        continue
    print(filme)

# 4 - Avaliação do filme
nomeFilme = input('Digite o nome do filme:\n')
avaliacaoFilme = int(input('Digite quantas avaliações deseja fazer:\n'))

total = 0
for i in range(avaliacaoFilme):
    nota = float(input('Digite a nota do filme:\n'))
    total += nota

if avaliacaoFilme > 0:
    average = total / avaliacaoFilme

else:
    average = 0

print(f'Media de avaliação do filme {nomeFilme} é: {average:.2f}')