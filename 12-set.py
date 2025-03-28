setFilmes = {'Velozes e Furiosos', 'Interestellar','Carros','Toys Story','Vingadores'}

# 1 - Buscar o tamanho do set 
print(len(setFilmes))

# 2 - True e 1 são considerado iguais
exemplose = {'Vingadores', True, 1, 8.7}
print(exemplose)

# 3 - Adicionar item de outro set 
setFilmes.update(exemplose)
print(setFilmes)

# 4 - Remover um item no set 
setFilmes.remove(True)
setFilmes.remove(8.7)
print(setFilmes)