import numpy as np 
a = np.arange(10)
a=np.where(a < 10/2, a, a-20).copy()
a= np.where(a > 2, a, a*1.33)

L=4
xNext =np.arange(10)-4
print(xNext)

xNext=np.where(xNext > -L/2, 0,xNext)
print (xNext)
#xNext=np.where(xNext > L/2, xNext, L-xNext)

matrix0= np.array([[0,1][2,3]])
print(matrix0)
matrix0.resize((3,3))