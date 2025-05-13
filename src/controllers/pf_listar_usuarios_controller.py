from src.models.sqlite.repository.pessoa_fisica_repository import PessoaFisicaRepository, PessoaFisica

class ListarUsuariosController:
  def __init__(self, pf_repository : PessoaFisicaRepository)-> None:
    self.__pf_repository = pf_repository
  
  def listar_usuarios(self)->dict:
    list_users = self.__get_pf_users()
    formatted_response = self.__format_response(list_users=list_users)
    return formatted_response

  def __get_pf_users(self)->list[PessoaFisica]:
    list_users = self.__pf_repository.listar_usuarios_pf()
    return list_users
  
  def __format_response(self, list_users:list[PessoaFisica])-> dict:
    formated_list = []
    for user in list_users:
      formated_list.append({
        "nome_completo": user.nome_completo,
        "celular": user.celular,
        "renda_mensal": user.renda_mensal,
        "saldo": user.saldo
        })
      
    return {
      "data":{
        "type": "Pessoa Física",
        "quantidade": len(formated_list),
        "usuários": formated_list
      }
    }
  
