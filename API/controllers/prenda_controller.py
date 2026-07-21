from bson.errors import InvalidId
from flask import jsonify, request

from models.prenda_model import PrendaModel


class PrendaController:

    @staticmethod
    def listar():
        prendas = PrendaModel.obtener_todas()

        return jsonify({
            "mensaje": "Prendas obtenidas correctamente",
            "datos": prendas
        }), 200

    @staticmethod
    def obtener(prenda_id):
        try:
            prenda = PrendaModel.obtener_por_id(prenda_id)

            if not prenda:
                return jsonify({
                    "mensaje": "Prenda no encontrada"
                }), 404

            return jsonify({
                "mensaje": "Prenda obtenida correctamente",
                "datos": prenda
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
            "nombre",
            "marca",
            "talla",
            "precio",
            "stock"
        ]

        for campo in campos_obligatorios:
            if campo not in datos:
                return jsonify({
                    "mensaje": f"El campo {campo} es obligatorio"
                }), 400

        if not isinstance(datos["precio"], (int, float)):
            return jsonify({
                "mensaje": "El precio debe ser numérico"
            }), 400

        if not isinstance(datos["stock"], int):
            return jsonify({
                "mensaje": "El stock debe ser un número entero"
            }), 400

        if datos["precio"] < 0 or datos["stock"] < 0:
            return jsonify({
                "mensaje": "El precio y el stock no pueden ser negativos"
            }), 400

        nueva_prenda = {
            "nombre": datos["nombre"],
            "marca": datos["marca"],
            "talla": datos["talla"],
            "precio": datos["precio"],
            "stock": datos["stock"]
        }

        prenda_id = PrendaModel.crear(nueva_prenda)

        return jsonify({
            "mensaje": "Prenda creada correctamente",
            "id": prenda_id
        }), 201

    @staticmethod
    def actualizar(prenda_id):
        datos = request.get_json()

        if not datos:
            return jsonify({
                "mensaje": "Debe enviar datos para actualizar"
            }), 400

        try:
            prenda = PrendaModel.obtener_por_id(prenda_id)

            if not prenda:
                return jsonify({
                    "mensaje": "Prenda no encontrada"
                }), 404

            campos_permitidos = {}

            for campo in ["nombre", "marca", "talla", "precio", "stock"]:
                if campo in datos:
                    campos_permitidos[campo] = datos[campo]

            if not campos_permitidos:
                return jsonify({
                    "mensaje": "No se enviaron campos válidos"
                }), 400

            if "precio" in campos_permitidos:
                if not isinstance(campos_permitidos["precio"], (int, float)):
                    return jsonify({
                        "mensaje": "El precio debe ser numérico"
                    }), 400

                if campos_permitidos["precio"] < 0:
                    return jsonify({
                        "mensaje": "El precio no puede ser negativo"
                    }), 400

            if "stock" in campos_permitidos:
                if not isinstance(campos_permitidos["stock"], int):
                    return jsonify({
                        "mensaje": "El stock debe ser un número entero"
                    }), 400

                if campos_permitidos["stock"] < 0:
                    return jsonify({
                        "mensaje": "El stock no puede ser negativo"
                    }), 400

            PrendaModel.actualizar(prenda_id, campos_permitidos)

            return jsonify({
                "mensaje": "Prenda actualizada correctamente"
            }), 200

        except InvalidId:
            return jsonify({
                "mensaje": "El ID proporcionado no es válido"
            }), 400

    @staticmethod
    def eliminar(prenda_id):
        try:
            prenda = PrendaModel.obtener_por_id(prenda_id)

            if not prenda:
                return jsonify({
                    "mensaje": "Prenda no encontrada"
                }), 404

            PrendaModel.eliminar(prenda_id)

            return jsonify({
                "mensaje": "Prenda eliminada correctamente"
            }), 200

        except InvalidId:
            return jsonify({
                "mensaje": "El ID proporcionado no es válido"
            }), 400