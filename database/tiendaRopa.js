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

