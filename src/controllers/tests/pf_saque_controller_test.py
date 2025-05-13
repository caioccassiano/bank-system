from src.controllers.pf_saque_controller import PFSaqueController


class MockSaque:
  def sacar_dinheiro(
      self,
      quantia: float,
      pessoa:str):
    pass
  
  def consultar_saldo(self, pessoa_fisica:str)-> float:
    return 10000



def test_sacar_dinheiro():
  quantia = 4000
  pessoa = "Caio Cesar Cassiano"

  controller = PFSaqueController(MockSaque())

  response = controller.sacar_dinheiro(quantia=quantia, pessoa=pessoa)

  print(response)



    
  