from src.models.sqlite.repository.pessoa_juridica_repository import PessoaJuridicaRepository
from .interfaces.extrato_controller_interface import RealizarExtratoInterface

class PJRealizarExtratoController(RealizarExtratoInterface):
  def __init__(self, pj_repository:PessoaJuridicaRepository):
    self.__pj_repository = pj_repository

  def realizar_extrato(self, nome_pessoa)->dict:
    user = self.__verificar_is_user(nome_user=nome_pessoa)
    saldo = self.__verificar_saldo(nome_user=user)
    formatted_response = self.__format_response(user,saldo)
    return formatted_response



  def __verificar_is_user(self, nome_user)-> None:
    user = self.__pj_repository.find_user(nome_fantasia=nome_user)
    
    if not user:
      raise Exception("Usuário nao existe!")
    
    return user
  
  def __verificar_saldo(self, nome_user)->float:
    try:
      saldo = self.__pj_repository.consultar_saldo(pessoa_juridica=nome_user)

      return saldo
    
    except Exception as exception:
      raise exception
  
  def __format_response(self, user_nome, saldo):
    return {
      "data":{
        "nome_empresa": {user_nome},
        "saldo_disponivel":f"R${saldo}"
      }
    }



