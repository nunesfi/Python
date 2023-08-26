#!python3
from db import nova_conexao

sql = 'SELECT tel, nome FROM contatos'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    #Retorna somente um registro
    print(cursor.fetchone())