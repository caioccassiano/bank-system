from src.view.interfaces.view_handle_interface import ViewHandleInterface
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from src.controllers.pf_extrato_controlller import PFRealizarExtratoController

class PfExtratoView(ViewHandleInterface):
  def __init__(self, controller: PFRealizarExtratoController):
    self.__controller = controller

  def handle(self, http_request: HttpRequest)-> HttpResponse:
    nome_pessoa = http_request["nome_completo"]
    body_reponse = self.__controller.realizar_extrato(nome_pessoa=nome_pessoa)
    return HttpResponse(status_code=200, body=body_reponse)
  

  