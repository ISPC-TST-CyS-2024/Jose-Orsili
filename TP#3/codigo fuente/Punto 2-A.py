import numpy as np
import matplotlib.pyplot as plt

# Definición de la función de transferencia del sistema en lazo cerrado
def sistema_lazo_cerrado(Kp, Tau):
    def tf(s):
        return Kp / (Tau * s + 1)
    return tf

# Parámetros del sistema
Kp = 2.0  # Ganancia proporcional
Tau = 1.0  # Constante de tiempo

# Definición de la función de transferencia del sistema en lazo cerrado
G = sistema_lazo_cerrado(Kp, Tau)

# Respuesta al escalón del sistema en lazo cerrado
t = np.linspace(0, 10, 1000)
y = 1.0 - 1.0 / (1 + Tau * t)  # Respuesta al escalón unitario

# Graficación de la respuesta al escalón
plt.plot(t, y, label='Respuesta al Escalón')
plt.title('Respuesta al Escalón de un Sistema de Control en Lazo Cerrado')
plt.xlabel('Tiempo')
plt.ylabel('Respuesta')
plt.grid(True)
plt.legend()
plt.show()
