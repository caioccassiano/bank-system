from abc import ABC, abstractmethod

class RealizarExtratoInterface(ABC):
  
  @abstractmethod
  def realizar_extrato(self, nome_pessoa:str):
    pass

  