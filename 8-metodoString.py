nomeFilme = 'Top Gun'

filmeDescricao = '''Top Gun Maverick, é um filme
de aviação muito forte na industria'''

print(nomeFilme.lower()) # Fica tudo minusculo
print(nomeFilme.upper()) # Fica tudo maiusculo
print(nomeFilme.capitalize()) # Simple a primeiro fica maiuscula
print(nomeFilme.title()) # Simple a primeiro fica maiuscula
print(nomeFilme.split(',')) #  divide pelo virgula na caso (' , ')
print(nomeFilme.replace('Gun','Master')) # Altera o elemento por outro
print(nomeFilme.find('u')) # Retorna a posição de um determinado caractere
print(nomeFilme.find('o')) # Conta os caracteres
print(nomeFilme.center(10,'-')) # Retorna a string centralizada com caractere de preenchimento

