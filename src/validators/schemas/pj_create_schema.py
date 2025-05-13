from pydantic import BaseModel, EmailStr, Field

class PJCreateSchema(BaseModel):
  faturamento: float = Field(..., gt=0)
  idade: int = Field(..., ge=18)
  nome_fantasia: str = Field(..., min_length=3)
  celular: str = Field(..., min_length=9)
  email_corporativo: EmailStr
  categoria: str
  saldo: float = Field(..., ge=0)


