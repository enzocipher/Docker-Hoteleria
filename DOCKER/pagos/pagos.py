# pagos.py - Servicio simulado de pagos
from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route('/pagar', methods=['POST'])
def pagar():
    data = request.json
    # Simula procesamiento de pago
    time.sleep(1)
    return jsonify({'status': 'ok', 'mensaje': 'Pago procesado', 'detalle': data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
