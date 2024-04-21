import time
import RPi.GPIO as GPIO

# Definir pines GPIO
sensor_pin = 17
heater_pin = 4

# Configurar pines GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)
GPIO.setup(heater_pin, GPIO.OUT)

# Definir temperatura objetivo
target_temperature = 20

while True:
    # Leer temperatura del sensor
    sensor_value = GPIO.input(sensor_pin)
    temperature = sensor_value / 1024 * 3.3

    # Controlar potencia del calentador
    if temperature < target_temperature:
        GPIO.output(heater_pin, GPIO.HIGH)
    else:
        GPIO.output(heater_pin, GPIO.LOW)

    # Imprimir temperatura actual
    print("Temperatura actual:", temperature)

    # Esperar un intervalo de tiempo
    time.sleep(1)
