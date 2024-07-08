import os
import cmath
from sympy import *

def verificacion_funcion_syntaxis():
    while True:
        try:
            ecuacion = input("\nIngrese la ecuacion con la cual se va a trabajar: ")
            return sympify(ecuacion)

        except SympifyError as e:
            print("\n-------------------------------")
            print("\nSe ha producido un error: ", e)
            print("\nPor favor intentelo de nuevo")
            print("\n-------------------------------")

def valor_aproximacion():
    try:
        p0_real, p0_imag = map(float, input("Ingrese la parte real e imaginaria de la aproximacion p0 separadas por espacio: ").split())
        p1_real, p1_imag = map(float, input("Ingrese la parte real e imaginaria de la aproximacion p1 separadas por espacio: ").split())
        p2_real, p2_imag = map(float, input("Ingrese la parte real e imaginaria de la aproximacion p2 separadas por espacio: ").split())
        return complex(p0_real, p0_imag), complex(p1_real, p1_imag), complex(p2_real, p2_imag)
    except ValueError:
        print("\n-------------------------------")
        print("\nValor de aproximación inválido. Intente de nuevo.")
        print("\n-------------------------------")
        return valor_aproximacion()

def evaluacion_funcion(funcion, aproximacion):
    x = Symbol('x')
    try:
        f_p = N(funcion.subs(x, aproximacion))
        return f_p
    except Exception as e:
        print("\n-------------------------------")
        print("\nSe ha producido un error: ", e)
        print("\nIntente con otro valor de aproximacion")
        aproximacion = valor_aproximacion()
        print("\n-------------------------------")
        return evaluacion_funcion(funcion, aproximacion)

def determinar_valores(p0,p1,p2,funcion):
    h1 = p1 - p0
    h2 = p2 - p1
    e1 = (evaluacion_funcion(funcion,p1)-evaluacion_funcion(funcion,p0))/h1
    e2 = (evaluacion_funcion(funcion,p2)-evaluacion_funcion(funcion,p1))/h2
    d = (e1-e2)/(h2+h1)
    return h1,h2,e1,e2,d

def metodo_muller(funcion,p0,p1,p2,Iteraciones_maximas,count,tol):
    archivo = open('Metodo_muller.txt', 'w')
    h1,h2,e1,e2,d = determinar_valores(p0,p1,p2,funcion)

    while count < Iteraciones_maximas:
        archivo.write("\n--------------------------------------------------------------------------------------------")
        archivo.write(f"\niteracion {count} \n\n p0: {p0}   p1: {p1}    p2: {p2} \n h1: {h1}  h2: {h2}    e1: {e1}    e2: {e2}    d: {d}")
        b = e2+(h2*d)
        D = cmath.sqrt(pow(b,2)-(4*evaluacion_funcion(funcion,p2)*d))

        if abs(b-D) < abs(b+D):
            E = b + D
        else:
            E = b - D

        h = (-2*evaluacion_funcion(funcion,p2))/E
        p = p2+h
        archivo.write(f"\n h: {h}   p: {p}")

        if abs(h) < tol:
            archivo.write("\n\n\nprocedimiento realizado con éxito, solución: {}".format(p))
            archivo.close()
            return p
        else:
            p0 = p1
            p1 = p2
            p2 = p
            h1,h2,e1,e2,d = determinar_valores(p0,p1,p2,funcion)
            count += 1

    archivo.write(f"\nEl metodo fallo despues de {count} iteraciones")
    archivo.close()
    return False

if __name__ == '__main__':
    name = 'Metodo_muller.txt'
    dirc = ''
    dirc_completa = os.path.join(dirc, name)
    archivo = open(dirc_completa, 'w')

    funcion = verificacion_funcion_syntaxis()
    p0,p1,p2 = valor_aproximacion()
    Iteraciones_maximas = int(input('Ingrese el numero máximo de iteraciones: '))
    p = metodo_muller(funcion,p0,p1,p2,Iteraciones_maximas,1,tol=1e-12)
    if not p:
        print("\nEl método de Muller no pudo encontrar una solución dentro del límite de iteraciones.")
