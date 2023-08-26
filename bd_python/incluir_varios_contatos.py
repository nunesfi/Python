#!python3
from mysql.connector.errors import ProgrammingError
from db import nova_conexao

#Neste exemplo estamo utilizando os parametros do python para inserir dados na tabela contatos

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = (
    ('Filipi', '91834-5978'),
    ('Bruna', '96234-5678'),
    ('Vania', '91734-5178'),
    ('Caroline', '91934-0678'),
    ('Cicera', '91230-5578'),
    ('Nilson', '91224-5678'),
    ('Carolina', '95234-5688'),
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        #Chamando o sql e meu argumento Python / executemany (executa vários comandos diretamente)
        # commit realizada a execução no banco
        cursor.executemany(sql,args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    #Caso não ocorra erro ele mostrará o id do contato incluído na tabela
    else:
        print(f'Foram incluídos: {cursor.rowcount} registros!' )