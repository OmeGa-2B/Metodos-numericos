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

def metodo_newton(funcion, aproximacion, iteraciones_maximas,count,tol):
    x = Symbol('x')
    # = funcion.subs(x,a).evalf
    while True:
        try:
            #p = p0 -f(p0)/f'(p0)
            f_p = N(funcion.subs(x,aproximacion))
            df = diff(funcion,x)
            df_p = N(df.subs(x,aproximacion))
            p = aproximacion-f_p/df_p
            break
        except Exception as e:
            print("\n-------------------------------")
            print("\nSe ha producido un error: ",e)
            print("\nIntente con otro valor de aproximacion")
            aproximacion = valor_aproximacion()
            print("\n-------------------------------")

    archivo.write('\n\n-----------------------------------------------------------------------------------------')
    archivo.write("\np0: {}".format(aproximacion))
    archivo.write("\np: {}".format(p))

    if count < iteraciones_maximas:
        if abs(p-aproximacion) < tol:
            return p
        else:
            return metodo_newton(funcion,p,iteraciones_maximas,count+1,1e-6)

    print("\nEl metodo fallo despues de {} iteraciones".format(count))
    return 0

if __name__ == '__main__':
    name = 'Metodo_Newton.txt'
    dirc = 'direccion del archivo'
    dirc_completa = os.path.join(dirc, name)
    archivo = open(dirc_completa, 'w')

    funcion = verificacion_funcion_syntaxis()
    aproximacion_inicial = valor_aproximacion()
    Iteraciones_maximas = int(input('Ingrese el umero maximo de iteraciones: '))
    p = metodo_newton(funcion,aproximacion_inicial,Iteraciones_maximas,0,tol = 1e-6)
    archivo.close()
    print("\nprocedimiento realizado con exito \nsolucion: {}".format(p))