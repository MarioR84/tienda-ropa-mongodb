from flask import Blueprint

from controllers.prenda_controller import PrendaController


prenda_bp = Blueprint("prenda_bp", __name__)


@prenda_bp.route("/prendas", methods=["GET"])
def listar_prendas():
    return PrendaController.listar()


@prenda_bp.route("/prendas/<prenda_id>", methods=["GET"])
def obtener_prenda(prenda_id):
    return PrendaController.obtener(prenda_id)


@prenda_bp.route("/prendas", methods=["POST"])
def crear_prenda():
    return PrendaController.crear()


@prenda_bp.route("/prendas/<prenda_id>", methods=["PUT"])
def actualizar_prenda(prenda_id):
    return PrendaController.actualizar(prenda_id)


@prenda_bp.route("/prendas/<prenda_id>", methods=["DELETE"])
def eliminar_prenda(prenda_id):
    return PrendaController.eliminar(prenda_id)