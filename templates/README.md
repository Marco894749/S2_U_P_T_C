# Control de ventas de velas

Aplicación web sencilla para llevar el registro de ventas de un emprendimiento
de velas. Está desarrollada con Flask y guarda los datos en una base SQLite.

## Funcionalidades

- Registrar ventas con cliente, aroma, tamaño, cantidad y precio unitario.
- Calcular el total de cada venta automáticamente.
- Consultar el historial de ventas, ordenado de la más reciente a la más antigua.
- Ver el total de ingresos y las unidades vendidas.
- Eliminar ventas del historial.

## Requisitos

- Python 3.9 o posterior.
- `pip` (incluido normalmente con Python).

La interfaz carga Bootstrap desde un CDN, por lo que se requiere conexión a
Internet para obtener sus estilos.

## Instalación y ejecución

Abre una terminal en la carpeta del proyecto y crea un entorno virtual:

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS o Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instala las dependencias definidas en `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

Inicia la aplicación:

```bash
python app.py
```

Abre [http://127.0.0.1:5000](http://127.0.0.1:5000) en el navegador. Para
detener el servidor, pulsa `Ctrl+C` en la terminal.

Al iniciar, la aplicación crea la tabla `ventas` si todavía no existe en
`ventas_velas.db`, en la carpeta desde la que se ejecuta. El archivo de base de
datos contiene los registros del proyecto; conserva una copia de seguridad si
vas a modificar o reemplazar esos datos.

> La aplicación se ejecuta con el modo de depuración de Flask activado para
> desarrollo local. No la expongas directamente a Internet ni uses ese modo en
> producción.