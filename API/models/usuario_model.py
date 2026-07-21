from bson import ObjectId
from config.database import db


class UsuarioModel:
    coleccion = db["usuarios"]

    @staticmethod
    def obtener_todos():
        usuarios = []

        for usuario in UsuarioModel.coleccion.find():
            usuario["_id"] = str(usuario["_id"])
            usuarios.append(usuario)

        return usuarios

    @staticmethod
    def obtener_por_id(usuario_id):
        usuario = UsuarioModel.coleccion.find_one(
            {"_id": ObjectId(usuario_id)}
        )

        if usuario:
            usuario["_id"] = str(usuario["_id"])

        return usuario

    @staticmethod
    def crear(datos):
        resultado = UsuarioModel.coleccion.insert_one(datos)
        return str(resultado.inserted_id)

    @staticmethod
    def actualizar(usuario_id, datos):
        resultado = UsuarioModel.coleccion.update_one(
            {"_id": ObjectId(usuario_id)},
            {"$set": datos}
        )

        return resultado.modified_count

    @staticmethod
    def eliminar(usuario_id):
        resultado = UsuarioModel.coleccion.delete_one(
            {"_id": ObjectId(usuario_id)}
        )

        return resultado.deleted_count