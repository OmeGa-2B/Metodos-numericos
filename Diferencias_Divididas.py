import numpy as np

def diferencias_divididas(x, y):
    n = len(x)
    coef = np.zeros([n, n])
    coef[:,0] = y

    try:
        for i in range(1, n):
            for j in range(n - i):
                if (x[j + i] - x[j]) == 0:
                    print("se a intentado dicidir entre 0")
                    return False
                else:
                    coef[j, i] = (coef[j + 1, i - 1] - coef[j, i - 1]) / (x[j + i] - x[j])
    except Exception as e:
        print("Ocurrio una excepcion: {}".format(e))

    return coef

def polinomio_newton(coef, x_data, x):
    """
    coef: Coeficientes del polinomio de Newton.
    x_data: Puntos x originales.
    x: Punto en el cual se evalúa el polinomio.
    return: Valor del polinomio en x.
    """
    n = len(x_data) - 1
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n - k] + (x - x_data[n - k]) * p
    return p

if __name__ == "__main__":
    # Solicitar el número de puntos al usuario
    num_puntos = int(input("Ingrese el número de puntos: "))

    # Inicializar listas para los puntos x e y
    x_p = []
    y_p = []

    # Solicitar los puntos x e y al usuario
    for i in range(num_puntos):
        x = float(input(f"Ingrese x_{i}: "))
        y = float(input(f"Ingrese y_{i}: "))
        x_p.append(x)
        y_p.append(y)

    # Generar la tabla de diferencias divididas
    coef = diferencias_divididas(x_p, y_p)
    if coef == False:
        print("Error")
    else:
        # Solicitar el punto a evaluar al usuario
        x = float(input("Ingrese el punto x a evaluar: "))

        # Evaluar el polinomio en el punto x
        y = polinomio_newton(coef, x_p, x)
        print(f"El valor interpolado en x = {x} es y = {y}")

        # Guardar los resultados en un archivo de texto
        with open('resultado_diferencias_divididas.txt', 'w') as archivo:
            archivo.write(f"Puntos x: {x_p}\n")
            archivo.write(f"Puntos y: {y_p}\n")
            archivo.write("Tabla de diferencias divididas:\n")
            for row in coef:
                archivo.write(f"{row}\n")
            archivo.write(f"\nValor interpolado en x = {x}: y = {y}\n")

        print("Los resultados se han guardado en 'resultado_diferencias_divididas.txt'.")
