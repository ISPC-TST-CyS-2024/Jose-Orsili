import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Definir los coeficientes del sistema
b = [1.0]  # Coeficientes del numerador
a = [1.0, -0.5]  # Coeficientes del denominador

# Calcular la respuesta en frecuencia
w, h = signal.freqz(b, a)

# Graficar la respuesta en magnitud
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(w, np.abs(h), 'b')
plt.title('Respuesta en Frecuencia')
plt.ylabel('Magnitud')

# Graficar la respuesta en fase
plt.subplot(2, 1, 2)
plt.plot(w, np.angle(h), 'g')
plt.xlabel('Frecuencia [rad/muestra]')
plt.ylabel('Fase [radianes]')
plt.show()