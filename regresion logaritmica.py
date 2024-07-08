import numpy as np
import matplotlib.pyplot as plt

# Función para leer los datos de un archivo .dat con una sola columna
def read_data(file_path):
    data = np.loadtxt(file_path)
    return data

# Ruta del archivo .dat
file_path = ''

# Leer los datos del archivo .dat
X = read_data(file_path)

# Generar datos de y (supongamos que son valores logarítmicos con ruido)
y = 2 + 0.5 * np.log(X) + np.random.randn(len(X)) * 0.5

# Aplicar la transformación logarítmica a X
ln_X = np.log(X)

# Calcular las medias de ln_X y y
mean_ln_X = np.mean(ln_X)
mean_y = np.mean(y)

# Calcular b1 (pendiente)
numerator = np.sum((ln_X - mean_ln_X) * (y - mean_y))
denominator = np.sum((ln_X - mean_ln_X) ** 2)
b1 = numerator / denominator

# Calcular b0 (intersección)
b0 = mean_y - b1 * mean_ln_X

# Mostrar los resultados
print("Intersección (b0):", b0)
print("Coeficiente (b1):", b1)

# Hacer predicciones
y_pred = b0 + b1 * ln_X

# Gráfica
plt.scatter(X, y, color='blue')
plt.plot(X, y_pred, color='red', linewidth=2)
plt.xlabel("X")
plt.ylabel("y")
plt.title("Regresión Logarítmica por Mínimos Cuadrados")
plt.show()
