import sqlite3

conn = sqlite3.connect('db.db')
cursor = conn.cursor()

criarTabela = f'CREATE TABLE IF NOT EXISTS funcionario (id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT NOT NULL,salario REAL NOT NULL,cargo TEXT NOT NULL);'

cursor.execute(criarTabela)


def listar_funcionario():
    cursor.execute('SELECT * FROM funcionario')
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def adicionar():
    nome = input('Digite o nome do funcionário: ')
    salario = float(input('Digite o salário do funcionário: '))
    cargo = input('Digite o cargo do funcionário: ')
    cursor.execute(
        'INSERT INTO funcionario (nome, salario, cargo) VALUES (?, ?, ?)', (nome, salario, cargo))
    conn.commit()
    print('Funcionário adicionado com sucesso!')


def atualizar():
    id = int(input('Digite o ID do funcionário que deseja atualizar: '))

    res = conn.execute(f"SELECT id FROM funcionario WHERE id={id}")

    if res.fetchone() is not None:

        nome = input('Digite o novo nome do funcionário: ')
        salario = float(input('Digite o novo salário do funcionário: '))
        cargo = input('Digite o novo cargo do funcionário: ')
        cursor.execute(
            'UPDATE funcionario SET nome=?, salario=?, cargo=? WHERE id=?', (nome, salario, cargo, id))
        conn.commit()
        print('Funcionário atualizado com sucesso!')

    else:
        print('Funcionário não existe!')


def excluir():
    id = int(input('Digite o ID do funcionário que deseja excluir: '))

    res = conn.execute(f"SELECT id FROM funcionario WHERE id={id}")

    if res.fetchone() is not None:
        cursor.execute('DELETE FROM funcionario WHERE id=?', (id,))
        conn.commit()
        print('Funcionário excluído com sucesso!')

    else:
        print('Funcionário não existe!')
