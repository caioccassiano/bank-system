from abc import ABC, abstractmethod

class Client(ABC):

  @abstractmethod
  def create_user(self, user_info: dict):
    pass

  @abstractmethod
  def sacar_dinheiro(self, quantia):
    pass

  def realizar_extrato(self, pessoa):
    pass