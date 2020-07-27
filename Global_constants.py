'''Global constants and arrays'''
from time_steps import *

'''=========================================================================='''
'''Some Global Constants for the code'''
h = 0.01                                              #step size in x coordinate
k = 0.1                                               #step size in t coordinate
x_range = (-4,4)
n = int((x_range[1]- x_range[0])/h)+1                           #no. of x points
lam = (1j*k)/(4*(h**2))                        #lambda value of L and U matrices
omega = float(input('Enter the value of omega : '))

x = np.linspace(x_range[0],x_range[1],n)
y = np.zeros(n)
z = 0.000001                                     #initial slope to calculate Psi
y[1] = z*h

'''=========================================================================='''
ntp = 1
tsteps = time_steps(ntp,k,omega)
t_val = tsteps.t_val()
print('number of time steps = ',len(t_val))
'''=========================================================================='''
