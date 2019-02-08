import math
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

pi = 3.14

def dxdt(x,t):
    # print(x[2])
    pc = np.array([2, 5])
    teta_cell = math.atan(pc[1] / pc[0])
    v = 0.1
    kp =8

    w = 0
    # print('x0',x[0])
    # print('x1',x[1])
    if  t>2 and teta_cell != x[2]:
        teta_err = teta_cell - x[2]
        w = kp * teta_err

    if (x[0] > pc[0] and x[1] > pc[1]):
        fx1 = 2
        fx2 = 5
    else:
        fx1 = v * math.cos(x[2])
        fx2 = v * math.sin(x[2])

    fteta1 = w
    # print(type(fx1))
    # y = np.array([fx1, fx2, fteta1])
    y=[fx1,fx2,fteta1]
    print(y)
    return y





x0=np.array([0,0,-np.pi/2])# начальное значение

t = np.linspace(0,55) # вектор моментов времени

y = odeint(dxdt, x0,t) # решение уравнения

print(y)
X=y[:,0]
X=X[:, None]
Y=y[:,1]
Y=Y[:, None]
Z=y[:,2]
# print('X',X)
# print('Y',Y)
#y = np.array(y).flatten() # преобразование массива
plt.plot(X,Y)
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()


#print(x0[2])






