#!python3
from db import nova_conexao

sql = 'SELECT tel, nome FROM contatos'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)
    
    for contato in cursor.fetchall:
        # list compreehension: \t dar uma tabulação,no join em cada contato percorrido, vamos pegar os atributos
        # e fazer um join entre eles. com sso vamos pegar todos os campos e converter para string e fazer a junção
        print('\t'.join(str(campo) for campo in contato))