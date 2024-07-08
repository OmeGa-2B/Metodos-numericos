import numpy as np
import matplotlib.pyplot as plt

"""
un solo archivo
# Leer el archivo .dat usando numpy
data = np.loadtxt('data.dat')

# Separar las columnas en X e y
X = data[:, 0]
y = data[:, 1]
"""
"""
dos archivos
def read_data(file_path):
    data = np.loadtxt(file_path)
    return data

# Rutas de los archivos .dat
file_X = 'X_data.dat'
file_y = 'y_data.dat'

# Leer los datos de los archivos .dat
X = read_data(file_X)
y = read_data(file_y)
"""

def read_data(file_path):
    data = np.loadtxt(file_path)
    return data

# Ruta del archivo .dat
file_path = 'data.dat'

# Leer los datos del archivo .dat
X = read_data("")

# Generar datos de y (valores ficticios para este ejemplo)
y = 2 * X + 1 + np.random.randn(len(X)) * 0.5  # y = 2X + 1 + ruido gaussiano


# Calcular las medias de X y y
mean_X = np.mean(X)
mean_y = np.mean(y)

# Calcular b1 (pendiente)
numerator = np.sum((X - mean_X) * (y - mean_y))
denominator = np.sum((X - mean_X) ** 2)
b1 = numerator / denominator

# Calcular b0 (intersección)
b0 = mean_y - b1 * mean_X

# Mostrar los resultados
print("Intersección (b0):", b0)
print("Coeficiente (b1):", b1)

# Hacer predicciones
y_pred = b0 + b1 * X

# Gráfica
plt.scatter(X, y, color='blue')
plt.plot(X, y_pred, color='red', linewidth=2)
plt.xlabel("X")
plt.ylabel("y")
plt.title("Regresión Lineal por Mínimos Cuadrados")
plt.show()
