from src.view.interfaces.view_handle_interface import ViewHandleInterface
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from src.controllers.pj_listar_usuarios_controller import ListarUsuariosController

class ListarUsuariosView(ViewHandleInterface):
  def __init__(self, controller: ListarUsuariosController):
    self.__controller = controller

  def handle(self, http_request: HttpRequest)->HttpResponse:
    body_response = self.__controller.listar_usuarios()
    return HttpResponse(status_code=200, body=body_response)
  

  