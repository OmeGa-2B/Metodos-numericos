import numpy as np

def bairstow(a, r, s, tol, max_iter):
    n = len(a) - 1
    b = np.zeros_like(a)
    c = np.zeros_like(a)

    for iteration in range(max_iter):
        b[n] = a[n]
        b[n-1] = a[n-1] + r * b[n]

        for i in range(n-2, -1, -1):
            b[i] = a[i] + r * b[i+1] + s * b[i+2]

        c[n] = b[n]
        c[n-1] = b[n-1] + r * c[n]

        for i in range(n-2, -1, -1):
            c[i] = b[i] + r * c[i+1] + s * c[i+2]

        det = c[2] * c[2] - c[3] * c[1]

        if abs(det) < tol:
            raise ValueError("Determinante muy pequño.")

        dr = (b[1] * c[2] - b[0] * c[3]) / det
        ds = (b[0] * c[2] - b[1] * c[1]) / det

        r += dr
        s += ds

        if abs(dr) < tol and abs(ds) < tol:
            break
    else:
        raise ValueError("Maximo numero de iteraciones, no convergue.")

    return r, s, b

def quadratic_roots(r, s):
    disc = r * r + 4 * s
    if disc > 0:
        return [(-r + np.sqrt(disc)) / 2, (-r - np.sqrt(disc)) / 2]
    elif disc == 0:
        return [-r / 2]
    else:
        return [(-r / 2, np.sqrt(-disc) / 2), (-r / 2, -np.sqrt(-disc) / 2)]

def find_roots(a, tol, max_iter):
    roots = []
    while len(a) > 3:
        r, s = 1.0, -1.0
        r, s, b = bairstow(a, r, s, tol, max_iter)
        roots.extend(quadratic_roots(r, s))
        a = b[2:]

    if len(a) == 3:
        roots.extend(quadratic_roots(a[1], a[2]))
    elif len(a) == 2:
        roots.append(-a[1] / a[0])
    return roots

if __name__ == "__main__":
    # Solicitar los coeficientes del polinomio al usuario
    coeficientes = input("Ingrese los coeficientes del polinomio separados por espacios (del término de mayor grado al término independiente): ")
    coeficientes = list(map(float, coeficientes.split()))
    max_iteraciones = int(input("Ingrese el número máximo de iteraciones: "))

    # Encontrar las raíces del polinomio
    try:
        roots = find_roots(coeficientes, tol=1e-6, max_iter=max_iteraciones)
        print("Las raíces del polinomio son:", roots)

        # Guardar los resultados en un archivo de texto
        with open('resultado_bairstow.txt', 'w') as archivo:
            archivo.write("Coeficientes del polinomio: {}\n".format(coeficientes))
            archivo.write("Las raíces del polinomio son:\n")
            for root in roots:
                archivo.write("{}\n".format(root))

        print("Los resultados se han guardado en 'resultado_bairstow.txt'.")
    except Exception as e:
        print(f"Error: {e}")
