#!python3
from mysql.connector.pooling import connect
from contextlib import contextmanager

# Tive que realizar a alterarção do parametros para dicionárioa função connect espera receber um dicionário e não uma tupla

#parametros = connect(
#    host='localhost',
#    port=3306,
#    user='root',
#    passwd='Fnunes@1234',
#    database='agenda'
#)

parametros = {
    'host':'localhost',
    'port': 3306,
    'user': 'root',
    'passwd' :'Fnunes@1234',
    'database': 'agenda'
}

@contextmanager
def nova_conexao():
    conexao = connect(**parametros)
    try:
        yield conexao
    finally:
        if (conexao and conexao.is_connected()):
            print('finalizando...saindo do bloco')
            conexao.close()
