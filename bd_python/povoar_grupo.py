from db import nova_conexao
from mysql.connector.errors import ProgrammingError

sql = 'INSERT INTO grupos (descricao) VALUES(%s)'
args = (
    ('Familia',),
    ('Trabalho',),
    ('Igreja',),
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro ao povoar a tabela {e.msg}')
    else:
        print(f'Foram inseridos {cursor.rowcount} dados com sucesso.')

        'Filipi'
'Bruna' 
'Vania' 
'Robson'
'Cicera'
'Nilson'