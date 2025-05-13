from pydantic import BaseModel, EmailStr, Field

class PFCreateSchema(BaseModel):
  renda_mensal: float = Field(..., gt=0, description="Renda mensal deve ser positiva")
  idade: int = Field(..., ge=18, description="Idade mínima é 18 anos")
  nome_completo: str = Field(..., min_length=3)
  celular: str = Field(..., min_length=9)
  email: EmailStr
  categoria: str
  saldo: float = Field(..., ge=0, description="Saldo inicial não pode ser negativo")
  
