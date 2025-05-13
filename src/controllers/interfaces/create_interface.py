from abc import ABC, abstractmethod

class CreatorInterface(ABC):

  @abstractmethod
  def create_user(self, user_info:dict) -> dict:
    pass

