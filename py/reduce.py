# Reduce
# Composta por 2 parametros, 1º acumulador, 2º parametro atual

from functools import reduce

pessoas = [
    {'nome': 'Filipi', 'idade': 29},
    {'nome': 'Bruna', 'idade': 27},
    {'nome': 'Augusto', 'idade': 1},
    {'nome': 'Catarina', 'idade': 2},
    {'nome': 'Laura', 'idade': 5},
    {'nome': 'Vânia', 'idade': 62},
]

# map
so_idade = map(lambda p: p['idade'], pessoas)

#filter
menores = filter(lambda idade: idade < 10, so_idade)

# Reduce
# Neste exemplo de reduce colocamos primeiro o acumulador (idades) depois o parametro atual
# com isso vamos somar a idade com a idade da pessoa que esta no dicionário
# depois informar de onde quero pegar estas informações
# por ultimo posso colocar um parametro de inicialização do meu acumulador (0)
soma_idades = reduce(lambda idades, idade: idades + idade, list(menores), 0)
print(soma_idades)

