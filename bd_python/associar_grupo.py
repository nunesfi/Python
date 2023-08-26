from db import nova_conexao
from mysql.connector.errors import ProgrammingError

selecionar_grupo = 'SELECT id FROM grupos WHERE descricao = %s'
atualizar_contato = 'UPDATE contatos SET grupo_id = %s WHERE nome = %s'

#criar dicionario para associação
contato_grupo = {
    "Filipi": "Trabalho",
    "Bruna": "Familia",
    "Vania": "Familia",
    "Robson": "Trabalho",
    "Cicera": "Igreja",
    "Nilson": "Igreja",
}

with nova_conexao() as conexao:
    try:
        cursor= conexao.cursor()
        #Definir FOR para ter  o nome da pessoa e o grupo a qual pertence
        for contato, grupo in contato_grupo.items():
            cursor.execute(selecionar_grupo, (grupo,))
            grupo_id = cursor.fetchone()[0]
            cursor.execute(atualizar_contato, (grupo_id, contato))
            conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print('contatos associados')
