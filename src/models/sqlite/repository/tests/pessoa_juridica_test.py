from src.models.sqlite.entities.pessoa_juridica import PessoaJuridica
from src.models.sqlite.repository.pessoa_juridica_repository import PessoaJuridicaRepository
from src.models.sqlite.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

def test_sacar_dinheiro():

  quantia = 9000

  repo = PessoaJuridicaRepository(db_connection_handler)

  with db_connection_handler as db:
    pessoa = db.session.query(PessoaJuridica).filter_by(nome_fantasia = "Empresa XYZ").first()
  
  response = repo.sacar_dinheiro(quantia=quantia, pessoa_juridica=pessoa)

  print(response)

def test_consultar_saldo():
  repo = PessoaJuridicaRepository(db_connection_handler)

  with db_connection_handler as db:
    pessoa = db.session.query(PessoaJuridica).filter_by(nome_fantasia = "Empresa XYZ").first()
  
  response = repo.consultar_saldo(pessoa)
  print(response)