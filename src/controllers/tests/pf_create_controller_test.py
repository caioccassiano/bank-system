from src.controllers.pf_create_controller import PfCreatorController

class Mock:
  def create_user(
      self,
      renda_mensal:float,
      idade: int,
      nome_completo: str,
      celular: str,
      email: str,
      categoria: str,
      saldo: float)-> None:
    pass
    
def test_create_user():
  user_info = {
    "renda_mensal": 4.230,
    "idade": 18,
    "nome_completo": "Rosiclair da Rosa",
    "celular": "99999-8888",
    "email": "rosi@example.com",
    "categoria": "Categoria A",
    "saldo": 10.240
  }

  controller = PfCreatorController(Mock())
  response = controller.create_user(user_info=user_info)

  print(response)

  assert response["data"]["type"] == "Pessoa Física"
  assert response["data"]["dados"] == user_info

