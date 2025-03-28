import pprint


descricaoFilmes = {
    'Homem de Ferro':{
        'anoLancamento': 2012,
        'nota': 8.5,
        'genero': ['acao','drama']
    },
    'flash':{
        'anoLancamento': 2012,
        'nota': 8.0,
        'genero': ['acao','aventura','crime']
    },  
    'Homem Aranha':{
        'anoLancamento': 2012,
        'nota': 7.5,
        'genero': ['acao','aventura','frito']
    },
    'Titanic':{
        'anoLancamento': 2012,
        'nota': 8.5,
        'genero': ['real','romance','drama']
}
}

pp = pprint.PrettyPrinter(depth=6)
pp.pprint(descricaoFilmes)

# 1 - Buscar uma informação dentro de um dicionario aninhado
print(descricaoFilmes['Titanic']['genero'])

# 2 - Adicionar novo item 
descricaoFilmes['Homem de Ferro']['diretor'] = 'Pedro Backer'
print(descricaoFilmes['Homem de Ferro'])

# 3 - excluir um dicionario
del descricaoFilmes['flash']
pp.pprint(descricaoFilmes)
