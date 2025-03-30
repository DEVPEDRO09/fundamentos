# listando valores de 0 a 10 que sejam menores do que 8
# listaNumeros = [ i for i in range (10) if i < 8]
# print(listaNumeros)

# lista de filme 
listaFilme = [
    "Titanic", "O Poderoso Chefão", "Clube da Luta", "Pulp Fiction", "Interestelar",
    "A Origem", "Forrest Gump", "Os Vingadores", "O Senhor dos Anéis: A Sociedade do Anel",
    "O Senhor dos Anéis: As Duas Torres", "O Senhor dos Anéis: O Retorno do Rei",
    "Matrix", "De Volta para o Futuro", "O Rei Leão", "Toy Story", "Homem-Aranha",
    "Homem-Aranha 2", "Homem-Aranha 3", "O Espetacular Homem-Aranha", "O Espetacular Homem-Aranha 2",
    "Homem-Aranha: De Volta ao Lar", "Homem-Aranha: Longe de Casa", "Homem-Aranha: Sem Volta para Casa",
    "Capitão América: O Primeiro Vingador", "Capitão América: O Soldado Invernal",
    "Capitão América: Guerra Civil", "Doutor Estranho", "Pantera Negra", "Thor", "Thor: O Mundo Sombrio",
    "Thor: Ragnarok", "Thor: Amor e Trovão", "Guardiões da Galáxia", "Guardiões da Galáxia Vol. 2",
    "Guardiões da Galáxia Vol. 3", "O Incrível Hulk", "Homem de Ferro", "Homem de Ferro 2", "Homem de Ferro 3",
    "Batman Begins", "Batman: O Cavaleiro das Trevas", "Batman: O Cavaleiro das Trevas Ressurge",
    "O Esquadrão Suicida", "Esquadrão Suicida", "Mulher-Maravilha", "Mulher-Maravilha 1984",
    "Aquaman", "Shazam!", "Adão Negro", "Liga da Justiça", "Zack Snyder’s Liga da Justiça",
    "Flash", "Coringa", "Superman: O Filme", "Superman II", "Superman: O Retorno",
    "O Homem de Aço", "O Exterminador do Futuro", "O Exterminador do Futuro 2: O Julgamento Final",
    "O Exterminador do Futuro 3: A Rebelião das Máquinas", "O Exterminador do Futuro: A Salvação",
    "O Exterminador do Futuro: Gênesis", "O Exterminador do Futuro: Destino Sombrio",
    "Rocky: Um Lutador", "Rocky II", "Rocky III", "Rocky IV", "Rocky V", "Rocky Balboa",
    "Creed: Nascido para Lutar", "Creed II", "Creed III", "Velozes e Furiosos",
    "Velozes e Furiosos 2", "Velozes e Furiosos: Desafio em Tóquio", "Velozes e Furiosos 4",
    "Velozes e Furiosos 5: Operação Rio", "Velozes e Furiosos 6", "Velozes e Furiosos 7",
    "Velozes e Furiosos 8", "Velozes e Furiosos 9", "Velozes e Furiosos 10",
    "Hobbs & Shaw", "Missão: Impossível", "Missão: Impossível 2", "Missão: Impossível 3",
    "Missão: Impossível – Protocolo Fantasma", "Missão: Impossível – Nação Secreta",
    "Missão: Impossível – Efeito Fallout", "Missão: Impossível – Acerto de Contas",
    "Harry Potter e a Pedra Filosofal", "Harry Potter e a Câmara Secreta",
    "Harry Potter e o Prisioneiro de Azkaban", "Harry Potter e o Cálice de Fogo",
    "Harry Potter e a Ordem da Fênix", "Harry Potter e o Enigma do Príncipe",
    "Harry Potter e as Relíquias da Morte – Parte 1", "Harry Potter e as Relíquias da Morte – Parte 2",
    "Animais Fantásticos e Onde Habitam", "Animais Fantásticos: Os Crimes de Grindelwald",
    "Animais Fantásticos: Os Segredos de Dumbledore", "A Freira", "Invocação do Mal",
    "Invocação do Mal 2", "Invocação do Mal 3: A Ordem do Demônio", "Annabelle",
    "Annabelle 2: A Criação do Mal", "Annabelle 3: De Volta para Casa", "It: A Coisa",
    "It: Capítulo Dois", "O Iluminado", "Doutor Sono", "A Hora do Pesadelo",
    "Sexta-Feira 13", "O Massacre da Serra Elétrica", "Pânico", "Pânico 2", "Pânico 3",
    "Pânico 4", "Pânico 5", "Jogos Mortais", "Jogos Mortais 2", "Jogos Mortais 3",
    "Jogos Mortais 4", "Jogos Mortais 5", "Jogos Mortais 6", "Jogos Mortais 7",
    "Jogos Mortais: Jigsaw", "Jogos Mortais X", "Halloween", "Halloween Kills",
    "Halloween Ends", "O Chamado", "O Chamado 2", "O Grito", "O Grito 2",
    "A Bruxa", "Hereditário", "Midsommar", "Corra!", "Nós", "Fragmentado",
    "Vidro", "O Sexto Sentido", "Um Lugar Silencioso", "Um Lugar Silencioso 2",
    "A Chegada", "Duna", "Blade Runner", "Blade Runner 2049", "O Planeta dos Macacos",
    "O Planeta dos Macacos: O Confronto", "O Planeta dos Macacos: A Guerra",
    "Guerra Mundial Z", "Eu Sou a Lenda", "O Dia Depois de Amanhã", "2012",
    "Armageddon", "Impacto Profundo", "O Inferno de Dante", "San Andreas",
    "Terremoto: A Falha de San Andreas", "O Impossível", "Naufrago",
    "A Rede Social", "Steve Jobs", "O Lobo de Wall Street", "A Grande Aposta",
    "Ford vs Ferrari", "Rush: No Limite da Emoção", "Senna", "Whiplash",
    "Bohemian Rhapsody", "Elvis", "Rocketman", "Yesterday", "A Star Is Born",
    "Os Miseráveis", "Chicago", "O Rei do Show", "La La Land", "Mamma Mia!",
    "Mamma Mia! Here We Go Again", "Grease", "Dirty Dancing", "Flashdance",
    "Footloose", "High School Musical", "Camp Rock", "Encanto", "Moana",
    "Frozen", "Frozen 2", "Ratatouille", "Procurando Nemo", "Procurando Dory",
    "Toy Story 2", "Toy Story 3", "Toy Story 4", "Up: Altas Aventuras",
    "Divertida Mente", "Os Incríveis 2", "Carros", "Carros 3", "Valente",
    "A Bela e a Fera", "A Pequena Sereia", "Aladdin", "O Corcunda de Notre Dame",
    "O Rei Leão (2019)", "Dumbo", "A Dama e o Vagabundo", "Cruella",
    "Malévola", "Malévola: Dona do Mal", "Piratas do Caribe", "Piratas do Caribe: O Baú da Morte",
    "Piratas do Caribe: No Fim do Mundo", "Piratas do Caribe: Navegando em Águas Misteriosas",
    "Piratas do Caribe: A Vingança de Salazar", "O Estranho Mundo de Jack",
    "Coraline", "Frankenweenie", "A Noiva Cadáver", "A Família Addams",
    "Hotel Transilvânia", "Hotel Transilvânia 2", "Hotel Transilvânia 3",
    "Hotel Transilvânia: Transformonstrão"
]

# 1 - Filmes que possuem letra 'e'
filmesComE = [filme for filme in listaFilme if 'e' in filme.lower()]
print('Nomes de filmes que possuem a letra "e"')
print(filmesComE)

# 2 - Mostrar filme assistido Obs: Homem-Aranha e Piratas do Caribe
filmeAssistido = [filme for filme in listaFilme if filme != 'Homem-Aranha''Piratas do Caribe']
print('Lista de filmes assistidos( excluindo " Homem-Aranha " e " Pirartas do Caribe "):')
print(filmeAssistido)

# 3 - Encontrando um filme pelo nome
while True:
    procurar = input('Digite o nome do filme (ou "sair" para encerrar.):\n')
    if procurar.lower() == 'sair':
        print('programa encerrado.')
        break 

# Mostrar filmes com o nome pesquisado
    tabelafilme = [filme for filme in listaFilme if procurar.lower() in filme.lower()]

    if tabelafilme:
        print(f'\nFilmes encontrado com {procurar}')
        for filmeEncontrado in tabelafilme:
            print(filmeEncontrado)
    
    else:
        print(f'\nNenhum filme foi encontrado pelo nome {procurar}.')
        print(f'Tente novamente.')

