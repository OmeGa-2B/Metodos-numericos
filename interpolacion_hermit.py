# Función para calcular los coeficientes de interpolación de Hermite
def interpolacion_hermite(x, f, df):
    n = len(x) - 1
    # Inicializar la matriz Q y el vector z
    Q = [[0 for _ in range(2*n+2)] for _ in range(2*n+2)]
    z = [0] * (2*n+2)

    # Pasos 1 y 2 del algoritmo
    for i in range(n+1):
        # Llenar z con los valores de x repetidos
        z[2*i] = x[i]
        z[2*i+1] = x[i]
        # Asignar valores de f(x) y f'(x)
        Q[2*i][0] = f[i]
        Q[2*i+1][0] = f[i]
        Q[2*i+1][1] = df[i]

        # Calcular Q[2i][1] para i != 0
        if i != 0:
            try:
                Q[2*i][1] = (Q[2*i][0] - Q[2*i-1][0]) / (z[2*i] - z[2*i-1])
            except Exception as e:
                print("Se ha producido un error: {}".format(e))
                exit()

    # Pasos 3 y 4 del algoritmo
    for i in range(2, 2*n+2):
        for j in range(2, i+1):
            # Calcular los elementos restantes de Q
            try:
                Q[i][j] = (Q[i][j-1] - Q[i-1][j-1]) / (z[i] - z[i-j])
            except Exception as e:
                print("Se ha producido un error: {}".format(e))
                exit

    # Paso 5: Retornar los coeficientes (diagonal principal de Q)
    return [Q[i][i] for i in range(2*n+2)]

# Entrada de datos por el usuario
n = int(input("Ingrese el número de puntos: "))
x = []
f = []
df = []

# Solicitar al usuario los valores de x, f(x) y f'(x) para cada punto
for i in range(n):
    x.append(float(input(f"Ingrese x_{i}: ")))
    f.append(float(input(f"Ingrese f(x_{i}): ")))
    df.append(float(input(f"Ingrese f'(x_{i}): ")))

# Calcular los coeficientes
coeficientes = interpolacion_hermite(x, f, df)

# Guardar resultados en un archivo de texto
with open("resultados_hermite.txt", "w") as archivo:
    archivo.write("Coeficientes del polinomio de interpolación de Hermite:\n")
    for i, coef in enumerate(coeficientes):
        linea = f"Q_{i},{i} = {coef}\n"
        archivo.write(linea)
        print(linea.strip())  # También mostramos en consola

print("\nLos resultados se han guardado en 'resultados_hermite.txt'")