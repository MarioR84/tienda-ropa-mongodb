from flask import Blueprint

from controllers.usuario_controller import UsuarioController
from middleware.auth import token_requerido


usuario_bp = Blueprint("usuario_bp", __name__)


@usuario_bp.route("/usuarios", methods=["GET"])
@token_requerido
def listar_usuarios():
    return UsuarioController.listar()


@usuario_bp.route("/usuarios/<usuario_id>", methods=["GET"])
@token_requerido
def obtener_usuario(usuario_id):
    return UsuarioController.obtener(usuario_id)


@usuario_bp.route("/usuarios", methods=["POST"])
@token_requerido
def crear_usuario():
    return UsuarioController.crear()


@usuario_bp.route("/usuarios/<usuario_id>", methods=["PUT"])
@token_requerido
def actualizar_usuario(usuario_id):
    return UsuarioController.actualizar(usuario_id)


@usuario_bp.route("/usuarios/<usuario_id>", methods=["DELETE"])
@token_requerido
def eliminar_usuario(usuario_id):
    return UsuarioController.eliminar(usuario_id)