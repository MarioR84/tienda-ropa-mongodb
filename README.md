README.md
API Tienda de Ropa 👕

Universidad Florencio del Castillo

Carrera: Ingeniería Informática

Curso: Desarrollo con Plataformas Abiertas

Proyecto: Segundo Proyecto

Docente: Daniel Bogarín Granados

Estudiante: Mario Rodríguez

Descripción

Este proyecto consiste en el desarrollo de una API REST utilizando Python, Flask y MongoDB Atlas para administrar la información de una tienda de ropa.

La API implementa una arquitectura por capas (Configuración, Modelos, Controladores y Rutas), permitiendo realizar operaciones CRUD para las colecciones de la base de datos y generar los reportes solicitados en el proyecto.

Objetivos
Administrar las marcas de la tienda.
Administrar los usuarios.
Administrar las prendas.
Administrar las ventas.
Generar reportes mediante consultas en MongoDB.
Aplicar una arquitectura por capas utilizando programación orientada a objetos.
Tecnologías utilizadas
Tecnología	Descripción
Python	Lenguaje de programación
Flask	Framework para desarrollar la API
MongoDB Atlas	Base de datos NoSQL
PyMongo	Conector entre Python y MongoDB
Postman	Pruebas de los endpoints
GitHub	Repositorio del proyecto
Arquitectura
API
│
├── config
│   └── database.py
│
├── controllers
│   ├── marca_controller.py
│   ├── usuario_controller.py
│   ├── prenda_controller.py
│   ├── venta_controller.py
│   └── reporte_controller.py
│
├── models
│   ├── marca_model.py
│   ├── usuario_model.py
│   ├── prenda_model.py
│   ├── venta_model.py
│   └── reporte_model.py
│
├── routes
│   ├── marca_routes.py
│   ├── usuario_routes.py
│   ├── prenda_routes.py
│   ├── venta_routes.py
│   └── reporte_routes.py
│
├── app.py
├── requirements.txt
└── .env
Instalación

Clonar el repositorio.

Entrar a la carpeta API.

Instalar las dependencias:

pip install -r requirements.txt

Ejecutar la aplicación:

python app.py

La API estará disponible en:

http://127.0.0.1:5000
Documentación de Endpoints
Marcas
Acción	Método	Endpoint
Obtener todas las marcas	GET	/marcas
Obtener una marca	GET	/marcas/{id}
Crear marca	POST	/marcas
Actualizar marca	PUT	/marcas/{id}
Eliminar marca	DELETE	/marcas/{id}
Ejemplo para crear una marca
{
    "nombre":"Nike",
    "pais":"Estados Unidos"
}
Usuarios
Acción	Método	Endpoint
Obtener usuarios	GET	/usuarios
Obtener usuario	GET	/usuarios/{id}
Crear usuario	POST	/usuarios
Actualizar usuario	PUT	/usuarios/{id}
Eliminar usuario	DELETE	/usuarios/{id}
Ejemplo
{
    "nombre":"Mario Rodríguez",
    "correo":"mario@gmail.com",
    "telefono":"88888888",
    "direccion":"Cartago"
}
Prendas
Acción	Método	Endpoint
Obtener prendas	GET	/prendas
Obtener prenda	GET	/prendas/{id}
Crear prenda	POST	/prendas
Actualizar prenda	PUT	/prendas/{id}
Eliminar prenda	DELETE	/prendas/{id}
Ejemplo
{
    "nombre":"Camiseta Deportiva",
    "marca":"Nike",
    "talla":"M",
    "precio":18000,
    "stock":25
}
Ventas
Acción	Método	Endpoint
Obtener ventas	GET	/ventas
Obtener venta	GET	/ventas/{id}
Crear venta	POST	/ventas
Actualizar venta	PUT	/ventas/{id}
Eliminar venta	DELETE	/ventas/{id}
Ejemplo
{
    "fecha":"2026-07-20",
    "cliente":"Mario Rodríguez",
    "prenda":"Camiseta Deportiva",
    "marca":"Nike",
    "cantidad":2,
    "total":36000
}
Reportes
1. Marcas con al menos una venta

Método

GET

Endpoint

/reportes/marcas-con-ventas

Este reporte devuelve todas las marcas que poseen al menos una venta registrada.

2. Prendas vendidas con stock restante

Método

GET

Endpoint

/reportes/prendas-vendidas-stock

Este reporte muestra la cantidad vendida de cada prenda junto con el stock disponible.

3. Cinco marcas más vendidas

Método

GET

Endpoint

/reportes/cinco-marcas-mas-vendidas

Este reporte devuelve las cinco marcas con mayor cantidad de ventas registradas.

Pruebas realizadas

La API fue probada utilizando Postman, verificando correctamente:

CRUD de Marcas.
CRUD de Usuarios.
CRUD de Prendas.
CRUD de Ventas.
Reportes solicitados.
Conclusiones

Durante el desarrollo del proyecto se implementó una API REST utilizando Flask y MongoDB Atlas aplicando una arquitectura por capas. Se desarrollaron operaciones CRUD para todas las colecciones y se implementaron los reportes solicitados, comprobando su funcionamiento mediante Postman.

Autor

Mario Rodríguez

Ingeniería Informática

Universidad Florencio del Castillo