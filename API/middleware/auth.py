from functools import wraps
from flask import request, jsonify
import os


def token_requerido(funcion):
    @wraps(funcion)
    def decorador(*args, **kwargs):
        encabezado_autorizacion = request.headers.get("Authorization")

        if not encabezado_autorizacion:
            return jsonify({
                "error": "Token no proporcionado"
            }), 401

        partes = encabezado_autorizacion.split()

        if len(partes) != 2 or partes[0].lower() != "bearer":
            return jsonify({
                "error": "Formato de token inválido"
            }), 401

        token_recibido = partes[1]
        token_valido = os.getenv("API_TOKEN")

        if not token_valido:
            return jsonify({
                "error": "El token de la API no está configurado"
            }), 500

        if token_recibido != token_valido:
            return jsonify({
                "error": "Token no válido"
            }), 401

        return funcion(*args, **kwargs)

    return decorador