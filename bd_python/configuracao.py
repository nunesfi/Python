#!python3
from mysql.connector import connect

# conexão com BD MYSQL
conexao = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='Fnunes@1234'
)

print(conexao)