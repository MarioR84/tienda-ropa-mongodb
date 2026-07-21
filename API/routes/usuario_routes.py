from flask import Blueprint

from controllers.usuario_controller import UsuarioController


usuario_bp = Blueprint("usuario_bp", __name__)


@usuario_bp.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return UsuarioController.listar()


@usuario_bp.route("/usuarios/<usuario_id>", methods=["GET"])
def obtener_usuario(usuario_id):
    return UsuarioController.obtener(usuario_id)


@usuario_bp.route("/usuarios", methods=["POST"])
def crear_usuario():
    return UsuarioController.crear()


@usuario_bp.route("/usuarios/<usuario_id>", methods=["PUT"])
def actualizar_usuario(usuario_id):
    return UsuarioController.actualizar(usuario_id)


@usuario_bp.route("/usuarios/<usuario_id>", methods=["DELETE"])
def eliminar_usuario(usuario_id):
    return UsuarioController.eliminar(usuario_id)