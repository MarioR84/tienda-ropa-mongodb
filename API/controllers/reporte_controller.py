from flask import jsonify

from models.reporte_model import ReporteModel


class ReporteController:

    @staticmethod
    def marcas_con_ventas():
        resultado = ReporteModel.marcas_con_ventas()

        return jsonify({
            "mensaje": "Marcas con ventas obtenidas correctamente",
            "datos": resultado
        }), 200

    @staticmethod
    def prendas_vendidas_con_stock():
        resultado = ReporteModel.prendas_vendidas_con_stock()

        return jsonify({
            "mensaje": (
                "Prendas vendidas con stock obtenidas correctamente"
            ),
            "datos": resultado
        }), 200

    @staticmethod
    def cinco_marcas_mas_vendidas():
        resultado = ReporteModel.cinco_marcas_mas_vendidas()

        return jsonify({
            "mensaje": (
                "Cinco marcas más vendidas obtenidas correctamente"
            ),
            "datos": resultado
        }), 200