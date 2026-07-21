from flask import Blueprint

from controllers.marca_controller import MarcaController


marca_bp = Blueprint("marca_bp", __name__)


@marca_bp.route("/marcas", methods=["GET"])
def listar_marcas():
    return MarcaController.listar()


@marca_bp.route("/marcas/<marca_id>", methods=["GET"])
def obtener_marca(marca_id):
    return MarcaController.obtener(marca_id)


@marca_bp.route("/marcas", methods=["POST"])
def crear_marca():
    return MarcaController.crear()


@marca_bp.route("/marcas/<marca_id>", methods=["PUT"])
def actualizar_marca(marca_id):
    return MarcaController.actualizar(marca_id)


@marca_bp.route("/marcas/<marca_id>", methods=["DELETE"])
def eliminar_marca(marca_id):
    return MarcaController.eliminar(marca_id)