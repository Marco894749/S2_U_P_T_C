from flask import Flask, render_template, request, redirect, url_for
import sqlite3  #bases de datos locales para proyectos 
from datetime import datetime

app = Flask(__name__)
DB_NAME = "ventas_velas.db"

def init_db():
    """Crea la tabla de ventas si aún no existe."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ventas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT NOT NULL,
            cliente TEXT NOT NULL,
            aroma TEXT NOT NULL,
            tamano TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            precio_unitario REAL NOT NULL,
            total REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Registrar una nueva venta
    if request.method == 'POST':
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
        cliente = request.form['cliente']
        aroma = request.form['aroma']
        tamano = request.form['tamano']
        cantidad = int(request.form['cantidad'])
        precio_unitario = float(request.form['precio_unitario'])
        total = cantidad * precio_unitario

        cursor.execute('''
            INSERT INTO ventas (fecha, cliente, aroma, tamano, cantidad, precio_unitario, total)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (fecha, cliente, aroma, tamano, cantidad, precio_unitario, total))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    # Consultar todas las ventas ordenadas de la más reciente a la más antigua
    cursor.execute('SELECT * FROM ventas ORDER BY id DESC')
    ventas = cursor.fetchall()

    # Calcular métricas generales
    cursor.execute('SELECT SUM(total) as ingresos, SUM(cantidad) as unidades FROM ventas')
    resumen = cursor.fetchone()
    ingresos_totales = resumen['ingresos'] if resumen['ingresos'] else 0.0
    unidades_vendidas = resumen['unidades'] if resumen['unidades'] else 0

    conn.close()

    return render_template(
        'index.html',
        ventas=ventas,
        ingresos_totales=ingresos_totales,
        unidades_vendidas=unidades_vendidas
    )

@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_venta(id):
    """Elimina un registro de venta por su ID."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM ventas WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
