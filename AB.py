from TISE_solver import *

'''=========================================================================='''
'''Defining functions to make A and B dictionaries'''
def a(i,j):
    '''A matrix elements'''
    if i==j:
        return 1 + 2*lam + 1j*k*V(x[i-1],t)/2
    elif abs(i-j) == 1:
        return -lam

def b(i,j):
    '''B matrix elements'''
    if i==j:
        return 1 - 2*lam - 1j*k*V(x[i-1],t)/2
    elif abs(i-j) == 1:
        return lam

def comp_conj(number):
    '''returns the complex conjugate of a number'''
    return number.real-(number.imag)*1j
    
'''=========================================================================='''
'''Storing the A and B matrix for each time step'''
A_val = {}                   #stores the A matrix for each time step
B_val = {}                   #stores the B matrix for each time step
for t in t_val:
    a_val={}
    b_val={}
    for i in range(1,n+1):
        if (i-1)!=0 :
            a_val[(i,i-1)]=a(i,i-1)
            b_val[(i,i-1)]=b(i,i-1)
        a_val[(i,i)]=a(i,i)
        b_val[(i,i)]=b(i,i)
        if (i+1)!=n+1 :
            a_val[(i,i+1)]=a(i,i+1)
            b_val[(i,i+1)]=b(i,i+1)
    A_val[t] = a_val
    B_val[t] = b_val
'''=========================================================================='''
L_val = {}                   #stores the L and U matrix for each time step
U_val = {}
for t in t_val:
    a_val = A_val[t]
    def l(i,j):
        if (i,j) in l_val:
            return l_val[(i,j)]
        else:
            if i==j:
                l_val[(i,j)]=1
                return 1
            elif (j == i-1):
                l_val[(i,j)] = a_val[i,i-1]/u(i-1,i-1)
                return a_val[i,i-1]/u(i-1,i-1)

    def u(i,j):
        if (i,j) in u_val:
            return u_val[(i,j)]
        else:
            if i==j:
                if i==1:
                    u_val[(i,j)] = a_val[1,1]
                    return a_val[1,1]
                else:
                    u_val[i,j] = a_val[i,i]-(l(i,i-1)*u(i-1,i))
                    return a_val[i,i]-(l(i,i-1)*u(i-1,i))
            elif (j==i+1):
                u_val[(i,j)] = a_val[i,j]
                return a_val[i,j]

    l_val={}
    u_val={}

    for i in range(1,n+1):
        l_val[(i,i)]=l(i,i)
        if (i-1)!=0 : l_val[(i,i-1)]=l(i,i-1)
        u_val[(i,i)]=u(i,i)
        if (i+1)!=n+1 : u_val[(i,i+1)]=u(i,i+1)
    L_val[t] = l_val
    U_val[t] = u_val

'''=========================================================================='''
