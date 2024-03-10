# Punto fijo
# OmeGa2B

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

def iteracion_punto_fijo(funcion,aproximacion_inicial, Iteraciones_maximas,tol,count):
    #calculo de las imagenes
    x = Symbol('x')
    # = funcion.subs(x,a).evalf
    while True:
        try:
            p = N(funcion.subs(x,aproximacion_inicial))
            break
        except Exception as e:
            print("\n-------------------------------")
            print("\nSe ha producido un error: ",e)
            print("\nIntente con otro valor de aproximacion")
            aproximacion_inicial = valor_aproximacion()
            print("\n-------------------------------")

    archivo.write('\n\n-----------------------------------------------------------------------------------------')
    archivo.write("\np0: {}".format(aproximacion_inicial))
    archivo.write("\np: {}".format(p))
    if count < Iteraciones_maximas:
        if abs(p-aproximacion_inicial) < tol:
            return p
        else:
            return iteracion_punto_fijo(funcion,p,Iteraciones_maximas,1e-6,count+1)

    print("\nEl metodo fallo despues de {} iteraciones".format(count))


def valor_aproximacion():
    va = float(input("Ingrese la aproximacion inicial: "))
    return va


if __name__ == '__main__':
    #creacion de la ruta donde se guardara el txt con los datos de las iteraciones y de los errores relativos
    name = 'Punto_fijo.txt'
    dirc = ''#direccion donde se guardara el archivo
    dirc_completa = os.path.join(dirc, name)
    archivo = open(dirc_completa, 'w')

    funcion = verificacion_funcion_syntaxis()
    aproximacion_inicial = valor_aproximacion()
    Iteraciones_maximas = int(input('Ingrese el numero maximo de interacions: '))
    p = iteracion_punto_fijo(funcion,aproximacion_inicial,Iteraciones_maximas,1e-6,0)
    archivo.close()
    print("\nprocedimiento realizado con exito \nsolucion: {}".format(p))