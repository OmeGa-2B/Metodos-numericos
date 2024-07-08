

def lista_coeficientes(n):
    lista_c = []
    for i in range(n):
        c = float(input(f"Ingrese el coeficioente {i+1}: "))
        lista_c.append(c)
    return lista_c

def metodo_horner(grado,lista_c,x0):
    resultado = lista_c[0]
    for i in lista_c[1:]:
        resultado = resultado * x0 + i
    return resultado

if __name__ == '__main__':
    x0 = float(input("Ingrese la aproximacion inicial: "))
    grado_polinommio = int(input("Ingrese el grado del polinomio: "))
    lista_c = lista_coeficientes(grado_polinommio)
    p = metodo_horner(grado_polinommio,lista_c,x0)
    print(f"\nResultado del metodo: {p}")
    if not p:
        print("\nEl método de Muller no pudo encontrar una solución dentro del límite de iteraciones.")

