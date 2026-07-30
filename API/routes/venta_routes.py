from flask import Blueprint

from controllers.venta_controller import VentaController
from middleware.auth import token_requerido


venta_bp = Blueprint("venta_bp", __name__)


@venta_bp.route("/ventas", methods=["GET"])
@token_requerido
def listar_ventas():
    return VentaController.listar()


@venta_bp.route("/ventas/<venta_id>", methods=["GET"])
@token_requerido
def obtener_venta(venta_id):
    return VentaController.obtener(venta_id)


@venta_bp.route("/ventas", methods=["POST"])
@token_requerido
def crear_venta():
    return VentaController.crear()


@venta_bp.route("/ventas/<venta_id>", methods=["PUT"])
@token_requerido
def actualizar_venta(venta_id):
    return VentaController.actualizar(venta_id)


@venta_bp.route("/ventas/<venta_id>", methods=["DELETE"])
@token_requerido
def eliminar_venta(venta_id):
    return VentaController.eliminar(venta_id)