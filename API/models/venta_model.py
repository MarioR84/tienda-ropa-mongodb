from bson import ObjectId
from config.database import db


class VentaModel:
    coleccion = db["ventas"]

    @staticmethod
    def obtener_todas():
        ventas = []

        for venta in VentaModel.coleccion.find():
            venta["_id"] = str(venta["_id"])
            ventas.append(venta)

        return ventas

    @staticmethod
    def obtener_por_id(venta_id):
        venta = VentaModel.coleccion.find_one(
            {"_id": ObjectId(venta_id)}
        )

        if venta:
            venta["_id"] = str(venta["_id"])

        return venta

    @staticmethod
    def crear(datos):
        resultado = VentaModel.coleccion.insert_one(datos)
        return str(resultado.inserted_id)

    @staticmethod
    def actualizar(venta_id, datos):
        resultado = VentaModel.coleccion.update_one(
            {"_id": ObjectId(venta_id)},
            {"$set": datos}
        )

        return resultado.modified_count

    @staticmethod
    def eliminar(venta_id):
        resultado = VentaModel.coleccion.delete_one(
            {"_id": ObjectId(venta_id)}
        )

        return resultado.deleted_count