from flask import Blueprint

from controllers.reporte_controller import ReporteController


reporte_bp = Blueprint("reporte_bp", __name__)


@reporte_bp.route(
    "/reportes/marcas-con-ventas",
    methods=["GET"]
)
def marcas_con_ventas():
    return ReporteController.marcas_con_ventas()


@reporte_bp.route(
    "/reportes/prendas-vendidas-stock",
    methods=["GET"]
)
def prendas_vendidas_con_stock():
    return ReporteController.prendas_vendidas_con_stock()


@reporte_bp.route(
    "/reportes/cinco-marcas-mas-vendidas",
    methods=["GET"]
)
def cinco_marcas_mas_vendidas():
    return ReporteController.cinco_marcas_mas_vendidas()