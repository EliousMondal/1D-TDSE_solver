from potential import *

'''=========================================================================='''
'''defining the function to carry out Numerov method'''
def Numerov(x,y1,y2,E):
    '''returns y[i+1] value'''
    u = 1 - (1/6.)*(h**2)*(V(x,t)-E)
    return ((12-10*u)*y1-u*y2)/u

'''=========================================================================='''
'''defining a function to carry out Numerov for a given E'''
def Psi(E):
    for i in range(2,n):
        y[i] = Numerov(x[i],y[i-1],y[i-2],E)
    N_const = 0                 #Inverse of square of Normalisation constant
    for j in y:
        N_const = N_const + j*j*h
    A1 = 1.0/np.sqrt(N_const)
    m = A1*y
    return(m[-1],m)

'''=========================================================================='''
'''finding the eigenvalues'''
def Eigen():
    Eigenvalues = []
    a = np.linspace(min(V(x,t)),1,20)
    P = np.array([Psi(i)[0] for i in a])
    for i in range(len(P)-1):
        if (P[i]<0 and P[i+1]>0) or (P[i]>0 and P[i+1]<0):
            low = a[i]
            high = a[i+1]
            mid = (low + high)/2.
            while abs(Psi(mid)[0]) > h:
                mid = (low + high)/2.
                if P[i] < 0:
                    if Psi(mid)[0] < 0:
                        low = mid
                    else:
                        high = mid
                elif P[i] > 0:
                    if Psi(mid)[0] > 0:
                        low = mid
                    else:
                        high = mid
            Eigenvalues.append(mid)
    return Eigenvalues

'''=========================================================================='''
'''Storing the instantaneous ground state at each time step'''
Psi_gs = {}
for t in t_val:
    Eigenvalue = Eigen()[0] 
    Psi_gs[t] = Psi(Eigenvalue)[1]
    print('Psi_ground_state at t = ',t,' generated with eigenvalue = ',Eigenvalue)
print('All Psi_gs generated')

'''=========================================================================='''
