from src.models.sqlite.entities.pessoa_juridica import PessoaJuridica
from src.models.sqlite.interfaces.cliente_interface import Client

class PessoaJuridicaRepository(Client):
  def __init__(self, db_connection)->None:
    self.__db_connection = db_connection

  def create_user(
      self,
      faturamento: float,
      idade: int,
      nome_fantasia: str,
      celular: str,
      email_corporativo: str,
      categoria: str,
      saldo: float)-> None:
    
    with self.__db_connection as database:
      try:
        pessoa_juridica = PessoaJuridica(
          faturamento = faturamento,
          idade = idade,
          nome_fantasia = nome_fantasia,
          celular = celular,
          email_corporativo = email_corporativo,
          categoria = categoria,
          saldo = saldo)
        
        database.session.add(pessoa_juridica)
        database.session.commit()

      except Exception as exception:
        raise exception
      
  
  def consultar_saldo(self, pessoa_juridica)-> float:
    with self.__db_connection as database:
      try:
        consulta = database.session.query(PessoaJuridica).filter_by(nome_fantasia = pessoa_juridica.nome_fantasia).first()
        return consulta.saldo
      except Exception as exception:
        raise exception
      
  def sacar_dinheiro(self, quantia, pessoa_juridica ):
    limite_saque = 10000

    saldo = self.consultar_saldo(pessoa_juridica)

    if quantia <= limite_saque and quantia <= saldo:
      saldo -= quantia
      return f"Saque de R${quantia} realizado com sucesso. Saldo restante R${saldo}"
    else:
      return "Erro: Quantia de saque excede o limite ou saldo insuficiente"
    
  def realizar_extrato(self, pessoa_juridica):

    with self.__db_connection as database:

      try:
        consulta = database.session.query(PessoaJuridica).filter_by(nome_fantasia = pessoa_juridica.nome_fantasia).first()
        return consulta.saldo
      except Exception as exception:
        raise exception
      
  def find_user(self, nome:str):
    with self.__db_connection as database:
      try:
        user_nome = database.session.query(PessoaJuridica).filter_by(nome_fantasia = nome).first()
        return user_nome
      except Exception as exception:
        raise exception
      
  def listar_usuarios_pj(self)-> list:
    with self.__db_connection as database:
      try:
        pj_users = database.session.query(PessoaJuridica).all()
        return pj_users
      except Exception as e:
        raise e
    
      

