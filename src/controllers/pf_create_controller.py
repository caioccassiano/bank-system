from src.models.sqlite.repository.pessoa_fisica_repository import PessoaFisicaRepository
from src.controllers.interfaces.create_interface import CreatorInterface
from src.validators.schemas.pf_create_schema import PFCreateSchema

class PfCreatorController(CreatorInterface):
  def __init__(self, pf_repository: PessoaFisicaRepository):
    self.__pf_repository = pf_repository

  def create_user(self, user_info:PFCreateSchema)-> dict:

    self.__validade_saldo(user_info.saldo)
    self.__insert_user(user_info.model_dump())
    formatted_response = self.__format_response(user_info.model_dump())
    return formatted_response

  

  def __validade_saldo(self, saldo:float)-> None:
    
    if saldo < 0:
      raise Exception("Saldo deve ser positivo")
    
  def __insert_user(self, user_info: dict) -> None:
    self.__pf_repository.create_user(user_info)


  def __format_response(self, user_info:dict)-> dict:
    return {
      "data":{
        "type": "Pessoa Física",
        "dados": user_info
      }
    }
    
  
    
  
    




    
  




