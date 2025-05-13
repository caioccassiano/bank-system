from src.models.sqlite.repository.pessoa_juridica_repository import PessoaJuridicaRepository
from src.validators.schemas.pj_create_schema import PJCreateSchema
from src.controllers.interfaces.create_interface import CreatorInterface

class PJCreatorController(CreatorInterface):
  def __init__(self, pj_repository:PessoaJuridicaRepository)-> None:
    self.__pj_repository = pj_repository

  def create_user(self, user_info:PJCreateSchema)-> dict:
    validated_data = PJCreateSchema(**user_info)

    self.__validade_saldo(validated_data.saldo)
    self.__insert_user(**validated_data.model_dump())
    formatted_response = self.__format_response(validated_data.model_dump())
    return formatted_response

  def __validade_saldo(self, saldo:float)-> None:
    
    if saldo < 0:
      raise Exception("Saldo deve ser positivo")
    
  def __insert_user(self, **user_info) -> None:
        self.__pj_repository.create_user(**user_info)

  def __format_response(self, user_info:dict)-> dict:
    return {
      "data":{
        "type": "Pessoa Jurídica",
        "dados": user_info
      }
    }
  
