# 👕 API Tienda de Ropa

## Desarrollo con Plataformas Abiertas

**Universidad Florencio del Castillo**

- **Curso:** Desarrollo con Plataformas Abiertas
- **Proyecto:** Segundo Proyecto
- **Docente:** Daniel Bogarín Granados
- **Estudiante:** Mario Rodríguez

---

# 📖 Descripción

Este proyecto consiste en el desarrollo de una **API REST** utilizando **Python**, **Flask** y **MongoDB Atlas** para administrar la información de una tienda de ropa.

La API implementa una arquitectura por capas utilizando **Modelos**, **Controladores** y **Rutas**, permitiendo realizar operaciones CRUD para las colecciones de la base de datos y generar los reportes solicitados en el proyecto.

---

# 🎯 Objetivos

- Administrar las marcas de la tienda.
- Administrar los usuarios.
- Administrar las prendas.
- Administrar las ventas.
- Generar reportes utilizando MongoDB.
- Aplicar programación orientada a objetos mediante una arquitectura por capas.

---

# 🛠 Tecnologías utilizadas

| Tecnología | Descripción |
|------------|-------------|
| Python | Lenguaje de programación |
| Flask | Framework para desarrollar la API |
| MongoDB Atlas | Base de datos NoSQL |
| PyMongo | Conexión con MongoDB |
| Postman | Pruebas de la API |
| Git | Control de versiones |
| GitHub | Repositorio del proyecto |

---

# 📂 Arquitectura del proyecto

```text
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
```

---

# 🚀 Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/MarioR84/tienda-ropa-mongodb.git
```

## 2. Entrar a la carpeta API

```bash
cd API
```

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 4. Ejecutar la aplicación

```bash
python app.py
```

La API quedará disponible en:

```text
http://127.0.0.1:5000
```

---

# 📌 Endpoints

## 🏷 Marcas

| Acción | Método | Endpoint |
|---------|---------|----------|
| Obtener todas | GET | `/marcas` |
| Obtener por ID | GET | `/marcas/{id}` |
| Crear | POST | `/marcas` |
| Actualizar | PUT | `/marcas/{id}` |
| Eliminar | DELETE | `/marcas/{id}` |

### Ejemplo de creación

```json
{
  "nombre": "Nike",
  "pais": "Estados Unidos"
}
```

---

## 👤 Usuarios

| Acción | Método | Endpoint |
|---------|---------|----------|
| Obtener todos | GET | `/usuarios` |
| Obtener por ID | GET | `/usuarios/{id}` |
| Crear | POST | `/usuarios` |
| Actualizar | PUT | `/usuarios/{id}` |
| Eliminar | DELETE | `/usuarios/{id}` |

### Ejemplo

```json
{
  "nombre": "Mario Rodríguez",
  "correo": "mario@gmail.com",
  "telefono": "88888888",
  "direccion": "Cartago"
}
```

---

## 👕 Prendas

| Acción | Método | Endpoint |
|---------|---------|----------|
| Obtener todas | GET | `/prendas` |
| Obtener por ID | GET | `/prendas/{id}` |
| Crear | POST | `/prendas` |
| Actualizar | PUT | `/prendas/{id}` |
| Eliminar | DELETE | `/prendas/{id}` |

### Ejemplo

```json
{
  "nombre": "Camiseta Deportiva",
  "marca": "Nike",
  "talla": "M",
  "precio": 18000,
  "stock": 25
}
```

---

## 💰 Ventas

| Acción | Método | Endpoint |
|---------|---------|----------|
| Obtener todas | GET | `/ventas` |
| Obtener por ID | GET | `/ventas/{id}` |
| Crear | POST | `/ventas` |
| Actualizar | PUT | `/ventas/{id}` |
| Eliminar | DELETE | `/ventas/{id}` |

### Ejemplo

```json
{
  "fecha": "2026-07-20",
  "cliente": "Mario Rodríguez",
  "prenda": "Camiseta Deportiva",
  "marca": "Nike",
  "cantidad": 2,
  "total": 36000
}
```

---

# 📊 Reportes

| Reporte | Método | Endpoint |
|----------|---------|----------|
| Marcas con al menos una venta | GET | `/reportes/marcas-con-ventas` |
| Prendas vendidas con stock restante | GET | `/reportes/prendas-vendidas-stock` |
| Cinco marcas más vendidas | GET | `/reportes/cinco-marcas-mas-vendidas` |

### Marcas con ventas

Obtiene todas las marcas que tienen al menos una venta registrada.

### Prendas vendidas con stock

Muestra cada prenda vendida junto con la cantidad restante en inventario.

### Cinco marcas más vendidas

Lista las cinco marcas con mayor cantidad de ventas registradas.

---

# ✅ Pruebas

Todos los endpoints fueron probados utilizando **Postman**, verificando correctamente:

- CRUD de Marcas.
- CRUD de Usuarios.
- CRUD de Prendas.
- CRUD de Ventas.
- Reportes solicitados.

---

# 📌 Conclusión

Con este proyecto se desarrolló una API REST utilizando Flask y MongoDB Atlas, implementando una arquitectura por capas, operaciones CRUD para todas las colecciones y los reportes solicitados. El funcionamiento de la API fue validado mediante pruebas realizadas con Postman.

---

# 👨‍💻 Autor

**Mario Rodríguez**

Ingeniería Informática

Universidad Florencio del Castillo