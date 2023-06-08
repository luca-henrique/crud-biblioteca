import datetime
import sqlite3

from cliente import listar_cliente
from funcionario import listar_funcionario
from livro import listar_livro

# conexão com o banco de dados
conn = sqlite3.connect('db.db')

criarTabela = f'CREATE TABLE IF NOT EXISTS ALUGUEL (id INTEGER PRIMARY KEY AUTOINCREMENT,livro_id integer NOT NULL,cliente_id integer NOT NULL,funcionario_id integer NOT NULL,data_aluguel DATETIME NOT NULL,data_devolucao DATETIME NOT NULL,FOREIGN KEY (livro_id) REFERENCES livro(id),FOREIGN KEY (cliente_id) REFERENCES cliente(id),FOREIGN KEY (funcionario_id) REFERENCES funcionario(id));'

# criação da tabela clientes
conn.execute(criarTabela)

conn.commit()


def alugar_livro():
    listar_livro()
    livro_id = input("Digite o id do livro: ")

    listar_cliente()
    cliente_id = input("Digite o id do cliente: ")

    listar_funcionario()
    funcionario_id = input("Digite o id do funcionario: ")

    data_aluguel = datetime.datetime.now()

    data_devolucao = data_aluguel + datetime.timedelta(days=3)

    conn.execute(
        'INSERT INTO ALUGUEL (livro_id, cliente_id, funcionario_id,data_aluguel,data_devolucao) VALUES (?, ?, ?,?,?)', (livro_id, cliente_id, funcionario_id, data_aluguel, data_devolucao))
    conn.commit()

    print("Cliente adicionado com sucesso!")


def deletar_aluguel():
    id = int(input("Digite o ID do aluguel que deseja deletar: "))
    res = conn.execute(f"SELECT id FROM ALUGUEL WHERE id={id}")

    if res.fetchone() is not None:
        conn.execute(f"DELETE FROM ALUGUEL WHERE ID={id}")
        conn.commit()
        print("ALUGUEL deletado com sucesso!")
    else:
        print("ALUGUEL não existe")


def listar_funcionario():
    conn.execute('SELECT * FROM funcionario')
    rows = conn.fetchall()
    for row in rows:
        print(row)
