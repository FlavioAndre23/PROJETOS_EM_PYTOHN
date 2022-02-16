#Metodo de Newton

from math import pow, sin, cos, exp
def f(x):
    #return exp(-x)+x**2-2
    #return pow(x,2)/4-sin(x)
     return 4*cos(x)-exp(2*x)
def Dfx(x):
    #return x/2-cos(x)
    #return exp(-x) + x ** 2 - 2
    return -4*sin(x)-2*exp(2*x)

def Dfx(x):
    h =0.0001
    return (f(x+h)-f(x))/h

def Newton(x0,tol):
    erro = tol+1
    while erro > tol:
        x = x0 - f(x0)/Dfx(x0)
        erro = abs(f(x))/abs(x)
        #erro = abs(x - x0)/abs(x)
        x0 = x
        print(f'x_k = {x0:.6f}\tx_k+1 = {x:.6f}\tf(x_k) = {Dfx(x0):.6f}\terro ={erro:.6f}')
    return x
x0 = float(input('Estimativa Inicial: '))
tol = float(input('Tolerancia: '))
print(Newton(x0,tol))

