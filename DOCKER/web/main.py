from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)
DB_PATH = 'reservas.db'

def init_db():
    if not os.path.exists(DB_PATH):
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute('''CREATE TABLE reservas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                fecha TEXT NOT NULL,
                tipo TEXT NOT NULL
            )''')

@app.route('/', methods=['GET', 'POST'])
def reservas_hotel():
    mensaje = None
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        fecha = request.form.get('fecha')
        tipo = request.form.get('tipo')
        if nombre and fecha and tipo:
            with sqlite3.connect(DB_PATH) as conn:
                conn.execute('INSERT INTO reservas (nombre, fecha, tipo) VALUES (?, ?, ?)', (nombre, fecha, tipo))
            mensaje = 'Reserva realizada con éxito.'
        else:
            mensaje = 'Todos los campos son obligatorios.'
    with sqlite3.connect(DB_PATH) as conn:
        reservas = conn.execute('SELECT nombre, fecha, tipo FROM reservas').fetchall()
    return render_template('reservas.html', reservas=reservas, mensaje=mensaje)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
