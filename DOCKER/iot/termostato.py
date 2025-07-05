# termostato.py - Simulación de dispositivo IoT (termostato)
import time
import random

while True:
    temperatura = round(random.uniform(18, 26), 2)
    print(f"[TERMOSTATO] Temperatura actual: {temperatura}°C")
    time.sleep(5)
