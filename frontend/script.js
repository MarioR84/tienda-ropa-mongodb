const URL_BASE_API = "http://127.0.0.1:5000";
const URL_API = `${URL_BASE_API}/prendas`;
const API_TOKEN = "tienda-ropa-token-2026";

const REPORTES = {
    "marcas-ventas": {
        endpoint: "/reportes/marcas-con-ventas",
        tablaId: "tablaMarcasVentas",
        mensajeId: "mensajeMarcasVentas",
        campos: ["marca"]
    },
    "prendas-stock": {
        endpoint: "/reportes/prendas-vendidas-stock",
        tablaId: "tablaPrendasStock",
        mensajeId: "mensajePrendasStock",
        campos: ["prenda", "marca", "cantidad_vendida", "stock_restante"]
    },
    "marcas-top": {
        endpoint: "/reportes/cinco-marcas-mas-vendidas",
        tablaId: "tablaMarcasTop",
        mensajeId: "mensajeMarcasTop",
        campos: ["marca", "cantidad_vendida", "cantidad_ventas"]
    }
};

const formulario = document.getElementById("formPrenda");
const prendaId = document.getElementById("prendaId");
const nombre = document.getElementById("nombre");
const marca = document.getElementById("marca");
const talla = document.getElementById("talla");
const precio = document.getElementById("precio");
const stock = document.getElementById("stock");
const tituloFormulario = document.getElementById("tituloFormulario");
const botonGuardar = document.getElementById("btnGuardar");
const botonCancelar = document.getElementById("btnCancelar");
const botonCargar = document.getElementById("btnCargar");
const tablaPrendas = document.getElementById("tablaPrendas");
const mensaje = document.getElementById("mensaje");

let prendasActuales = [];
const reportesCargados = new Set();

formulario.addEventListener("submit", guardarPrenda);
botonCancelar.addEventListener("click", limpiarFormulario);
botonCargar.addEventListener("click", cargarPrendas);
tablaPrendas.addEventListener("click", manejarAccionTabla);
document.addEventListener("DOMContentLoaded", cargarPrendas);
document.querySelector(".navegacion").addEventListener("click", cambiarVista);
document.querySelectorAll("[data-recargar]").forEach((boton) => {
    boton.addEventListener("click", () => cargarReporte(boton.dataset.recargar));
});

async function solicitarApi(url = URL_API, opciones = {}) {
    const encabezados = {
        Authorization: `Bearer ${API_TOKEN}`,
        ...opciones.headers
    };

    const respuesta = await fetch(url, {
        ...opciones,
        headers: encabezados
    });

    const datos = await respuesta.json().catch(() => ({}));

    if (!respuesta.ok) {
        throw new Error(
            datos.error || datos.mensaje || `Error HTTP: ${respuesta.status}`
        );
    }

    return datos;
}

async function cargarPrendas() {
    mostrarMensaje("Cargando prendas...", "informacion");
    botonCargar.disabled = true;

    try {
        const respuesta = await solicitarApi();
        prendasActuales = Array.isArray(respuesta)
            ? respuesta
            : respuesta.datos || [];

        renderizarPrendas(prendasActuales);

        if (prendasActuales.length === 0) {
            mostrarMensaje("No hay prendas registradas.", "informacion");
        } else {
            mostrarMensaje(
                `Se cargaron ${prendasActuales.length} prendas correctamente.`,
                "exito"
            );
        }
    } catch (error) {
        prendasActuales = [];
        renderizarPrendas([]);
        mostrarMensaje(`No fue posible cargar las prendas: ${error.message}`, "error");
    } finally {
        botonCargar.disabled = false;
    }
}

