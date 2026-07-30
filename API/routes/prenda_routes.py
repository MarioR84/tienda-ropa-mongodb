from flask import Blueprint

from controllers.prenda_controller import PrendaController
from middleware.auth import token_requerido


prenda_bp = Blueprint("prenda_bp", __name__)


@prenda_bp.route("/prendas", methods=["GET"])
@token_requerido
def listar_prendas():
    return PrendaController.listar()


@prenda_bp.route("/prendas/<prenda_id>", methods=["GET"])
@token_requerido
def obtener_prenda(prenda_id):
    return PrendaController.obtener(prenda_id)


@prenda_bp.route("/prendas", methods=["POST"])
@token_requerido
def crear_prenda():
    return PrendaController.crear()


@prenda_bp.route("/prendas/<prenda_id>", methods=["PUT"])
@token_requerido
def actualizar_prenda(prenda_id):
    return PrendaController.actualizar(prenda_id)


@prenda_bp.route("/prendas/<prenda_id>", methods=["DELETE"])
@token_requerido
def eliminar_prenda(prenda_id):
    return PrendaController.eliminar(prenda_id)