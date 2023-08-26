#!python3
from mysql.connector.errors import ProgrammingError
from db import nova_conexao

#Neste exemplo estamo utilizando os parametros do python para inserir dados na tabela contatos

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = ('Filipi', '91234-5678')

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        #Chamando o sql e meu argumento Python
        cursor.execute(sql,args)
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    #Caso não ocorra erro ele mostrará o id do contato incluído na tabela
    else:
        print('1 Registro incluído, ID: ', cursor.lastrowid)