function renderizarPrendas(prendas) {
    tablaPrendas.replaceChildren();

    if (prendas.length === 0) {
        const fila = document.createElement("tr");
        const celda = document.createElement("td");
        celda.colSpan = 6;
        celda.className = "tabla-vacia";
        celda.textContent = "No hay prendas para mostrar.";
        fila.appendChild(celda);
        tablaPrendas.appendChild(fila);
        return;
    }

    prendas.forEach((prenda) => {
        const fila = document.createElement("tr");
        agregarCelda(fila, prenda.nombre ?? "Sin dato");
        agregarCelda(fila, prenda.marca ?? "Sin dato");
        agregarCelda(fila, prenda.talla ?? "Sin dato");
        agregarCelda(
            fila,
            `₡${Number(prenda.precio ?? 0).toLocaleString("es-CR")}`
        );
        agregarCelda(fila, prenda.stock ?? 0);

        const acciones = document.createElement("td");
        acciones.className = "acciones-tabla";
        acciones.appendChild(crearBotonAccion("Editar", "editar", prenda._id));
        acciones.appendChild(crearBotonAccion("Eliminar", "eliminar", prenda._id));
        fila.appendChild(acciones);
        tablaPrendas.appendChild(fila);
    });
}

function agregarCelda(fila, valor) {
    const celda = document.createElement("td");
    celda.textContent = valor;
    fila.appendChild(celda);
}

function crearBotonAccion(texto, accion, id) {
    const boton = document.createElement("button");
    boton.type = "button";
    boton.textContent = texto;
    boton.dataset.accion = accion;
    boton.dataset.id = id;
    boton.className = accion === "eliminar" ? "boton-peligro" : "boton-editar";
    return boton;
}

function manejarAccionTabla(evento) {
    const boton = evento.target.closest("button[data-accion]");

    if (!boton) {
        return;
    }

    if (boton.dataset.accion === "editar") {
        cargarPrendaEnFormulario(boton.dataset.id);
    } else if (boton.dataset.accion === "eliminar") {
        eliminarPrenda(boton.dataset.id);
    }
}

function cargarPrendaEnFormulario(id) {
    const prenda = prendasActuales.find((item) => item._id === id);

    if (!prenda) {
        mostrarMensaje("No se encontró la prenda seleccionada.", "error");
        return;
    }

    prendaId.value = prenda._id;
    nombre.value = prenda.nombre ?? "";
    marca.value = prenda.marca ?? "";
    talla.value = prenda.talla ?? "";
    precio.value = prenda.precio ?? "";
    stock.value = prenda.stock ?? "";
    tituloFormulario.textContent = "Editar prenda";
    botonGuardar.textContent = "Guardar cambios";
    botonCancelar.classList.remove("oculto");
    nombre.focus();
    formulario.scrollIntoView({ behavior: "smooth", block: "start" });
    mostrarMensaje("Edita los datos y guarda los cambios.", "informacion");
}

async function guardarPrenda(evento) {
    evento.preventDefault();

    if (!formulario.reportValidity()) {
        return;
    }

    const id = prendaId.value;
    const esEdicion = Boolean(id);
    const datosPrenda = {
        nombre: nombre.value.trim(),
        marca: marca.value.trim(),
        talla: talla.value.trim(),
        precio: Number(precio.value),
        stock: Number(stock.value)
    };

    if (!datosPrenda.nombre || !datosPrenda.marca || !datosPrenda.talla) {
        mostrarMensaje("Completa todos los campos de la prenda.", "error");
        return;
    }

    cambiarEstadoFormulario(true);
    mostrarMensaje(
        esEdicion ? "Guardando cambios..." : "Creando prenda...",
        "informacion"
    );

    try {
        const respuesta = await solicitarApi(
            esEdicion ? `${URL_API}/${encodeURIComponent(id)}` : URL_API,
            {
                method: esEdicion ? "PUT" : "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(datosPrenda)
            }
        );

        limpiarFormulario();
        await cargarPrendas();
        mostrarMensaje(
            respuesta.mensaje ||
                (esEdicion
                    ? "Prenda actualizada correctamente."
                    : "Prenda creada correctamente."),
            "exito"
        );
    } catch (error) {
        mostrarMensaje(
            `No fue posible ${esEdicion ? "actualizar" : "crear"} la prenda: ${error.message}`,
            "error"
        );
    } finally {
        cambiarEstadoFormulario(false);
    }
}

