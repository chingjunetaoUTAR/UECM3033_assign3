"""
Ching June Tao
1202462
Assignment 3 Task 2
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def biological_system(y, t, a, b):
    y0, y1 = y
    dydt = [a*(y0-y0*y1), b*(-y1+y0*y1)]
    return dydt
    
a = 1.0
b = 0.2
# y_initial = [y0_initial, y1_initial]
y_initial = [0.1, 1.0]

t = np.linspace(0,5,150)
sol = odeint(biological_system,y_initial,t,args=(a, b))

#Graph of y0 and y1 against t
plt.plot(t, sol[:, 0], 'b', label='y0(t)')
plt.plot(t, sol[:, 1], 'g', label='y1(t)')
plt.title('Graph of y0 and y1 against t with y0(0)=0.1')
plt.legend(loc='best')
plt.xlabel('t')
plt.ylabel('y')
plt.grid()
plt.savefig('Graph of y0 and y1 against t with y0(0)=01.jpg')
plt.show()


# plotting the graph for y1 against y0
plt.plot(sol[:, 0],sol[:,1], 'b')
plt.title('Graph of y1 against y0 with y0(0) = 0.1')
plt.xlabel('y0')
plt.ylabel('y1')
plt.grid()
plt.savefig('Graph of y1 against y0 with y0(0) = 01.jpg')
plt.show()


##########################################
# when y0(0) = 0.11

y_initial = [0.11, 1.0]
sol2 = odeint(biological_system,y_initial,t,args=(a, b))

#Graph of y0 and y1 against t
plt.plot(t, sol2[:, 0], 'b', label='y0(t)')
plt.plot(t, sol2[:, 1], 'r', label='y1(t)')
plt.title('Graph of y0 and y1 against t with y0(0)=0.11')
plt.legend(loc='best')
plt.xlabel('t')
plt.ylabel('y')
plt.grid()
plt.savefig('Graph of y0 and y1 against t with y0(0)=011.jpg')
plt.show()


# plotting the graph for y1 against y0
plt.plot(sol2[:, 0],sol2[:,1], 'r')
plt.title('Graph of y1 against y0 with y0(0) = 0.11')
plt.xlabel('y0')
plt.ylabel('y1')
plt.grid()
plt.savefig('Graph of y1 against y0 with y0(0) = 011.jpg')
plt.show()

