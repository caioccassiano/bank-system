from src.view.http_types.http_request import HttpRequest
from pydantic import ValidationError
from .schemas.pj_create_schema import PJCreateSchema

def pj_creator_validator(http_request : HttpRequest)-> None:
  try:
    PJCreateSchema(**http_request.body)
  except ValidationError as e:
    raise e
  

