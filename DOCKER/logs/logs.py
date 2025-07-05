# logs.py - Servicio simulado de logs/auditoría
from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log():
    data = request.json
    with open('eventos.log', 'a') as f:
        f.write(f"{datetime.datetime.now()} - {data}\n")
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
