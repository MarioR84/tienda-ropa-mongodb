from bson import ObjectId
from config.database import db


class PrendaModel:
    coleccion = db["prendas"]

    @staticmethod
    def obtener_todas():
        prendas = []

        for prenda in PrendaModel.coleccion.find():
            prenda["_id"] = str(prenda["_id"])
            prendas.append(prenda)

        return prendas

    @staticmethod
    def obtener_por_id(prenda_id):
        prenda = PrendaModel.coleccion.find_one(
            {"_id": ObjectId(prenda_id)}
        )

        if prenda:
            prenda["_id"] = str(prenda["_id"])

        return prenda

    @staticmethod
    def crear(datos):
        resultado = PrendaModel.coleccion.insert_one(datos)
        return str(resultado.inserted_id)

    @staticmethod
    def actualizar(prenda_id, datos):
        resultado = PrendaModel.coleccion.update_one(
            {"_id": ObjectId(prenda_id)},
            {"$set": datos}
        )

        return resultado.modified_count

    @staticmethod
    def eliminar(prenda_id):
        resultado = PrendaModel.coleccion.delete_one(
            {"_id": ObjectId(prenda_id)}
        )

        return resultado.deleted_count