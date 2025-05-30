from abc import ABC, abstractmethod
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse

class ViewHandleInterface(ABC):
  @abstractmethod
  def handle(self, http_request:HttpRequest)-> HttpResponse:
    pass

