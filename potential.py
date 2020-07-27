from Global_constants import *

'''=========================================================================='''
'''Defining the time dependent potential'''
dist = 2                #a value for the potential
epsilon = 1             #epsilon value for the potential
gamma = 0.025           #gamma value for the potential

def V(x,t):
    '''takes in the x coordinate and time
       returns the time dependent potential'''
    b = -((2*epsilon)/dist**2)*(x**2)+(epsilon/(dist**4))*(x**4) + gamma*np.cos(omega*t)*(x**3)
    return b

'''=========================================================================='''
