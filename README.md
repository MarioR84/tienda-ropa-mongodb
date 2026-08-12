# Tienda de Ropa

## Proyecto Final — Desarrollo con Plataformas Abiertas

**Universidad Florencio del Castillo**

- **Curso:** Desarrollo con Plataformas Abiertas
- **Proyecto:** Proyecto Final
- **Docente:** Daniel Bogarín Granados
- **Estudiante:** Mario Rodríguez

---

## Descripción

Tienda de Ropa es una aplicación web para administrar el inventario de prendas y consultar reportes de ventas. El proyecto integra una API REST desarrollada con Flask, una base de datos MongoDB Atlas y un frontend web que permite realizar el CRUD completo de prendas.

La API conserva la arquitectura por capas de los proyectos anteriores, separando modelos, controladores y rutas. Además de prendas, contiene operaciones CRUD para marcas, usuarios y ventas, junto con los reportes solicitados.

## Objetivos

- Administrar marcas, usuarios, prendas y ventas.
- Crear, consultar, actualizar y eliminar prendas desde el frontend.
- Generar reportes mediante consultas a MongoDB.
- Aplicar programación orientada a objetos y una arquitectura por capas.
- Proteger los recursos CRUD mediante un Bearer Token.

## Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Python | Lenguaje utilizado en el backend |
| Flask | Desarrollo de la API REST |
| MongoDB Atlas | Base de datos NoSQL en la nube |
| PyMongo | Conexión entre Python y MongoDB |
| HTML | Estructura del frontend |
| CSS | Presentación y diseño de las vistas |
| JavaScript | Consumo de la API e interacción del frontend |
| Postman | Pruebas de los endpoints |
| Git y GitHub | Control de versiones y alojamiento del repositorio |

## Estructura del repositorio

```text
tienda-ropa-mongodb/
├── API/
│   ├── config/          # Conexión con MongoDB Atlas
│   ├── controllers/     # Lógica de las solicitudes
│   ├── middleware/      # Validación del Bearer Token
│   ├── models/          # Acceso a datos y consultas
│   ├── routes/          # Endpoints de la API
│   ├── app.py           # Punto de entrada de Flask
│   ├── requirements.txt
│   └── .env             # Variables locales; no se versiona
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
└── scripts/
    ├── tiendaRopa.js    # Creación y consultas de apoyo en MongoDB
    ├── marcas.json
    ├── prendas.json
    ├── usuarios.json
    └── ventas.json
```

## Configuración

### Requisitos previos

- Python 3 y `pip`.
- Acceso a un clúster de MongoDB Atlas.
- Un navegador web.
- Un servidor HTTP local para servir el frontend.

### Variables de entorno

Dentro de `API/`, cree un archivo `.env` con las siguientes variables:

```dotenv
MONGO_URI=mongodb+srv://<usuario>:<contraseña>@<cluster>/<base_de_datos>?<opciones>
API_TOKEN=<token-secreto-elegido-por-usted>
```

- `MONGO_URI` debe ser la cadena de conexión entregada por MongoDB Atlas. El usuario de base de datos debe contar con los permisos necesarios y la dirección IP del equipo debe estar autorizada en Atlas.
- `API_TOKEN` debe ser un valor secreto acordado entre la API y el cliente. El frontend debe enviar exactamente ese mismo valor en el encabezado de autorización.
- No publique `.env`, contraseñas, tokens ni cadenas de conexión reales. El archivo ya está excluido mediante `.gitignore`.

## Cómo ejecutar la API

Desde la raíz del repositorio:

```bash
cd API
python -m venv .venv
```

Active el entorno virtual:

```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

```bash
# Linux o macOS
source .venv/bin/activate
```

Instale las dependencias y ejecute Flask:

```bash
pip install -r requirements.txt
python app.py
```

La API estará disponible en `http://127.0.0.1:5000`. La ruta `/` permite comprobar que el servicio está activo y `/conexion` verifica la conexión con la base de datos.

## Cómo ejecutar el frontend

Antes de iniciarlo, revise en `frontend/script.js` que la URL base apunte a `http://127.0.0.1:5000` y que el token usado por el cliente coincida con `API_TOKEN` de `API/.env`. No almacene una credencial real en un repositorio público.

En otra terminal, desde la raíz del repositorio, ejecute:

```bash
cd frontend
python -m http.server 5500
```

