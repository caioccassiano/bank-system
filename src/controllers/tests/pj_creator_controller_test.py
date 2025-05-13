from src.controllers.pj_create_controller import PJCreatorController

class Mock:
  def create_user(
      self,
      faturamento:float,
      idade: int,
      nome_fantasia: str,
      celular: str,
      email_corporativo: str,
      categoria: str,
      saldo: float)-> None:
    pass
    
def test_create_user():

  mock_repository = Mock()
  user_info = {
    "faturamento": 7.000,
    "idade": 18,
    "nome_fantasia": "Bita Kids",
    "celular": "99999-8888",
    "email_corporativo": "bitakids@example.com",
    "categoria": "Categoria A",
    "saldo": 154000
  }

  controller = PJCreatorController(mock_repository)
  response = controller.create_user(user_info=user_info)

  print(response)

  assert response["data"]["type"] == "Pessoa Jurídica"
  assert response["data"]["dados"] == user_info

