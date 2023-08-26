#!python3
from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='Fnunes@1234'
)

#Criando um database através do Python
cursor = conexao.cursor()
cursor.execute('CREATE DATABASE agenda')

