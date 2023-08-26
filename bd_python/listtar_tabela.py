#!python3
from db import nova_conexao
from mysql.connector import ProgrammingError

with nova_conexao() as conexao:
        cursor= conexao.cursor()
        cursor.execute('SHOW TABLES')
        
        #FOR para mostrar as tabelas em ordem
        for i, table in enumerate(cursor, start=1):
                print(f'Tabela {i}: {table[0]}')