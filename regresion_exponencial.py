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

# Generar datos de y (supongamos que son valores exponenciales con ruido)
y = 2 * np.exp(0.5 * X) + np.random.randn(len(X)) * 0.5

# Aplicar la transformación logarítmica a y
ln_y = np.log(y)

# Calcular las medias de X y ln_y
mean_X = np.mean(X)
mean_ln_y = np.mean(ln_y)

# Calcular b1 (pendiente)
numerator = np.sum((X - mean_X) * (ln_y - mean_ln_y))
denominator = np.sum((X - mean_X) ** 2)
b1 = numerator / denominator

# Calcular b0 (intersección en la escala logarítmica)
b0 = mean_ln_y - b1 * mean_X

# Convertir b0 a la escala original
a = np.exp(b0)

# Mostrar los resultados
print("Intersección (a):", a)
print("Coeficiente (b):", b1)

# Hacer predicciones
y_pred = a * np.exp(b1 * X)

# Gráfica
plt.scatter(X, y, color='blue')
plt.plot(X, y_pred, color='red', linewidth=2)
plt.xlabel("X")
plt.ylabel("y")
plt.title("Regresión Exponencial por Mínimos Cuadrados")
plt.show()
