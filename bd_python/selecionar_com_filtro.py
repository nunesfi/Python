#!python3
from db import nova_conexao

sql = ("SELECT * FROM  contatos WHERE tel = '91834-5978'")

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    for x in cursor:
        print(x)