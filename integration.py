import math as m
import numpy as np
from matplotlib import pyplot as plt
def Riemann_Sums(f,a,b,n,option="m"):
    w=(b-a)/n
    total_h = 0
    for i in range(n):
        if option =="l": i += 0 ; total_h += f(a + w*i)
        elif option == "r": i += 1 ; total_h += f(a + w*i)
        else: i += 0.5 ; total_h += f(a + w*i)
    # graph design code
    x,y = np.linspace(a,b,n),[]
    for i in range(n):y.append(f(a+w*i))
    plt.figure(figsize=(6,4),facecolor="#C0D3D6")
    plt.plot(x,y,color="b",lw="3")
    plt.title("Area Under The Curve ",color="r",family="Times New Roman",size=18)
    plt.xlabel("x",color="b",size=16)
    plt.ylabel("y",color="b",size=16)
    plt.axhline(c="k")
    plt.axvline(c="k")
    plt.fill_between(x,y,color="r")
    y.clear()
    return w * total_h

def Trapezoidal(f,a,b,n):
    w=(b-a)/n
    total_h = f(a)/2 + f(b)/2
    for i in range(1,n):total_h += f(a+i*w)
    # graph design code
    x,y = np.linspace(a,b,n),[]
    for i in range(n):y.append(f(a+w*i))
    plt.figure(figsize=(6,4),facecolor="#C0D3D6")
    plt.plot(x,y,color="b",lw="3")
    plt.title("Area Under The Curve ",color="r",family="Times New Roman",size=18)
    plt.xlabel("x",color="b",size=16)
    plt.ylabel("y",color="b",size=16)
    plt.axhline(c="k")
    plt.axvline(c="k")
    plt.fill_between(x,y,color="r")
    y.clear()
    return total_h*w


def Simpsons_Rule(f,a,b,n):
    w=(b-a)/n
    total_h = f(a) + f(b)
    for i in range(1,n,2): total_h += 4 * f(a+w*i)
    for j in range(2,n-1,2):total_h += 2 * f(a+w*j)
    # graph design code
    x,y = np.linspace(a,b,n),[]
    for i in range(n):y.append(f(a+w*i))
    plt.figure(figsize=(6,4),facecolor="#C0D3D6")
    plt.plot(x,y,color="b",lw="3")
    plt.title("Area Under The Curve ",color="r",family="Times New Roman",size=18)
    plt.xlabel("x",color="b",size=16)
    plt.ylabel("y",color="b",size=16)
    plt.axhline(c="k")
    plt.axvline(c="k")
    plt.fill_between(x,y,color="r")
    y.clear()
    return w*total_h/3
if __name__=="__main__":
    print("Riemann Sums = ",Riemann_Sums(m.cos,0,m.pi,100))
    print("Trapezoidal = ",Trapezoidal(m.cos,0,m.pi,100))
    print("Simpsons Rule = ",Simpsons_Rule(m.cos,0,m.pi,100))
    print("Exact Value = ",m.sin(m.pi)-m.sin(0))
