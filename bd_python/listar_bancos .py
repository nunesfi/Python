#!python3
from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='Fnunes@1234'
)

#Listando todos os bancos de dados

cursor = conexao.cursor()
cursor.execute('SHOW DATABASES')

for i, database in enumerate(cursor, start=1):
    print(f'Banco de Dados {i}: {database[0]}')