async function eliminarPrenda(id) {
    const prenda = prendasActuales.find((item) => item._id === id);
    const nombrePrenda = prenda?.nombre || "esta prenda";

    if (!window.confirm(`¿Deseas eliminar ${nombrePrenda}?`)) {
        return;
    }

    mostrarMensaje(`Eliminando ${nombrePrenda}...`, "informacion");

    try {
        const respuesta = await solicitarApi(
            `${URL_API}/${encodeURIComponent(id)}`,
            { method: "DELETE" }
        );

        if (prendaId.value === id) {
            limpiarFormulario();
        }

        await cargarPrendas();
        mostrarMensaje(
            respuesta.mensaje || "Prenda eliminada correctamente.",
            "exito"
        );
    } catch (error) {
        mostrarMensaje(`No fue posible eliminar la prenda: ${error.message}`, "error");
    }
}

function limpiarFormulario() {
    formulario.reset();
    prendaId.value = "";
    tituloFormulario.textContent = "Agregar prenda";
    botonGuardar.textContent = "Guardar prenda";
    botonCancelar.classList.add("oculto");
}

function cambiarEstadoFormulario(deshabilitado) {
    Array.from(formulario.elements).forEach((elemento) => {
        elemento.disabled = deshabilitado;
    });
}

function mostrarMensaje(texto, tipo) {
    mensaje.textContent = texto;
    mensaje.className = `mensaje mensaje-${tipo}`;
}

function cambiarVista(evento) {
    const boton = evento.target.closest("button[data-vista]");

    if (!boton) {
        return;
    }

    const vistaSeleccionada = boton.dataset.vista;

    document.querySelectorAll(".vista").forEach((vista) => {
        vista.hidden = vista.id !== `vista-${vistaSeleccionada}`;
    });

    document.querySelectorAll(".nav-boton").forEach((item) => {
        const estaActivo = item === boton;
        item.classList.toggle("activo", estaActivo);
        item.setAttribute("aria-current", estaActivo ? "page" : "false");
    });

    if (REPORTES[vistaSeleccionada] && !reportesCargados.has(vistaSeleccionada)) {
        cargarReporte(vistaSeleccionada);
    }
}

async function cargarReporte(nombreReporte) {
    const configuracion = REPORTES[nombreReporte];

    if (!configuracion) {
        return;
    }

    const tabla = document.getElementById(configuracion.tablaId);
    const mensajeReporte = document.getElementById(configuracion.mensajeId);
    const botonRecargar = document.querySelector(`[data-recargar="${nombreReporte}"]`);

    mostrarMensajeReporte(mensajeReporte, "Cargando reporte...", "informacion");
    botonRecargar.disabled = true;

    try {
        const respuesta = await solicitarApi(`${URL_BASE_API}${configuracion.endpoint}`);
        const registros = Array.isArray(respuesta) ? respuesta : respuesta.datos || [];

        renderizarReporte(tabla, registros, configuracion.campos);
        reportesCargados.add(nombreReporte);

        const textoExito = registros.length === 0
            ? "El reporte no contiene registros."
            : respuesta.mensaje || `Reporte cargado: ${registros.length} registros.`;
        mostrarMensajeReporte(
            mensajeReporte,
            textoExito,
            registros.length === 0 ? "informacion" : "exito"
        );
    } catch (error) {
        renderizarReporte(tabla, [], configuracion.campos);
        mostrarMensajeReporte(
            mensajeReporte,
            `No fue posible cargar el reporte: ${error.message}`,
            "error"
        );
    } finally {
        botonRecargar.disabled = false;
    }
}

function renderizarReporte(tabla, registros, campos) {
    tabla.replaceChildren();

    if (registros.length === 0) {
        const fila = document.createElement("tr");
        const celda = document.createElement("td");
        celda.colSpan = campos.length;
        celda.className = "tabla-vacia";
        celda.textContent = "No hay datos para mostrar.";
        fila.appendChild(celda);
        tabla.appendChild(fila);
        return;
    }

    registros.forEach((registro) => {
        const fila = document.createElement("tr");
        campos.forEach((campo) => {
            agregarCelda(fila, registro[campo] ?? "Sin dato");
        });
        tabla.appendChild(fila);
    });
}

function mostrarMensajeReporte(elemento, texto, tipo) {
    elemento.textContent = texto;
    elemento.className = `mensaje mensaje-${tipo}`;
}
