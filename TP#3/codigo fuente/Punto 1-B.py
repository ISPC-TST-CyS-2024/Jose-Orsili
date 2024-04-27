import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
tasa_carga_deseada = 1  # Amperios por hora
capacidad_bateria = 7  # Capacidad total de la batería en amperios
tiempo_simulacion = 10  # Tiempo de simulación en horas
dt = 0.1  # Incremento de tiempo en horas

# Inicialización del sistema
tiempo = np.arange(0, tiempo_simulacion, dt)  # Array de tiempo

# Simulación del sistema en lazo abierto
corriente_carga_abierto = np.ones_like(tiempo) * tasa_carga_deseada  # Corriente de carga constante en lazo abierto
carga_bateria_abierto = np.zeros_like(tiempo)  # Inicialización de la carga de la batería en lazo abierto
for i, t in enumerate(tiempo):
    if i > 0:
        carga_bateria_abierto[i] = carga_bateria_abierto[i - 1] + corriente_carga_abierto[i] * dt

# Simulación del sistema en lazo cerrado
carga_bateria_cerrado = np.zeros_like(tiempo)  # Inicialización de la carga de la batería en lazo cerrado
corriente_carga_cerrado = np.zeros_like(tiempo)  # Corriente de carga en lazo cerrado
for i, t in enumerate(tiempo):
    # Calcular la corriente de carga para mantener la tasa de carga deseada en lazo cerrado
    if carga_bateria_cerrado[i-1] < capacidad_bateria:
        corriente_carga_cerrado[i] = min(tasa_carga_deseada, capacidad_bateria - carga_bateria_cerrado[i-1])
    # Actualizar la carga de la batería en lazo cerrado
    carga_bateria_cerrado[i] = carga_bateria_cerrado[i - 1] + corriente_carga_cerrado[i] * dt if i > 0 else corriente_carga_cerrado[i] * dt

# Visualización de los resultados
plt.plot(tiempo, carga_bateria_abierto, label="Lazo Abierto")
plt.plot(tiempo, carga_bateria_cerrado, label="Lazo Cerrado")
plt.title('Comparación entre Lazo Abierto y Lazo Cerrado')
plt.xlabel('Tiempo (horas)')
plt.ylabel('Carga de la Batería (Amperios)')
plt.grid(True)
plt.legend()
plt.show()
