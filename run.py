from flask import Flask, request, jsonify
from src.controllers.pf_create_controller import PfCreatorController
from src.validators.schemas.pf_create_schema import PFCreateSchema
from src.models.sqlite.repository.pessoa_fisica_repository import PessoaFisicaRepository
from src.models.sqlite.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()



# Instância do Flask
app = Flask(__name__)

# Injeção de dependência
pf_repository = PessoaFisicaRepository(db_connection=db_connection_handler)
controller = PfCreatorController(pf_repository)

@app.route("/usuarios/pf", methods=["POST"])
def criar_usuario():
    user_info = request.get_json()
    try:
        schema = PFCreateSchema(**user_info)  # Aqui sim precisa usar **
        response = controller.create_user(user_info=schema)
        return jsonify(response), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
