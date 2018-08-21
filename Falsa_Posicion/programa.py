import numpy as np

def f(V):
    P = 10.0
    a = 3.599
    b = 0.04267
    R = 0.08205
    T = 353.2
    value = (P+a/V**2)*(V-b)-R*T
    return value

# Inputs
#p_prev_2 = 0.5
#p_prev_1 = 30.0
p0=0.5
p1=30.0
Tol = 1e-4
error = 1.0
Nmax = 1000
iteracion = 0

q0=f(p0)
q1=f(p1)
while(error>Tol):
    p = p1-q1*(p1-p0)/(q1-q0)
    error = abs(p-p1)
    q=f(p)
    if(q*q1<0):
        p0=p1
        q0=q1
    p1=p
    q1=q
    print("p_n = %.6f\t error = %.5f\t abs(f(p_n)) = %.5f\t pn-1=%.5f\t pn-2=%.5f "%(p,error,abs(f(p)),p,p1))
    iteracion=iteracion+1
    if(iteracion>=Nmax):
        print("El metodo no converge despues de %d iteraciones"%Nmax)
        break
