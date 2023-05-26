from src.model.AbstractPessoa import AbstractPessoa


class Cliente(AbstractPessoa):

    def reiniciar(self, nome):
        print(nome)
