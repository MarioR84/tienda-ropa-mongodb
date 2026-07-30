const URL_API = "http://127.0.0.1:5000/prendas";
const API_TOKEN = "tienda-ropa-token-2026";

const botonCargar = document.getElementById("btnCargar");
const tablaPrendas = document.getElementById("tablaPrendas");
const mensaje = document.getElementById("mensaje");

botonCargar.addEventListener("click", cargarPrendas);

async function cargarPrendas() {
    mensaje.textContent = "Cargando prendas...";
    tablaPrendas.innerHTML = "";

    try {
        const respuesta = await fetch(URL_API, {
            method: "GET",
            headers: {
                Authorization: `Bearer ${API_TOKEN}`
            }
        });

        if (!respuesta.ok) {
            const errorApi = await respuesta.json().catch(() => ({}));
            throw new Error(
                errorApi.error || `Error HTTP: ${respuesta.status}`
            );
        }

        const datos = await respuesta.json();

        console.log("Respuesta de la API:", datos);

        const prendas = Array.isArray(datos)
            ? datos
            : datos.datos || [];

        if (!Array.isArray(prendas) || prendas.length === 0) {
            mensaje.textContent = "No se encontraron prendas.";
            return;
        }

        prendas.forEach((prenda) => {
            const fila = document.createElement("tr");

            fila.innerHTML = `
                <td>${prenda.nombre ?? "Sin dato"}</td>
                <td>${prenda.marca ?? "Sin dato"}</td>
                <td>${prenda.talla ?? "Sin dato"}</td>
                <td>₡${Number(prenda.precio ?? 0).toLocaleString("es-CR")}</td>
                <td>${prenda.stock ?? 0}</td>
            `;

            tablaPrendas.appendChild(fila);
        });

        mensaje.textContent =
            datos.mensaje ||
            `Se cargaron ${prendas.length} prendas correctamente.`;

    } catch (error) {
        console.error("Error al consumir la API:", error);
        mensaje.textContent = error.message;
    }
}