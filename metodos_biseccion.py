from sympy.parsing.sympy_parser import parse_expr
from sympy import *
import os

def verificacion_funcion_syntaxis():
    while True:
        try:
            # sen = sin
            # e = exp()
            # pi = pi
            ecuacion = input("\nIngrese la ecuacion con la cual se va a trabajar: ")
            #parse_expr
            return sympify(ecuacion)

        except Exception as e:
            print("\n-------------------------------")
            print("\nSe ha producido un error: ",e)
            print("\nPor favor intentelo de nuevo")
            print("\n-------------------------------")

def calculo_error_relativo(valor_medio1, valor_medio2):
    return abs((valor_medio2-valor_medio1)/valor_medio2)

def verificacion_valor_imagenes(funcion,a,b,Max_iteraciones,count,valor_medio1, tol=1e-6):
    # tol es un parámetro utilizado en algoritmos numéricos para determinar
    # cuando se considera que una aproximación es lo suficientemente cercana a una solución exacta.

    #calculo de las imagenes
    x = Symbol('x')
    # = funcion.subs(x,a).evalf
    try:
        f_a = N(funcion.subs(x, a))
        f_b = N(funcion.subs(x, b))
    except Exception as e:
        print("\n-------------------------------")
        print("\nSe ha producido un error: ",e)
        print("\n-------------------------------")

    archivo.write('\niteracion: {}'.format(count))
    archivo.write('\na={}, b= {}, f(a) = {}, f(b) = {}'.format(a,b,f_a,f_b))

    if (b - a)/2 > tol and count < Max_iteraciones:
        valor_medio = (a+b)/2

        #Calculo del error relativo de acuerdo a las aproximaciones a partir de la segunda iteracion
        if count == 0:
            valor_medio1 = valor_medio
        else:
            error_relativo = calculo_error_relativo(valor_medio1, valor_medio)
            valor_medio1 = valor_medio
            archivo.write("Error relativo: {}".format(error_relativo))
            if error_relativo < 0.0001:
                return (a+b)/2

        archivo.write('\n-----------------------------------------------------------------------------------------')

        #metodo por biseccion
        f_vm = N(funcion.subs(x, valor_medio))
        if f_vm == 0:
            return f_vm
        elif f_a*f_vm < 0:
            return verificacion_valor_imagenes(funcion,a,valor_medio,Max_iteraciones,count+1, valor_medio1)
        else:
            return verificacion_valor_imagenes(funcion,valor_medio,b,Max_iteraciones,count+1, valor_medio1)
    else:
        return (a+b)/2


if __name__ == '__main__':
    #creacion de la ruta donde se guardara el txt con los datos de las iteraciones y de los errores relativos
    name = 'Metodo_biseccion.txt'
    dirc = 'C:/Users/Bjsan/OneDrive/Escritorio/Metodos_numericos/metodo_biseccion'
    dirc_completa = os.path.join(dirc, name)
    archivo = open(dirc_completa, 'w')

    #parametros para el metodo
    funcion = verificacion_funcion_syntaxis()
    a = float(input("Introdusca el valor del extremo a del intervalo: "))
    b = float(input("Introdusca el valor del extremo b del intervalo: "))
    Max_iteraciones = int(input("Ingrese el numero maximo de iteraciones que desea que se realicen: "))

    solucion = verificacion_valor_imagenes(funcion,a,b, Max_iteraciones, 0,0)
    archivo.close()
    print("La solucion es: ", solucion)