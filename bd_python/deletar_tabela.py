#!python3
from db import nova_conexao
from mysql.connector import ProgrammingError

deletar_tabela = """
    DROP TABLE emails
"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(deletar_tabela) # Posso colocar o comando diretamente no EXECUTE "DROP TABLE emails"
    except ProgrammingError as e:
        print(f'Erro ao Deletar tabela', {e})
