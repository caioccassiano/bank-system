from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repository.pessoa_fisica_repository import PessoaFisicaRepository
db_connection_handler.connect_to_db()

def test_criar_pessoa_fisica():
  renda_mensal = 1500
  idade = 26
  nome_completo = "Caio Cassiano"
  celular = "996738291"
  email= "caio@example.com"
  categoria= "Categoria A"
  saldo = 3.546

  repo = PessoaFisicaRepository(db_connection=db_connection_handler)
  repo.criar_pessoa_fisica(
    renda_mensal=renda_mensal,
    idade=idade,
    nome_completo=nome_completo,
    celular=celular,
    email=email,
    categoria=categoria,
    saldo=saldo)
  
