import numpy as np
import matplotlib.pyplot as plt

# Función de transferencia del sistema en lazo cerrado
def sistema_lazo_cerrado(Kp, Tau):
    def tf(s):
        return Kp / (Tau * s + 1)
    return tf

# Parámetros de análisis
Kp_values = [1.0, 2.0, 3.0]  # Valores de ganancia proporcional
Tau_values = [1.0, 2.0, 3.0]  # Valores de constante de tiempo
t = np.linspace(0, 10, 1000)  # Tiempo

# Graficación de la respuesta al escalón para diferentes valores de Kp y Tau
plt.figure(figsize=(12, 8))

for Kp in Kp_values:
    for Tau in Tau_values:
        G = sistema_lazo_cerrado(Kp, Tau)
        y = 1.0 - 1.0 / (1 + Tau * t)
        plt.plot(t, y, label=f'Kp={Kp}, Tau={Tau}')

plt.title('Respuesta al Escalón de un Sistema de Control en Lazo Cerrado')
plt.xlabel('Tiempo')
plt.ylabel('Respuesta')
plt.grid(True)
plt.legend()
plt.show()