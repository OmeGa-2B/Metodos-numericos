def interpolacion_neville(x, xi, fi):
    n = len(xi) - 1
    q = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # Inicializar la primera columna de la tabla Q con los valores de la función
    for i in range(n + 1):
        q[i][0] = fi[i]

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            q[i][j] = ( (x - xi[i - j]) * q[i][j - 1] - (x - xi[i]) * q[i - 1][j - 1] ) / (xi[i] - xi[i - j])

    return q[n][n]

def valores_listas():
    n = int(input("Ingrese el numero de valores para las xi: "))
    xi = []
    fi = []

    for i in range(n):
        a = float(input("Introduzca un valor para la lista de los valores en xi: "))
        xi.append(a)
        b = float(input("Introduzca un valor para la lista de los valores en fi: "))
        fi.append(b)

    return xi, fi

xi, fi = valores_listas()

if len(xi) != len(fi):
    print("Las listas xi y fi deben tener la misma longitud.")
else:
    x = float(input("Introduzca el valor a interpolar: "))
    result = interpolacion_neville(x, xi, fi)
    print(f"El valor interpolado en x = {x} es {result}")
