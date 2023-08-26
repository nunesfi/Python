# Map

lista_1 = [2, 4, 6]
dobro = map(lambda x: x * 2, lista_1)
print (list(dobro))

nomes = [
    {'nome': 'Filipi', 'idade': 29},
    {'nome': 'Bruna', 'idade': 27},
    {'nome': 'Augusto', 'idade': 1},
    {'nome': 'Catarina', 'idade': 1},
]

so_nomes = map(lambda p: p['nome'], nomes)
print(list(so_nomes))

so_idade = map(lambda p: p['idade'], nomes)
print(list(so_idade))

# Desafio - Exibir o dicionário acima em forma de frase usando lambda

frase = map(lambda p: f'{p["nome"]} tem {p["idade"]} anos.', nomes)
print(list(frase))
