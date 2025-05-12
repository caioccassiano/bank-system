from src.models.sqlite.settings.base import Base
from sqlalchemy import BIGINT, Column, String, Float

class PessoaJuridica(Base):
  __tablename__ = "pessoa_juridica"
  id = Column(BIGINT, primary_key=True, autoincrement=True)
  faturamento = Column(Float, nullable=False)
  idade = Column(BIGINT, nullable = False)
  nome_fantasia = Column(String(80), nullable=False)
  celular = Column(String)
  email_corporativo = Column(String)
  categoria = Column(String)
  saldo = Column(Float)

  


