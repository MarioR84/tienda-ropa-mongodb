from config.database import db


class ReporteModel:

    @staticmethod
    def marcas_con_ventas():
        marcas = db["ventas"].distinct("marca")

        resultado = []

        for marca in sorted(marcas):
            resultado.append({
                "marca": marca
            })

        return resultado

    @staticmethod
    def prendas_vendidas_con_stock():
        pipeline = [
            {
                "$group": {
                    "_id": "$prenda",
                    "cantidad_vendida": {
                        "$sum": "$cantidad"
                    }
                }
            },
            {
                "$lookup": {
                    "from": "prendas",
                    "localField": "_id",
                    "foreignField": "nombre",
                    "as": "informacion_prenda"
                }
            },
            {
                "$unwind": {
                    "path": "$informacion_prenda",
                    "preserveNullAndEmptyArrays": True
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "prenda": "$_id",
                    "marca": "$informacion_prenda.marca",
                    "cantidad_vendida": 1,
                    "stock_restante": {
                        "$ifNull": [
                            "$informacion_prenda.stock",
                            0
                        ]
                    }
                }
            },
            {
                "$sort": {
                    "prenda": 1
                }
            }
        ]

        return list(db["ventas"].aggregate(pipeline))

    @staticmethod
    def cinco_marcas_mas_vendidas():
        pipeline = [
            {
                "$group": {
                    "_id": "$marca",
                    "cantidad_vendida": {
                        "$sum": "$cantidad"
                    },
                    "cantidad_ventas": {
                        "$sum": 1
                    }
                }
            },
            {
                "$sort": {
                    "cantidad_vendida": -1
                }
            },
            {
                "$limit": 5
            },
            {
                "$project": {
                    "_id": 0,
                    "marca": "$_id",
                    "cantidad_vendida": 1,
                    "cantidad_ventas": 1
                }
            }
        ]

        return list(db["ventas"].aggregate(pipeline))