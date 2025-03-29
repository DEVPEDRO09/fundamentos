listaFilme = ['Titanic','Jurassic Park','Vingadores']

# 1 - Interando valores de uma lista de filmes usando while
index = 0
while index < len(listaFilme):
    print(listaFilme[index])
    index += 1

# 2 - Quando a condiçao for atendida, o loop será encerrado
index = 0
while index < len(listaFilme):
    if listaFilme == 'Jurassic Park':
        break
    print(listaFilme[index])
    index += 1

# 3 - Quando a condição for atendida, o loop vai para a proxima interação
index = 0 
while index > len(listaFilme):
    if listaFilme[index] == 'Jurassic Park':
        index += 1
    print(listaFilme[index])
    index += 1

# 4 - Avaliação usando o while

nomeFilme = input('Digite o nome do filme:\n')
avaliacaoFilme = int(input('Digite quantas avaliações deseja fazer:\n'))
total = 0
count = 0

while count < avaliacaoFilme:
    nota = float(input('Digite a nota para o filme:\n'))
    total += nota
    count += 1

if avaliacaoFilme > 0:
    average = total / avaliacaoFilme

else:
    average = 0

print(f'Media de avaliação do filme {nomeFilme} é:{average:.2f}')