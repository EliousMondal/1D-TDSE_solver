from AB import *

'''=========================================================================='''
'''Generation of Psi(x,t)'''
Psi_0 = Psi_gs[t_val[0]]
PSI_t = {}                   #stores the Psi at each time
PSI_t[t_val[0]] = Psi_0      #set the initial Psi here
Psi = PSI_t[t_val[0]]
for t in range(1,len(t_val)):
    print('Psi(at t = %f) generated' %t)
    bv = []
    b_val = B_val[t_val[t-1]]
    l_val = L_val[t_val[t]]
    u_val = U_val[t_val[t]]
    for i in range(1,len(Psi)+1):
        if (i-1)!=0: x1 = b_val[(i,i-1)]*Psi[i-2]
        else: x1 = 0
        x2 = b_val[(i,i)]*Psi[i-1]
        if i!=len(Psi) : x3 = b_val[(i,i+1)]*Psi[i]
        else: x3 = 0
        bv.append(x1+x2+x3)
    z_val = {}
    z_val[1] = bv[0]
    for i in range(2,len(bv)+1):
        z_val[i] = bv[i-1]-(z_val[i-1]*l_val[(i,i-1)])
    x_val = {}
    x_val[n] = z_val[n-1]/u_val[(n-1,n-1)]
    for i in range(n-1,0,-1):
        x_val[i] = (z_val[i]-(u_val[(i,i+1)]*x_val[i+1]))/u_val[(i,i)]
    nindx=sorted(x_val.keys())
    
    npsi = []
    for i in nindx:
        npsi.append(x_val[i])
    PSI_t[t_val[t]] = npsi
    Psi = npsi
'''=========================================================================='''
