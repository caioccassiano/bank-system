from src.models.sqlite.repository.pessoa_fisica_repository import PessoaFisicaRepository
from .interfaces.saque_interface import SaqueInterface


class PFSaqueController(SaqueInterface):
  def __init__(self, pf_repository: PessoaFisicaRepository):
    self.__pf_repository = pf_repository

  def sacar_dinheiro(self, quantia:int, pessoa:str)-> dict:
    self.__validar_saque(quantia=quantia)
    novo_saldo =self.__verificar_saldo_user(quantia=quantia, pessoa=pessoa)
    formatted_response = self.__format_response(quantia,pessoa, novo_saldo)
    return formatted_response

  
  def __validar_saque(self, quantia: int)-> None:
    limite_saque = 5000

    if quantia > limite_saque:
      raise Exception("Valor de saque superior ao limite permitido.")
    
  def __verificar_saldo_user(self, quantia:int, pessoa:str) ->None:
    saldo_cliente = self.__pf_repository.consultar_saldo(pessoa_fisica=pessoa)
    
    if quantia > saldo_cliente:
      raise Exception("O valor de saque solicitado é maior que o saldo da conta.")
    
    novo_saldo = saldo_cliente - quantia
    
    return novo_saldo
    
  def __format_response(self, quantia, pessoa, novo_saldo):
    return {
      "data": {
        "nome_beneficiário": {pessoa},
        "valor_saque": f"R${quantia}",
        "novo_saldo": f"Voce ainda tem R${novo_saldo} na sua conta "
      }
    }


    
