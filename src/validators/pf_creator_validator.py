from pydantic import ValidationError
from src.view.http_types.http_request import HttpRequest
from .schemas.pf_create_schema import PFCreateSchema

def pf_creator_validator(http_request : HttpRequest)-> None:
  try:
    PFCreateSchema(**http_request.body)
  except ValidationError as e:
    raise e
  

