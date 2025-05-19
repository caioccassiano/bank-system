from src.controllers.pf_create_controller import PfCreatorController
from src.validators.pf_creator_validator import pf_creator_validator
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from src.view.interfaces.view_handle_interface import ViewHandleInterface

class PfCreatorView(ViewHandleInterface):
  def __init__(self, controller: PfCreatorController)-> None:
    self.__controller = controller

  def handle(self, http_request:HttpRequest)-> HttpResponse:
    pf_creator_validator(http_request=http_request)

    user_info = http_request.body

    body_response = self.__controller.create_user(user_info=user_info)

    return HttpResponse(status_code=200, body=body_response)