descricaoFilme = {
    'titulo':'Homem de Ferro',
    'anoLancamento': 2012,
    'nota': 8.5,
    'genero': ['acao','aventura','drama']
}

# 1 - Para recuperar um elemento do dicionario
print(descricaoFilme['genero'])
print(descricaoFilme.get('anoLancamento'))

# 2 - Buscar apenas as chaves do dicionario
print(descricaoFilme.keys())

# 3 - Buscar apenas os valores
print(descricaoFilme.values())

# 4 - Buscar itens do dicionario com chaver e valores
print(descricaoFilme.items())

# 5 - Adicionar itens no dicionario
descricaoFilme['diretor'] = 'Wayer Morth'
print(descricaoFilme)

# 6 - Atualizar itens no dicionario 
descricaoFilme.update({'nota':8.9})
print(descricaoFilme)

# 7 - Remover itens no dicionario
descricaoFilme.pop('diretor')
print(descricaoFilme)