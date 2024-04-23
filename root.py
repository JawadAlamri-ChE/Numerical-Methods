
def bisection(f,a,b,tol=1e-6):
    if abs(f(a))<tol:
        return a
    elif abs(f(b))<tol:
        return b
    elif f(a)*f(b)>0:
        return "No root in given interval"
    m = (a + b)/2
    while abs(f(m))>=tol:
        if f(a)*f(m)<0: b=m
        else: a=m
        m=(a+b)/2
    return m

def false_position(f,a,b,tol=1e-6):
    if abs(f(a))<tol:
        return a
    elif abs(f(b))<tol:
        return b
    elif f(a)*f(b)>0:
        return 
    m = (f(b)*a-f(a)*b)/(f(b)-f(a))
    while abs(f(m))>=tol:
        if f(a)*f(m)<0: b=m
        else: a=m
        m=(f(b)*a-f(a)*b)/(f(b)-f(a))
    return m

def Newton_Raphson(f,f_prime,xi,tol=1e-6):
    m=xi-f(xi)/f_prime(xi)
    while abs(f(m))>tol:
        xi=m
        m=xi-f(xi)/f_prime(xi)
    return m

def secant(f,xi,h,tol=1e-6):
    m=xi-f(xi)*h/(f(xi+h)-f(xi))
    while abs(f(m))>tol:
        xi=m
        m=xi-f(xi)*h/(f(xi+h)-f(xi))
    return m

# test code
if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    from tabulate import tabulate as tab
    #graph code
    fx = lambda x: (3*np.sin(x)+9)-(x**2 - np.cos(x))
    x = np.linspace(-5,5,1000)
    y = fx(x)
    x_roots = []
    y_roots = []
    for i in x: x_roots.append(secant(fx,i,0.001));y_roots.append(i*0)
    plt.figure(figsize=(6,4),facecolor="#C0D3D6")
    plt.axes(facecolor="#E7EBED")
    plt.plot(x,y,color="b",lw="2",label="f(x)")
    plt.scatter(x_roots,y_roots,color="r",label="roots")
    plt.title("x & y diagrame ",color="r",family="Times New Roman",size=18,weight="bold")
    plt.xlabel("x",color="b",size=16)
    plt.ylabel("y",color="b",size=16)
    plt.axhline(c="k")
    plt.axvline(c="k")
    plt.grid(color="#52625F")
    plt.legend(loc="upper right")
    plt.show()
    # roots code
    fx_prime = lambda x: -2*x - np.sin(x) + 3*np.cos(x)
    bisection_m = bisection(fx,2,3)
    false_position_m = false_position(fx,2,3)
    Newton_Raphson_m = Newton_Raphson(fx,fx_prime,5)
    secant_m = secant(fx,4,0.001)
    function = ["Function", "    f(x)", "(3sin(x)+9)−(x^2−cos(x))", "Interval", "  (-5,5)"]
    methods_roots = [(" Method", " Bisection ", " False_position ", " Newton_Raphson ", " Secant "),
                     (" Root", bisection_m, false_position_m, Newton_Raphson_m, secant_m)]
    print(tab(methods_roots, headers=function, tablefmt="fancy_grid"))

    
    
    