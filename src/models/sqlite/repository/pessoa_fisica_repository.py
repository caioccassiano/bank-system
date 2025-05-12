from src.models.sqlite.entities.pessoa_fisica import PessoaFisica
from src.models.sqlite.interfaces.cliente_interface import Client

class PessoaFisicaRepository(Client):
  def __init__(self, db_connection)-> None:
    self.__db_connection = db_connection

  def criar_pessoa_fisica(
      self, 
      renda_mensal: float,
      idade: int,
      nome_completo: str,
      celular: str,
      email: str,
      categoria: str,
      saldo: float)-> None:
    
    with self.__db_connection as database:
      try:
        pessoa_fisica = PessoaFisica(
          renda_mensal=renda_mensal,
          idade = idade,
          nome_completo = nome_completo,
          celular=celular,
          email=email,
          categoria=categoria,
          saldo = saldo
        )

        database.session.add(pessoa_fisica)
        database.session.commit()

      except Exception as exception:
        database.session.rollback()

        raise exception
    

  def consultar_saldo(self, pessoa_fisica)-> float:
    with self.__db_connection as database:
      try:
        consulta = database.session.query(PessoaFisica).filter_by(nome_completo=pessoa_fisica.nome_completo).first()
        return consulta.saldo
      
      except Exception as exception:
        database.session.rollback()

        raise exception
      
  def sacar_dinheiro(self, quantia, pessoa_fisica):
    limite_saque = 5000

    saldo = self.consultar_saldo(pessoa_fisica=pessoa_fisica)

    if quantia < saldo and quantia < limite_saque:
      saldo -= quantia
      return f"Saque de R${quantia} realizado com sucesso. Saldo restante R${saldo}"
    
    else:
      return "Erro: Quantia de saque excede o limite ou saldo insuficiente"
    
  def realizar_extrato(self, pessoa_fisica):
    with self.__db_connection as database:
      try:
        pessoa = database.session.query(PessoaFisica).filter_by(nome_completo = pessoa_fisica.nome_completo).first()
        return {
          "Nome": pessoa.nome_completo,
          "Saldo": pessoa.saldo,
          "Categoria": pessoa.categoria
        }
      except Exception as exception:

        raise exception
      

    
    

                              
      
  
