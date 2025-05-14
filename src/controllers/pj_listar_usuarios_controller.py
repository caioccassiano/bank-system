from src.models.sqlite.repository.pessoa_juridica_repository import PessoaJuridicaRepository
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridica

class ListarUsuariosController:
  def __init__(self, pj_repository : PessoaJuridicaRepository)-> None:
    self.__pj_repository = pj_repository
  
  def listar_usuarios(self)->dict:
    list_users = self.__get_pj_users()
    formatted_response = self.__format_response(list_users=list_users)
    return formatted_response

  def __get_pj_users(self)->list[PessoaJuridica]:
    list_users = self.__pj_repository.listar_usuarios_pj()
    return list_users
  
  def __format_response(self, list_users:list[PessoaJuridica])-> dict:
    formated_list = []
    for user in list_users:
      formated_list.append({
        "nome_fantasia": user.nome_fantasia,
        "celular": user.celular,
        "renda_faturamento": user.faturamento,
        "saldo": user.saldo
        })
      
    return {
      "data":{
        "type": "Pessoa Jurídica",
        "quantidade": len(formated_list),
        "usuários": formated_list
      }
    }
  
