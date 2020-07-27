from PSI_generation import *

'''=========================================================================='''
Coeff = {}                  #saves coefficients(c) for each time step
def C(Psi,yn):
    '''returns the coefficient cn of Psi in yn'''
    ip = 0
    for i in range(len(Psi)):
        ip = ip + Psi[i]*yn[i]*h
    return ip
for i in t_val:
    Coeff[i] = C(Psi_gs[i],PSI_t[i])

'''=========================================================================='''
Coeff2 = {}                 #saves cc* for each time step
for i in t_val:
    cn2 = (Coeff[i]*comp_conj(Coeff[i])).real
    Coeff2[i] = cn2
    
'''=========================================================================='''
