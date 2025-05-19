from src.view.interfaces.view_handle_interface import ViewHandleInterface
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from src.controllers.pf_saque_controller import PFSaqueController
class PfSaqueView(ViewHandleInterface):
  def __init__(self, controller:PFSaqueController )-> None:
    self.__controller = controller

  def handle(self, http_request:HttpRequest)-> HttpResponse:
    valor_saque = http_request.body["valor_saque"]
    nome = http_request.body["nome_completo"]
    body_response = self.__controller.sacar_dinheiro(quantia=valor_saque, pessoa=nome)

    return HttpResponse(status_code=200, body=body_response)
  


  