import abc


class AbstractPessoa(metaclass=abc.ABCMeta):
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f"{self.nome}"
