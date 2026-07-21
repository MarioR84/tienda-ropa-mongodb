from flask import Blueprint

from controllers.venta_controller import VentaController


venta_bp = Blueprint("venta_bp", __name__)


@venta_bp.route("/ventas", methods=["GET"])
def listar_ventas():
    return VentaController.listar()


@venta_bp.route("/ventas/<venta_id>", methods=["GET"])
def obtener_venta(venta_id):
    return VentaController.obtener(venta_id)


@venta_bp.route("/ventas", methods=["POST"])
def crear_venta():
    return VentaController.crear()


@venta_bp.route("/ventas/<venta_id>", methods=["PUT"])
def actualizar_venta(venta_id):
    return VentaController.actualizar(venta_id)


@venta_bp.route("/ventas/<venta_id>", methods=["DELETE"])
def eliminar_venta(venta_id):
    return VentaController.eliminar(venta_id)