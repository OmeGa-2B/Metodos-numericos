from sympy import Symbol, N, sympify
import os

def verificacion_funcion_syntaxis():
    while True:
        try:
            ecuacion = input("\nIngrese la ecuacion con la cual se va a trabajar: ")
            return sympify(ecuacion)
        except Exception as e:
            print("\n-------------------------------")
            print("\nSe ha producido un error: ", e)
            print("\nPor favor intentelo de nuevo")
            print("\n-------------------------------")

def calculo_error_relativo(valor_medio1, valor_medio2):
    return abs((valor_medio2 - valor_medio1) / valor_medio2)

def intervalo():
    a = float(input("Introduzca el valor del extremo a del intervalo: "))
    b = float(input("Introduzca el valor del extremo b del intervalo: "))
    return a, b

def verificacion_valor_imagenes(funcion, a, b, Max_iteraciones, count, valor_medio1, tol=1e-6):
    x = Symbol('x')
    while True:
        try:
            f_a = N(funcion.subs(x, a))
            f_b = N(funcion.subs(x, b))
            break
        except Exception as e:
            print("\n-------------------------------")
            print("\nSe ha producido un error: ", e)
            print("\nLa funcion no está definida en el rango, introduzca un nuevo intervalo")
            a, b = intervalo()
            print("\n-------------------------------")

    archivo.write('\nIteracion: {}'.format(count))
    archivo.write('\na={}, b= {}, f(a) = {}, f(b) = {}'.format(a, b, f_a, f_b))

    try:
        if (b - a) / 2 > tol and count < Max_iteraciones:
            valor_medio = (a + b) / 2

            if count == 0:
                valor_medio1 = valor_medio
            else:
                error_relativo = calculo_error_relativo(valor_medio1, valor_medio)
                valor_medio1 = valor_medio
                archivo.write(" Error relativo: {}".format(error_relativo))
                if error_relativo < 0.0001:
                    return (a + b) / 2

            archivo.write('\n-----------------------------------------------------------------------------------------')

            f_vm = N(funcion.subs(x, valor_medio))
            if f_vm == 0:
                return valor_medio
            elif f_a * f_vm < 0:
                return verificacion_valor_imagenes(funcion, a, valor_medio, Max_iteraciones, count + 1, valor_medio1)
            else:
                return verificacion_valor_imagenes(funcion, valor_medio, b, Max_iteraciones, count + 1, valor_medio1)
        else:
            print(f"El método falló con {count} iteraciones")
    except:
        print(f"El método falló con {count} iteraciones")

if __name__ == '__main__':
    name = 'Metodo_biseccion.txt'
    dirc = ''
    dirc_completa = os.path.join(dirc, name)
    archivo = open(dirc_completa, 'w')

    funcion = verificacion_funcion_syntaxis()
    Max_iteraciones = int(input("Ingrese el número máximo de iteraciones que desea que se realicen: "))
    a, b = intervalo()
    solucion = verificacion_valor_imagenes(funcion, a, b, Max_iteraciones, 0, 0)

    if solucion is None:
        print("\nLa función está indeterminada en alguno de los extremos")
    else:
        print("La solución es: ", solucion)

    archivo.close()
