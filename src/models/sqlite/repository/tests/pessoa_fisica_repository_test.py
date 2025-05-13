from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repository.pessoa_fisica_repository import PessoaFisicaRepository
from src.models.sqlite.entities.pessoa_fisica import PessoaFisica
from src.validators.schemas.pf_create_schema import PFCreateSchema
import pytest


db_connection_handler.connect_to_db()

@pytest.mark.skip("Test Done")
def test_criar_pessoa_fisica():
  user_data = PFCreateSchema(
    renda_mensal = 2100,
    idade = 60,
    nome_completo = "Rosiclair da Rosa",
    celular = "996738291",
    email= "rosi@example.com",
    categoria= "Categoria A",
    saldo = 3.546)

  repo = PessoaFisicaRepository(db_connection=db_connection_handler)
  repo.create_user(user=user_data)

@pytest.mark.skip("Test Done")
def test_consultar_saldo():
  repo = PessoaFisicaRepository(db_connection_handler)

  with db_connection_handler as db:
    pessoa = db.session.query(PessoaFisica).filter_by(nome_completo = "Pedro Santos").first()

    response = repo.consultar_saldo(pessoa)
    print(response)

@pytest.mark.skip("Test Done")
def test_sacar_dinheiro():
  quantia = 4000
  repo = PessoaFisicaRepository(db_connection_handler)

  with db_connection_handler as db:
    pessoa = db.session.query(PessoaFisica).filter_by(nome_completo = "Pedro Santos").first()


  response = repo.sacar_dinheiro(quantia, pessoa)
  print(response)
  assert response == "Saque de R$4000 realizado com sucesso. Saldo restante R$4000.0"

def test_listar_usuarios_pf():
  with db_connection_handler as db:
    list_users_pf = db.session.query(PessoaFisica).all()
    print(list_users_pf)




  

  
  