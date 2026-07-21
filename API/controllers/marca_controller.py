from bson.errors import InvalidId
from flask import jsonify, request

from models.marca_model import MarcaModel


class MarcaController:

    @staticmethod
    def listar():
        marcas = MarcaModel.obtener_todas()

        return jsonify({
            "mensaje": "Marcas obtenidas correctamente",
            "datos": marcas
        }), 200

    @staticmethod
    def obtener(marca_id):
        try:
            marca = MarcaModel.obtener_por_id(marca_id)

            if not marca:
                return jsonify({
                    "mensaje": "Marca no encontrada"
                }), 404

            return jsonify({
                "mensaje": "Marca obtenida correctamente",
                "datos": marca
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

        nombre = datos.get("nombre")

        if not nombre:
            return jsonify({
                "mensaje": "El campo nombre es obligatorio"
            }), 400

        nueva_marca = {
            "nombre": nombre
        }

        marca_id = MarcaModel.crear(nueva_marca)

        return jsonify({
            "mensaje": "Marca creada correctamente",
            "id": marca_id
        }), 201

    @staticmethod
    def actualizar(marca_id):
        datos = request.get_json()

        if not datos:
            return jsonify({
                "mensaje": "Debe enviar datos para actualizar"
            }), 400

        try:
            marca = MarcaModel.obtener_por_id(marca_id)

            if not marca:
                return jsonify({
                    "mensaje": "Marca no encontrada"
                }), 404

            campos_permitidos = {}

            if "nombre" in datos:
                campos_permitidos["nombre"] = datos["nombre"]

            if "pais" in datos:
                campos_permitidos["pais"] = datos["pais"]
            

            if not campos_permitidos:
                return jsonify({
                    "mensaje": "No se enviaron campos válidos"
                }), 400

            MarcaModel.actualizar(marca_id, campos_permitidos)

            return jsonify({
                "mensaje": "Marca actualizada correctamente"
            }), 200

        except InvalidId:
            return jsonify({
                "mensaje": "El ID proporcionado no es válido"
            }), 400

    @staticmethod
    def eliminar(marca_id):
        try:
            marca = MarcaModel.obtener_por_id(marca_id)

            if not marca:
                return jsonify({
                    "mensaje": "Marca no encontrada"
                }), 404

            MarcaModel.eliminar(marca_id)

            return jsonify({
                "mensaje": "Marca eliminada correctamente"
            }), 200

        except InvalidId:
            return jsonify({
                "mensaje": "El ID proporcionado no es válido"
            }), 400