Abra `http://127.0.0.1:5500` en el navegador. La API debe permanecer en ejecución mientras se utiliza el frontend.

## Autenticación con Bearer Token

Un Bearer Token es un valor que el cliente incluye en cada solicitud protegida para identificarse ante la API. Se envía mediante el encabezado HTTP:

```http
Authorization: Bearer <API_TOKEN>
```

La API compara el valor recibido con `API_TOKEN` configurado en `.env`. Si falta el encabezado, su formato es incorrecto o el token no coincide, la solicitud es rechazada. En este proyecto, los CRUD de marcas, usuarios, prendas y ventas están protegidos; los endpoints actuales de reportes son de consulta pública.

## CRUD de prendas desde el frontend

La vista principal permite realizar las cuatro operaciones sin utilizar Postman:

- **Crear:** completar el formulario y guardar una prenda nueva.
- **Leer:** cargar y visualizar las prendas registradas.
- **Actualizar:** seleccionar **Editar**, modificar los datos y guardar los cambios.
- **Eliminar:** seleccionar **Eliminar** y confirmar la operación.

Los datos administrados son nombre, marca, talla, precio y stock.

### Endpoints principales de prendas

Todos requieren el encabezado `Authorization: Bearer <API_TOKEN>`.

| Acción | Método | Endpoint |
|---|---|---|
| Listar todas las prendas | `GET` | `/prendas` |
| Obtener una prenda | `GET` | `/prendas/{id}` |
| Crear una prenda | `POST` | `/prendas` |
| Actualizar una prenda | `PUT` | `/prendas/{id}` |
| Eliminar una prenda | `DELETE` | `/prendas/{id}` |

Ejemplo de cuerpo para crear o actualizar:

```json
{
  "nombre": "Camiseta Deportiva",
  "marca": "Nike",
  "talla": "M",
  "precio": 18000,
  "stock": 25
}
```

## Reportes

| Reporte | Método | Endpoint |
|---|---|---|
| Marcas con al menos una venta | `GET` | `/reportes/marcas-con-ventas` |
| Prendas vendidas y stock restante | `GET` | `/reportes/prendas-vendidas-stock` |
| Cinco marcas más vendidas | `GET` | `/reportes/cinco-marcas-mas-vendidas` |

- **Marcas con ventas:** muestra las marcas presentes en los registros de ventas.
- **Prendas vendidas y stock:** presenta la cantidad vendida y las existencias registradas para cada prenda.
- **Cinco marcas más vendidas:** clasifica las cinco marcas principales según sus unidades vendidas.

## Vistas del frontend

El menú superior permite cambiar entre cuatro vistas:

1. **Gestión de prendas:** formulario de creación y edición, listado de prendas y acciones para actualizar o eliminar registros.
2. **Marcas con ventas:** tabla con las marcas que cuentan con ventas registradas.
3. **Prendas vendidas y stock:** tabla comparativa de cantidades vendidas y existencias restantes.
4. **5 marcas más vendidas:** clasificación de las marcas con mayor cantidad de unidades vendidas.

Cada vista de reporte incluye una opción para actualizar sus datos desde la API.

## Otros endpoints CRUD conservados

La API también mantiene los recursos desarrollados anteriormente:

| Recurso | Listar/crear | Consultar/actualizar/eliminar por ID |
|---|---|---|
| Marcas | `/marcas` | `/marcas/{id}` |
| Usuarios | `/usuarios` | `/usuarios/{id}` |
| Ventas | `/ventas` | `/ventas/{id}` |

Para cada recurso se utiliza `GET` para consultar, `POST` para crear, `PUT` para actualizar y `DELETE` para eliminar, según corresponda. Estas rutas requieren Bearer Token.

## Pruebas

Los endpoints se pueden validar con Postman o desde el frontend. Las pruebas contemplan:

- CRUD de marcas.
- CRUD de usuarios.
- CRUD de prendas.
- CRUD de ventas.
- Autorización de solicitudes mediante Bearer Token.
- Los tres reportes solicitados.

## Conclusión

El Proyecto Final amplía la API REST de Flask y MongoDB Atlas con un frontend en HTML, CSS y JavaScript. La solución mantiene la arquitectura por capas y los CRUD anteriores, incorpora autenticación mediante Bearer Token y permite administrar prendas y consultar reportes desde una interfaz web.

## Autor

**Mario Rodríguez**  
Ingeniería Informática  
Universidad Florencio del Castillo
