import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Sistema lineal invariante en el tiempo (por ejemplo, un sistema de segundo orden)
numerator = [1]  # Coeficientes del numerador
denominator = [1, 2, 1]  # Coeficientes del denominador (s^2 + 2s + 1)

system = ctrl.TransferFunction(numerator, denominator)

# Diseñar un controlador PID
Kp = 1.0  # Coeficiente proporcional
Ki = 0.5  # Coeficiente integral
Kd = 0.1  # Coeficiente derivativo

controller = ctrl.TransferFunction([Kd, Kp, Ki], [1, 0])  # Controlador PID

# Conectar el controlador al sistema
closed_loop_system = ctrl.feedback(system * controller)

# Generar una respuesta a una entrada escalón
time, response = ctrl.step_response(closed_loop_system)

# Graficar la respuesta
plt.plot(time, response)
plt.xlabel('Tiempo')
plt.ylabel('Respuesta')
plt.title('Respuesta del sistema con controlador PID')
plt.grid(True)
plt.show()
