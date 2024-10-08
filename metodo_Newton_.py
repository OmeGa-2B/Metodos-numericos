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
    archivo.write('\n\n-----------------------------------------------------------------------------------------')
    archivo.write(f"\nIteracion {count}")
    while True:
        try:
            #p = p0 -f(p0)/f'(p0)
            f_p = N(funcion.subs(x,aproximacion))
            archivo.write(f"\n funcion evaluada en p0: {f_p}")
            df = diff(funcion,x)
            archivo.write(f"\nfuncion derivada: {df}")
            df_p = N(df.subs(x,aproximacion))
            archivo.write(f"     funcion derivada evaluada: {df_p}")
            p = aproximacion-(f_p/df_p)
            break
        except Exception as e:
            print("\n-------------------------------")
            print("\nSe ha producido un error: ",e)
            print("\nIntente con otro valor de aproximacion")
            aproximacion = valor_aproximacion()
            print("\n-------------------------------")

    archivo.write("\np0: {}".format(aproximacion))
    archivo.write("   p: {}".format(p))
    archivo.write(f"\n error absoluto {p-aproximacion}")

    if count < iteraciones_maximas:
        if abs(p-aproximacion) < tol:
            return p
        else:
            return metodo_newton(funcion,p,iteraciones_maximas,count+1,1e-6)
    else:
        print("\nEl metodo fallo despues de {} iteraciones".format(count))
        return False

if __name__ == '__main__':
    name = 'Metodo_Newton.txt'
    dirc = ''
    dirc_completa = os.path.join(dirc, name)
    archivo = open(dirc_completa, 'w')

    funcion = verificacion_funcion_syntaxis()
    aproximacion_inicial = valor_aproximacion()
    Iteraciones_maximas = int(input('Ingrese el umero maximo de iteraciones: '))
    p = metodo_newton(funcion,aproximacion_inicial,Iteraciones_maximas,0,tol = 1e-6)
    archivo.close()
    if p != False:
        print("\nprocedimiento realizado con exito \nsolucion: {}".format(p))