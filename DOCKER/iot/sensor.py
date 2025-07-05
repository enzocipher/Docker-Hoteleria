# sensor.py - Simulación de dispositivo IoT (sensor de ocupación)
import time
import random

while True:
    ocupado = random.choice([True, False])
    print(f"[SENSOR] Habitación {'ocupada' if ocupado else 'libre'}")
    time.sleep(7)
