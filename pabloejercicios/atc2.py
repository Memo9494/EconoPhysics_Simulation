from random import uniform
import numpy as np
from scipy.special.orthogonal import p_roots
 
def func(x):
   return x*np.sin(x)**2
 
#montecarlo method
def montecarlo(N,xmin,xmax,ymin,ymax, func):
   contadorint=0
   for i in range(N):
       pointx=uniform(xmin,xmax)
       pointy=uniform(ymin,ymax)
       if pointy>=func(pointx):
           contadorint+=1
   coefficiente=contadorint/N
   areatotal=coefficiente*(xmax-xmin)*(ymax-ymin)
   return areatotal
  
#Gaussian method
def gaussian(a,b,func,n):
   [x,C]=p_roots(n+1)
   res=sum(C*func(x_m(x,b,a)))
   return res
  
#a method that transforms x into the range of gaussian quadrature
def x_m(x,b,a):
   x_m=1/2*(b-a)*x+1/2(b+a)
   x_mdx=1/2*(b-a)
   return x_m*x_mdx
  
print("valor = " + str(montecarlo(100,0,PI,0,2, func)))
print("valor = " + str(montecarlo(1000,0,PI,0,2, func)))
print("valor = " + str(montecarlo(5000,0,PI,0,2, func)))
print("valor = " + str(montecarlo(10000,0,PI,0,2, func)))
print("valor = " + str(montecarlo(50000,0,PI,0,2, func)))
print("valor = " + str(montecarlo(100000,0,PI,0,2, func)))
print("valor = " + str(montecarlo(5000000,0,PI,0,2, func)))
print("valor = " + str(montecarlo(10000000,0,PI,0,2, func)))
 
print("valor = " + str(gaussian(0,PI,func,2)))
print("valor = " + str(gaussian(0,PI,func,3)))
print("valor = " + str(gaussian(0,PI,func,4)))