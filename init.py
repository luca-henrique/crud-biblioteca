from src.model.Cliente import Cliente
from src.controller.Cliente import PessoaController
cria = PessoaController()

while True:
    opcao = int(input('1 ou 2'))

    if opcao == 1:
        pi = Cliente('Lucas', 10)
        cria.salvar_pessoa(pi)

    elif opcao == 2:
       for i in (cria.listar_pessoa()):
           print(i)
