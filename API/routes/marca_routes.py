from flask import Blueprint

from controllers.marca_controller import MarcaController
from middleware.auth import token_requerido


marca_bp = Blueprint("marca_bp", __name__)


@marca_bp.route("/marcas", methods=["GET"])
@token_requerido
def listar_marcas():
    return MarcaController.listar()


@marca_bp.route("/marcas/<marca_id>", methods=["GET"])
@token_requerido
def obtener_marca(marca_id):
    return MarcaController.obtener(marca_id)


@marca_bp.route("/marcas", methods=["POST"])
@token_requerido
def crear_marca():
    return MarcaController.crear()


@marca_bp.route("/marcas/<marca_id>", methods=["PUT"])
@token_requerido
def actualizar_marca(marca_id):
    return MarcaController.actualizar(marca_id)


@marca_bp.route("/marcas/<marca_id>", methods=["DELETE"])
@token_requerido
def eliminar_marca(marca_id):
    return MarcaController.eliminar(marca_id)