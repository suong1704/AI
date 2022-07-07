import numpy as np
import math
def daoham(x):
   y = 2 * (2*math.e**x -2/(math.e**x)) * (2*math.e**x + 2*x/(math.e**x))
   return y
def ham(x):
   return (2*math.e**x -2/(math.e**x))**2
loop=1000
x=0
alpha=0.1
gra =0.001
for i in range(loop):
   x_new= x
   x= x-alpha*daoham(x_new)
   if abs(daoham(x_new)) < gra:
      break
print("Ham so dat gia tri nho nhat tai %f" % x)
print("Gia tri nho nhat cua ham so: %f" %ham(x))