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
    p0 = float(input("Ingrese un valor para la aproximacion inicial p0: "))
    p1 = float(input("Ingrese un valor para la paroximacion inicial p1: "))
    return p0,p1

def metodo_secante(funcion,p0,p1,Iteraciones_maximas,i,count,tol):
    x = Symbol('x')
    # = funcion.subs(x,a).evalf
    while True:
        try:
            #p = p0 -f(p0)/f'(p0)
            q0 = N(funcion.subs(x,p0))
            q1 = N(funcion.subs(x,p1))
            break
        except Exception as e:
            print("\n-------------------------------")
            print("\nSe ha producido un error: ",e)
            print("\nIntente con otro valor de aproximacion")
            p0,p1 = valor_aproximacion()
            print("\n-------------------------------")

    while True:
        count = count + 1
        try:
            if i <= Iteraciones_maximas:
                p= p1-((q1*(p1-p0))/(q1-q0))
                archivo.write('\n\n-----------------------------------------------------------------------------------------')
                archivo.write("\niteracion {}".format(count))
                archivo.write("\np0: {}, p1: {}".format(p0, p1))
                archivo.write("\np: {}".format(p))

                archivo.write(f"\n error absoluto: {abs(p-p1)}")
                if abs(p-p1) < tol:
                    return p
                else:
                    i = i + 1
                    p0 = p1
                    q0 = q1
                    p1 = p
                    q1 = N(funcion.subs(x,p))
            else:
                print(f"El metodo fallo despues de {Iteraciones_maximas}")
                return False
        except Exception as e:
            print(f"\nOcurrio un problema: {e}")
            return False


if __name__ == '__main__':
    name = 'Metodo_secante.txt'
    dirc = ''
    dirc_completa = os.path.join(dirc, name)
    archivo = open(dirc_completa, 'w')

    funcion = verificacion_funcion_syntaxis()
    p0,p1 = valor_aproximacion()
    Iteraciones_maximas = int(input('Ingrese el numero maximo de iteraciones: '))
    p = metodo_secante(funcion,p0,p1,Iteraciones_maximas,i = 2,count =0,tol = 1e-6)
    if (p != False):
        archivo.write(f"\n\n\nprocedimiento realizado con exito, solucion: {p}".format(p))
    archivo.close()