from src.controllers.pf_extrato_controlller import PFRealizarExtratoController


class MockExtrato:
  def realizar_extrato(
      self,
      nome_pessoa:str):
    pass
  
  def find_user(self, nome):
    return "Caio Caano"

  def consultar_saldo(self,pessoa_fisica):
    return 1564.45
  
def test_realizar_extrato():
  nome_pessoa = "Caio Cassiano"
  controller = PFRealizarExtratoController(MockExtrato())


  response = controller.realizar_extrato(nome_pessoa)

  print(response)

  assert response["data"]["saldo_disponivel"] == "R$1564.45"

  assert "nome_usuário" in response["data"]

  assert "erro" not in response


  