from abc import ABC, abstractmethod

class SaqueInterface(ABC):
  @abstractmethod
  def sacar_dinheiro(self, quantia, pessoa):
    pass

  