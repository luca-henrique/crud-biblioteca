import mysql.connector

host = 'localhost'
db_user = 'root'
db_password = 'root@root'
db_name = 'biblioteca_db'

conexao = mysql.connector.connect(
    host=host,
    user=db_user,
    password=db_password,
    database=db_name,
)

cursor = conexao.cursor()


def createTable():
    criarTabela = f'CREATE TABLE IF NOT EXISTS TABLE_NAME (emp_id INT, emp_name CHAR);'
    cursor.execute(criarTabela)
    conexao.commit()


def createEvent():
    cidade = 'São Paulo'
    uf = 'SP'
    criarExemplo = f'INSERT INTO cidade (nome,uf) values ("{cidade}", "{uf}")'
    cursor.execute(criarExemplo)
    conexao.commit()
    return 'cidade criada com sucesso'


def readEvent():
    cursor.execute('select * from cidade')
    recset = cursor.fetchall()
    return recset


def updateEvent():
    id = 1
    cidade = 'São Paulo'
    uf = 'PE'
    updateExemplo = f'UPDATE cidade SET uf = "{uf}" where id = "{id}"'
    cursor.execute(updateExemplo)
    conexao.commit()
    return 'cidade atualizada com sucesso'


def deleteEvent():
    id = 1
    deleteExemplo = f'delete from cidade where id = "{id}"'
    cursor.execute(deleteExemplo)


print(createTable())

cursor.close()
conexao.close()
