import math  # Importamos el módulo math para funciones matemáticas avanzadas

def simpson_rule(f, a, b, n):
    """
    Implementa la Regla compuesta de Simpson para aproximar una integral definida.
    Parámetros:
    f -- la función a integrar
    a -- límite inferior de integración
    b -- límite superior de integración
    n -- número de subintervalos (debe ser par)
    """
    if n % 2 != 0:
        raise ValueError("n debe ser un número par")
    try: 
        h = (b - a) / n  # Calcula el ancho de cada subintervalo
    except Exception as e:
        print(f"A ocurrido un error: {e}")

    x0 = f(a) + f(b)  # Suma de los valores en los extremos
    x1 = 0  # Suma de los valores en los puntos impares
    x2 = 0  # Suma de los valores en los puntos pares

    for i in range(1, n):
        x = a + i * h  # Calcula el punto actual

        if i % 2 == 0:
            x2 += f(x)  # Suma para puntos pares
        else:
            x1 += f(x)  # Suma para puntos impares

    return h * (x0 + 2 * x2 + 4 * x1) / 3  # Fórmula final de Simpson


if __name__ == '__main__':
    # Solicitar la función al usuario
    try:
        func_str = input("Introduce la función a integrar (usa 'x' como variable, por ejemplo 'x**2 + 2*x'): ")

        # Crear una función lambda a partir de la entrada del usuario
        # Usamos eval() para convertir la cadena en una expresión ejecutable
        f = lambda x: eval(func_str)
    except Exception as e:
        print(f"Ocurrió un error al convertir la cadena: {e}")
    # Solicitar los límites de integración y el número de subintervalos
    a = float(input("Introduce el límite inferior de integración: "))
    b = float(input("Introduce el límite superior de integración: "))
    n = int(input("Introduce el número de subintervalos (debe ser par): "))

    try:
        # Intentamos calcular la integral
        result = simpson_rule(f, a, b, n)
        print(f"La aproximación de la integral es: {result}")
    except ValueError as e:
        # Capturamos errores específicos de valor (como n no par)
        print(f"Error: {e}")
    except Exception as e:
        # Capturamos cualquier otro error (como errores en la función introducida)
        print(f"Ocurrió un error al evaluar la función o calcular la integral: {e}")