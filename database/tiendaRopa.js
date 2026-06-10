// ==========================================
// Proyecto: Tienda de Ropa
// Curso: Desarrollo con Plataformas Abiertas
// Base de datos: MongoDB
// ==========================================

// Crear y seleccionar la base de datos
use("tiendaRopa");

// ==========================================
// COLECCIÓN USUARIOS
// ==========================================

// Insertar un usuario
db.usuarios.insertOne({
nombre: "Mario Rodríguez",
correo: "[mario@gmail.com](mailto:mario@gmail.com)",
telefono: "88888888",
direccion: "Cartago"
});

// Insertar varios usuarios
db.usuarios.insertMany([
{
nombre: "Ana López",
correo: "[ana@gmail.com](mailto:ana@gmail.com)",
telefono: "87777777",
direccion: "San José"
},
{
nombre: "Carlos Ramírez",
correo: "[carlos@gmail.com](mailto:carlos@gmail.com)",
telefono: "86666666",
direccion: "Heredia"
}
]);

// Actualizar un usuario
db.usuarios.updateOne(
{ nombre: "Mario Rodríguez" },
{ $set: { telefono: "89999999" } }
);

// Eliminar un usuario
db.usuarios.deleteOne({
nombre: "Carlos Ramírez"
});
// ==========================================
// COLECCIÓN MARCAS
// ==========================================

// Insertar una marca
db.marcas.insertOne({
nombre: "Nike",
pais: "Estados Unidos"
});

// Insertar varias marcas
db.marcas.insertMany([
{
nombre: "Adidas",
pais: "Alemania"
},
{
nombre: "Puma",
pais: "Alemania"
}
]);

// Actualizar una marca
db.marcas.updateOne(
{ nombre: "Nike" },
{ $set: { pais: "USA" } }
);

// Eliminar una marca
db.marcas.deleteOne({
nombre: "Puma"
});

// ==========================================
// COLECCIÓN PRENDAS
// ==========================================

// Insertar una prenda
db.prendas.insertOne({
nombre: "Camiseta Deportiva",
marca: "Nike",
precio: 18000,
stock: 25
});

// Insertar varias prendas
db.prendas.insertMany([
{
nombre: "Pantalón Deportivo",
marca: "Adidas",
precio: 25000,
stock: 15
},
{
nombre: "Jeans",
marca: "Levis",
precio: 30000,
stock: 18
}
]);

// Actualizar una prenda
db.prendas.updateOne(
{ nombre: "Camiseta Deportiva" },
{ $set: { stock: 20 } }
);

// Eliminar una prenda
db.prendas.deleteOne({
nombre: "Jeans"
});

// ==========================================
// COLECCIÓN VENTAS
// ==========================================

// Insertar una venta
db.ventas.insertOne({
fecha: "2026-06-01",
marca: "Nike",
prenda: "Camiseta Deportiva",
cantidad: 2
});

// Insertar varias ventas
db.ventas.insertMany([
{
fecha: "2026-06-02",
marca: "Adidas",
prenda: "Pantalón Deportivo",
cantidad: 1
},
{
fecha: "2026-06-03",
marca: "Nike",
prenda: "Camiseta Deportiva",
cantidad: 3
}
]);

// Actualizar una venta
db.ventas.updateOne(
{ fecha: "2026-06-02" },
{ $set: { cantidad: 2 } }
);

// Eliminar una venta
db.ventas.deleteOne({
fecha: "2026-06-03"
});

