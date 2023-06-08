import sqlite3

# conexão com o banco de dados
conn = sqlite3.connect('db.db')

criarTabela = f'CREATE TABLE IF NOT EXISTS livro (id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT NOT NULL,autor TEXT NOT NULL,categoria TEXT NOT NULL);'

# criação da tabela clientes
conn.execute(criarTabela)

conn.commit()


def criar_livro():
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor do livro: ")
    categoria = input("Digite em qual categoria o livro se encaixa: ")

    conn.execute(f"INSERT INTO LIVRO (nome, autor, categoria) \
                 VALUES ('{nome}', '{autor}', '{categoria}')")
    conn.commit()
    print("Livro adicionado com sucesso!")


def atualizar_livro():
    try:
        id = input("Digite o id do livro: ")

        res = conn.execute(f"SELECT id FROM livro WHERE id={id}")

        if res.fetchone() is not None:
            nome = input("Digite o nome do livro: ")
            autor = input("Digite o nome do autor do livro: ")
            categoria = input("Digite em qual categoria o livro se encaixa: ")

            conn.execute(f"UPDATE LIVRO SET nome='{nome}', autor='{autor}', categoria='{categoria}' \
        WHERE id={id}")
            conn.commit()

        print("Cliente atualizado com sucesso!")
    except NameError:
        print("Livro não existe")


def deletar_livro():
    id = int(input("Digite o ID do livro que deseja deletar: "))
    res = conn.execute(f"SELECT id FROM livro WHERE id={id}")

    if res.fetchone() is not None:
        conn.execute(f"DELETE FROM livro WHERE ID={id}")
        conn.commit()
        print("livro deletado com sucesso!")
    else:
        print("Livro não existe")


def listar_livro():
    cursor = conn.execute("SELECT * FROM livro")
    for row in cursor:
        print(row)
