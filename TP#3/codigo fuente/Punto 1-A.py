import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
tasa_carga_deseada = 5  # Amperios por hora
capacidad_bateria = 7  # Capacidad total de la batería en amperios
tiempo_simulacion = 10  # Tiempo de simulación en horas
dt = 0.1  # Incremento de tiempo en horas

# Inicialización del sistema
tiempo = np.arange(0, tiempo_simulacion, dt)  # Array de tiempo
corriente_carga_abierto = np.ones_like(tiempo) * tasa_carga_deseada  # Corriente de carga constante

# Simulación del sistema en lazo abierto
carga_bateria_abierto = np.zeros_like(tiempo)  # Inicialización de la carga de la batería
for i, t in enumerate(tiempo):
    if i > 0:
        carga_bateria_abierto[i] = carga_bateria_abierto[i - 1] + corriente_carga_abierto[i] * dt

# Visualización de los resultados del lazo abierto
plt.plot(tiempo, carga_bateria_abierto, label="Lazo Abierto")
plt.title('Cargador de Baterías')
plt.xlabel('Tiempo (horas)')
plt.ylabel('Carga de la Batería (Amperios)')
plt.grid(True)
plt.legend()
plt.show()