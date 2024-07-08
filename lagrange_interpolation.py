def lagrange_interpolation(x_p, y_p, x):

    n = len(x_p)
    r = 0
    try:
        for i in range(n):
            term = y_p[i]
            for j in range(n):
                if j != i:
                    term *= (x - x_p[j]) / (x_p[i] - x_p[j])
            r += term
    except Exception as e:
        print("Ocurrio un error: {}".format(e))

    return r

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

    # Solicitar el punto a evaluar al usuario
    x = float(input("Ingrese el punto x a evaluar: "))

    # Calcular la interpolación de Lagrange
    y = lagrange_interpolation(x_p, y_p, x)
    print(f"El valor interpolado en x = {x} es y = {y}")

    # Guardar los resultados en un archivo de texto
    with open('resultado_lagrange.txt', 'w') as archivo:
        archivo.write(f"Puntos x: {x_p}\n")
        archivo.write(f"Puntos y: {y_p}\n")
        archivo.write(f"Valor interpolado en x = {x}: y = {y}\n")

    print("Los resultados se han guardado en 'resultado_lagrange.txt'.")
