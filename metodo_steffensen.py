from sympy import *
import os

def verificacion_funcion_syntaxis():
    while True:
        try:
            ecuacion = input("\nIngrese la ecuacion con la cual se va a trabajar: ")
            #parse_expr
            return sympify(ecuacion)

        except Exception as e:
            print("\n-------------------------------")
            print("\nSe ha producido un error: ",e)
            print("\nPor favor intentelo de nuevo")
            print("\n-------------------------------")

def valor_aproximacion():
    va = float(input("Ingrese la aproximacion inicial: "))
    return va

def evaluacion_funcion(funcion, aproximacion):
    x = Symbol('x')
    while True:
        try:
            f_p = N(funcion.subs(x,aproximacion))
            return f_p
        except Exception as e:
            print("\n-------------------------------")
            print("\nSe ha producido un error: ",e)
            print("\nIntente con otro valor de aproximacion")
            aproximacion = valor_aproximacion()
            print("\n-------------------------------")

def metodo_steffensen(funcion,aproximacion,Iteraciones_maximas,count,tol):
    archivo.write('\n\n-----------------------------------------------------------------------------------------')
    archivo.write(f"\n\n iteracion: {count}  \n aproximacion(p0): {aproximacion}")
    try: 
        if count < Iteraciones_maximas:
            p1 = evaluacion_funcion(funcion, aproximacion)
            p2 = evaluacion_funcion(funcion, p1)
            p = aproximacion-pow(p1-aproximacion,2)/(p2-(2*p1)+aproximacion)
            archivo.write(f"  p1: {p1}   p2: {p2}    p: {p}")
            archivo.write(f"\nError absoluto: {abs(p-aproximacion)}")
            if abs(p-aproximacion) < tol:
                return p
            else:
                return metodo_steffensen(funcion,p,Iteraciones_maximas,count+1,tol)
        else:
            archivo.write(f"\n\n EL metodo fallo con {count} iteraciones")
            return False
    except Exception as e:
        print(f"\nOcurrio un error de tipo : {e}")
        return False

if __name__ == '__main__':
    name = 'Metodo_Steffense.txt'
    dirc = ''
    dirc_completa = os.path.join(dirc, name)
    archivo = open(dirc_completa, 'w')

    funcion = verificacion_funcion_syntaxis()
    aproximacion_inicial = valor_aproximacion()
    Iteraciones_maximas = int(input('Ingrese el umero maximo de iteraciones: '))
    p = metodo_steffensen(funcion,aproximacion_inicial,Iteraciones_maximas,0,tol = 1e-6)
    if p != False:
        archivo.write("\n\n\nprocedimiento realizado con exito, solucion: {}".format(p))
    archivo.close()