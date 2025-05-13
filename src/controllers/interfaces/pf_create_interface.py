from abc import ABC, abstractmethod

class PfCreatorInterface(ABC):

  @abstractmethod
  def create_user(self, user_info:dict) -> dict:
    pass

