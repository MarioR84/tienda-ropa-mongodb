from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

from config.database import db
from routes.marca_routes import marca_bp
from routes.usuario_routes import usuario_bp
from routes.prenda_routes import prenda_bp
from routes.venta_routes import venta_bp
from routes.reporte_routes import reporte_bp

# Cargar las variables del archivo .env
load_dotenv()

# Crear la aplicación Flask
app = Flask(__name__)

# Permitir solicitudes desde el frontend
CORS(app)

# Registrar rutas
app.register_blueprint(marca_bp)
app.register_blueprint(usuario_bp)
app.register_blueprint(prenda_bp)
app.register_blueprint(venta_bp)
app.register_blueprint(reporte_bp)


@app.route("/")
def inicio():
    return "API Tienda de Ropa funcionando correctamente."


@app.route("/conexion")
def conexion():
    try:
        colecciones = db.list_collection_names()

        return {
            "mensaje": "Conexión exitosa",
            "colecciones": colecciones
        }

    except Exception as error:
        return {
            "error": str(error)
        }, 500


if __name__ == "__main__":
    app.run(debug=True)