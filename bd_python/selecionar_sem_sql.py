#!python3

# SQL_INJECTION - Quando o usuario em seu input passa uma sintaxe SQL
# Fazendo com que o sistema possa ser danificado.
# Por isso é colocado uma variavel onde é incluido os argumentos, e a lib do sql ao realzar o merge
# Processa e trata estas infromações

from db import nova_conexao

sql = "SELECT * FROM contatos WHERE nome like %s"

with nova_conexao() as conexao:
    #recebendo o input do usuario
    nome = input('Contato a localizar: ')

    #criando uma tupla para passar o input para os argumentos
    args = (f'%{nome}%', )
    cursor = conexao.cursor()
    cursor.execute(sql, args)

    for x in cursor:
        print(x)
