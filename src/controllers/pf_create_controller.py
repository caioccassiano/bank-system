from src.models.sqlite.repository.pessoa_fisica_repository import PessoaFisicaRepository
from src.controllers.interfaces.pf_create_interface import PfCreatorInterface
from src.validators.schemas.pf_create_schema import PFCreateSchema

class PfCreatorController(PfCreatorInterface):
  def __init__(self, pf_repository: PessoaFisicaRepository):
    self.__pf_repository = pf_repository

  def create_user(self, user_info:PFCreateSchema)-> dict:
    validated_data = PFCreateSchema(**user_info)


    self.__validade_saldo(validated_data.saldo)
    self.__insert_user(**validated_data.model_dump())
    formatted_response = self.__format_response(validated_data.model_dump())
    return formatted_response

  

  def __validade_saldo(self, saldo:int)-> None:
    
    if saldo < 0:
      raise Exception("Saldo deve ser positivo")
    
  def __insert_user(self, **user_info) -> None:
        self.__pf_repository.create_user(**user_info)

  def __format_response(self, user_info:dict)-> dict:
    return {
      "data":{
        "type": "Pessoa Física",
        "dados": user_info
      }
    }
    
  
    
  
    




    
  




