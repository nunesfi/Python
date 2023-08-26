# Filter

pessoas = [
    {'nome': 'Filipi', 'idade': 29},
    {'nome': 'Bruna', 'idade': 27},
    {'nome': 'Augusto', 'idade': 1},
    {'nome': 'Catarina', 'idade': 2},
    {'nome': 'Laura', 'idade': 5},
    {'nome': 'Vânia', 'idade': 62},
]

# No filter a função lambda sempre trará um resultado verdadeiro ou falso
menores = filter(lambda p: p['idade'] < 10, pessoas)
print(list(menores))

#Desafio
maiores_nomes = filter(lambda p: len(p['nome']) >= 7, pessoas)
print(tuple(maiores_nomes))

