from bson.errors import InvalidId
from flask import jsonify, request

from models.usuario_model import UsuarioModel


class UsuarioController:

    @staticmethod
    def listar():
        usuarios = UsuarioModel.obtener_todos()

        return jsonify({
            "mensaje": "Usuarios obtenidos correctamente",
            "datos": usuarios
        }), 200

    @staticmethod
    def obtener(usuario_id):
        try:
            usuario = UsuarioModel.obtener_por_id(usuario_id)

            if not usuario:
                return jsonify({
                    "mensaje": "Usuario no encontrado"
                }), 404

            return jsonify({
                "mensaje": "Usuario obtenido correctamente",
                "datos": usuario
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
            "correo",
            "telefono",
            "direccion"
        ]

        for campo in campos_obligatorios:
            if not datos.get(campo):
                return jsonify({
                    "mensaje": f"El campo {campo} es obligatorio"
                }), 400

        nuevo_usuario = {
            "nombre": datos["nombre"],
            "correo": datos["correo"],
            "telefono": datos["telefono"],
            "direccion": datos["direccion"]
        }

        usuario_id = UsuarioModel.crear(nuevo_usuario)

        return jsonify({
            "mensaje": "Usuario creado correctamente",
            "id": usuario_id
        }), 201

    @staticmethod
    def actualizar(usuario_id):
        datos = request.get_json()

        if not datos:
            return jsonify({
                "mensaje": "Debe enviar datos para actualizar"
            }), 400

        try:
            usuario = UsuarioModel.obtener_por_id(usuario_id)

            if not usuario:
                return jsonify({
                    "mensaje": "Usuario no encontrado"
                }), 404

            campos_permitidos = {}

            for campo in ["nombre", "correo", "telefono", "direccion"]:
                if campo in datos:
                    campos_permitidos[campo] = datos[campo]

            if not campos_permitidos:
                return jsonify({
                    "mensaje": "No se enviaron campos válidos"
                }), 400

            UsuarioModel.actualizar(usuario_id, campos_permitidos)

            return jsonify({
                "mensaje": "Usuario actualizado correctamente"
            }), 200

        except InvalidId:
            return jsonify({
                "mensaje": "El ID proporcionado no es válido"
            }), 400

    @staticmethod
    def eliminar(usuario_id):
        try:
            usuario = UsuarioModel.obtener_por_id(usuario_id)

            if not usuario:
                return jsonify({
                    "mensaje": "Usuario no encontrado"
                }), 404

            UsuarioModel.eliminar(usuario_id)

            return jsonify({
                "mensaje": "Usuario eliminado correctamente"
            }), 200

        except InvalidId:
            return jsonify({
                "mensaje": "El ID proporcionado no es válido"
            }), 400