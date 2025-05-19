from src.view.interfaces.view_handle_interface import ViewHandleInterface
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from src.controllers.pj_extrato_controller import PJRealizarExtratoController

class PjExtratoView(ViewHandleInterface):
  def __init__(self, controller: PJRealizarExtratoController):
    self.__controller = controller

  def handle(self, http_request:HttpRequest)->HttpResponse:
    nome_pessoa = http_request.body["nome_pessoa"]
    body_response = self.__controller.realizar_extrato(nome_pessoa=nome_pessoa)
    return HttpResponse(status_code=200, body=body_response)
  

  