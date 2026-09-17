import time
import random 

def le_sensor():
    return random.uniform(20,30)

def registra(temperatura):
    print(f"Temperatura:{temperatura:.1f}°c")

while True:
    temperatura = le_sensor()
    registra(temperatura)
    time.sleep(10)