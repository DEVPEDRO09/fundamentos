listaFilmes = ['Velozes e Furiosos', 'Interestellar','Carros','Toys Story','Vingadores']

# 1 - tamanho da lista
print(len(listaFilmes))

# 2 - recuperar um iten da lista pelo nome
print(listaFilmes.index('Carros'))

# 3 - Adicionar item ao final da lista 
listaFilmes.append('Senhor dos Anéis')
print(listaFilmes)

# 4 - Ordenar a lista por ordem alfabetica
listaFilmes.sort()
print(listaFilmes)

# 5 - Passar de uma lista até a outra
filmeCopy = listaFilmes.copy()
print(filmeCopy)

# 6 - Remover iten 
filmeCopy.remove('Interestellar')
print(filmeCopy)

# 7 - Remover todos os itens da lista 
listaFilmes.clear()
print(listaFilmes)