from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repository.pessoa_fisica_repository import PessoaFisicaRepository
from src.models.sqlite.entities.pessoa_fisica import PessoaFisica
import pytest


db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Test done")
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
  


def test_consultar_saldo():
  repo = PessoaFisicaRepository(db_connection_handler)

  with db_connection_handler as db:
    pessoa = db.session.query(PessoaFisica).filter_by(nome_completo = "Pedro Santos").first()

    response = repo.consultar_saldo(pessoa)
    print(response)


def test_sacar_dinheiro():
  quantia = 4000
  repo = PessoaFisicaRepository(db_connection_handler)

  with db_connection_handler as db:
    pessoa = db.session.query(PessoaFisica).filter_by(nome_completo = "Pedro Santos").first()


  response = repo.sacar_dinheiro(quantia, pessoa)
  print(response)
  assert response == "Saque de R$4000 realizado com sucesso. Saldo restante R$4000.0"



  

  
  