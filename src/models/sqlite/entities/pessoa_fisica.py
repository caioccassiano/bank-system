from src.models.sqlite.settings.base import Base
from sqlalchemy import BIGINT, Column, String, Float

class PessoaFisica(Base):
  __tablename__ = "pessoa_fisica"
  id = Column(BIGINT, primary_key=True, autoincrement=True)
  renda_mensal = Column(Float, nullable=False)
  idade = Column(BIGINT, nullable = False)
  nome_completo = Column(String(80), nullable=False)
  celular = Column(String)
  email = Column(String)
  categoria = Column(String)
  saldo = Column(Float)

  


