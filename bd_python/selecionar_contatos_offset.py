#!python3
from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql = 'SELECT * FROM contatos LIMIT 3 OFFSET 3'

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        #Incluindo o comando fetchall para trazer toda a tabela consultada
        contatos = cursor.fetchall()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        #Percorrer a lista de contatos para exibição
        for contato in contatos:
            # 2d (2 digitos), 20s (20 caracteres)
            print(f'{contato[2]:2d} - {contato[0]:10s} Telefone: {contato[1]}')