#!python3
from db import nova_conexao

#Usando a conexão do BD dentro do bloco

with nova_conexao() as conexao:
    if conexao.is_connected():
        print('Conectado!')

print("Fim!")