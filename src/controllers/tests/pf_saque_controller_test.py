from src.controllers.pf_saque_controller import PFSaqueController


class MockSaque:
  def sacar_dinheiro(
      self,
      quantia: float,
      pessoa:str):
    pass
  
  def consultar_saldo(self, pessoa_fisica)-> float:
    pessoa_fisica = 10000
    return pessoa_fisica



def test_sacar_dinheiro():
  quantia = 4600
  pessoa = "Caio Cesar Cassiano"

  controller = PFSaqueController(MockSaque())

  response = controller.sacar_dinheiro(quantia=quantia, pessoa=pessoa)

  print(response)



    
  