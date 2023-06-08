import sqlite3

# conexão com o banco de dados
conn = sqlite3.connect('db.db')

criarTabelaCliente = f'CREATE TABLE IF NOT EXISTS cliente (id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT NOT NULL,email TEXT NOT NULL,telefone TEXT NOT NULL);'

# criação da tabela clientes
conn.execute(criarTabelaCliente)

conn.commit()

# função para criar um cliente


def criar_cliente():
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o e-mail do cliente: ")
    telefone = input("Digite o telefone do cliente: ")

    conn.execute(f"INSERT INTO cliente (NOME, EMAIL, TELEFONE) \
                 VALUES ('{nome}', '{email}', '{telefone}')")
    conn.commit()
    print("Cliente adicionado com sucesso!")

# função para atualizar um cliente


def atualizar_cliente():
    id = input("Digite o id do cliente: ")
    res = conn.execute(f"SELECT id FROM cliente WHERE id={id}")

    if res.fetchone() is not None:

        nome = input("Digite o novo nome do cliente: ")
        email = input("Digite o novo e-mail do cliente: ")
        telefone = input("Digite o novo telefone do cliente: ")
        conn.execute(f"UPDATE cliente SET NOME='{nome}', EMAIL='{email}', TELEFONE='{telefone}' \
                 WHERE ID={id}")
        conn.commit()
        print("Cliente atualizado com sucesso!")

    else:
        print("Cliente não existe!")


# função para deletar um cliente


def deletar_cliente():
    id = int(input("Digite o ID do cliente que deseja deletar: "))
    res = conn.execute(f"SELECT id FROM cliente WHERE id={id}")

    if res.fetchone() is not None:
        conn.execute(f"DELETE FROM CLIENTE WHERE ID={id}")
        conn.commit()
        print("Cliente deletado com sucesso!")

    else:
        print("Cliente não existe!")

# função para exibir todos os clientes


def listar_cliente():
    cursor = conn.execute("SELECT * FROM cliente")
    for row in cursor:
        print(row)
