from bson import ObjectId

from config.database import db


class MarcaModel:
    coleccion = db["marcas"]

    @staticmethod
    def obtener_todas():
        marcas = []

        for marca in MarcaModel.coleccion.find():
            marca["_id"] = str(marca["_id"])
            marcas.append(marca)

        return marcas

    @staticmethod
    def obtener_por_id(marca_id):
        marca = MarcaModel.coleccion.find_one(
            {"_id": ObjectId(marca_id)}
        )

        if marca:
            marca["_id"] = str(marca["_id"])

        return marca

    @staticmethod
    def crear(datos):
        resultado = MarcaModel.coleccion.insert_one(datos)
        return str(resultado.inserted_id)

    @staticmethod
    def actualizar(marca_id, datos):
        resultado = MarcaModel.coleccion.update_one(
            {"_id": ObjectId(marca_id)},
            {"$set": datos}
        )

        return resultado.modified_count

    @staticmethod
    def eliminar(marca_id):
        resultado = MarcaModel.coleccion.delete_one(
            {"_id": ObjectId(marca_id)}
        )

        return resultado.deleted_count