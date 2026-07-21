from datetime import datetime

from bson.errors import InvalidId
from flask import jsonify, request

from models.venta_model import VentaModel


class VentaController:

    @staticmethod
    def listar():
        ventas = VentaModel.obtener_todas()

        return jsonify({
            "mensaje": "Ventas obtenidas correctamente",
            "datos": ventas
        }), 200

    @staticmethod
    def obtener(venta_id):
        try:
            venta = VentaModel.obtener_por_id(venta_id)

            if not venta:
                return jsonify({
                    "mensaje": "Venta no encontrada"
                }), 404

            return jsonify({
                "mensaje": "Venta obtenida correctamente",
                "datos": venta
            }), 200

        except InvalidId:
            return jsonify({
                "mensaje": "El ID proporcionado no es válido"
            }), 400

    @staticmethod
    def crear():
        datos = request.get_json()

        if not datos:
            return jsonify({
                "mensaje": "Debe enviar datos en formato JSON"
            }), 400

        campos_obligatorios = [
            "fecha",
            "cliente",
            "prenda",
            "marca",
            "cantidad",
            "total"
        ]

        for campo in campos_obligatorios:
            if campo not in datos:
                return jsonify({
                    "mensaje": f"El campo {campo} es obligatorio"
                }), 400

        try:
            datetime.strptime(datos["fecha"], "%Y-%m-%d")
        except (ValueError, TypeError):
            return jsonify({
                "mensaje": "La fecha debe tener el formato YYYY-MM-DD"
            }), 400

        if not isinstance(datos["cantidad"], int):
            return jsonify({
                "mensaje": "La cantidad debe ser un número entero"
            }), 400

        if not isinstance(datos["total"], (int, float)):
            return jsonify({
                "mensaje": "El total debe ser numérico"
            }), 400

        if datos["cantidad"] <= 0:
            return jsonify({
                "mensaje": "La cantidad debe ser mayor que cero"
            }), 400

        if datos["total"] < 0:
            return jsonify({
                "mensaje": "El total no puede ser negativo"
            }), 400

        nueva_venta = {
            "fecha": datos["fecha"],
            "cliente": datos["cliente"],
            "prenda": datos["prenda"],
            "marca": datos["marca"],
            "cantidad": datos["cantidad"],
            "total": datos["total"]
        }

        venta_id = VentaModel.crear(nueva_venta)

        return jsonify({
            "mensaje": "Venta creada correctamente",
            "id": venta_id
        }), 201

    @staticmethod
    def actualizar(venta_id):
        datos = request.get_json()

        if not datos:
            return jsonify({
                "mensaje": "Debe enviar datos para actualizar"
            }), 400

        try:
            venta = VentaModel.obtener_por_id(venta_id)

            if not venta:
                return jsonify({
                    "mensaje": "Venta no encontrada"
                }), 404

            campos_permitidos = {}

            for campo in [
                "fecha",
                "cliente",
                "prenda",
                "marca",
                "cantidad",
                "total"
            ]:
                if campo in datos:
                    campos_permitidos[campo] = datos[campo]

            if not campos_permitidos:
                return jsonify({
                    "mensaje": "No se enviaron campos válidos"
                }), 400

            if "fecha" in campos_permitidos:
                try:
                    datetime.strptime(
                        campos_permitidos["fecha"],
                        "%Y-%m-%d"
                    )
                except (ValueError, TypeError):
                    return jsonify({
                        "mensaje": "La fecha debe tener el formato YYYY-MM-DD"
                    }), 400

            if "cantidad" in campos_permitidos:
                if not isinstance(campos_permitidos["cantidad"], int):
                    return jsonify({
                        "mensaje": "La cantidad debe ser un número entero"
                    }), 400

                if campos_permitidos["cantidad"] <= 0:
                    return jsonify({
                        "mensaje": "La cantidad debe ser mayor que cero"
                    }), 400

            if "total" in campos_permitidos:
                if not isinstance(campos_permitidos["total"], (int, float)):
                    return jsonify({
                        "mensaje": "El total debe ser numérico"
                    }), 400

                if campos_permitidos["total"] < 0:
                    return jsonify({
                        "mensaje": "El total no puede ser negativo"
                    }), 400

            VentaModel.actualizar(venta_id, campos_permitidos)

            return jsonify({
                "mensaje": "Venta actualizada correctamente"
            }), 200

        except InvalidId:
            return jsonify({
                "mensaje": "El ID proporcionado no es válido"
            }), 400

    @staticmethod
    def eliminar(venta_id):
        try:
            venta = VentaModel.obtener_por_id(venta_id)

            if not venta:
                return jsonify({
                    "mensaje": "Venta no encontrada"
                }), 404

            VentaModel.eliminar(venta_id)

            return jsonify({
                "mensaje": "Venta eliminada correctamente"
            }), 200

        except InvalidId:
            return jsonify({
                "mensaje": "El ID proporcionado no es válido"
            }), 400