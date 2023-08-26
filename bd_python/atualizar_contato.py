#!python3

from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql = "UPDATE contatos SET nome = %s WHERE id = %s"
args = ('Robson',5)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'Os dados atualizados foram: {args}')