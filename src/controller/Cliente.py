

from ..model.AbstractPessoa import AbstractPessoa


class PessoaController:
  pessoa = []
  
  @classmethod
  def salvar_pessoa(cls, pessoa:AbstractPessoa) -> None:
    cls.pessoa.append(pessoa)

  @classmethod
  def listar_pessoa(cls) -> []:
    return cls.pessoa