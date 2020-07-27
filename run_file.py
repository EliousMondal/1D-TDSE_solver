import time
start = time.clock()
import matplotlib.pyplot as plt
from coefficients import *

'''=========================================================================='''
C2_val = np.array([i for i in Coeff2.values()])
print('c(1)2 values are = ',C2_val)
end = time.clock()
print('time taken to run the program is ',end-start,' seconds')
'''=========================================================================='''
##To plot c1(2) vs time period uncomment the following region
plt.figure()
plt.title('omega = %.3f' %omega)
plt.xlabel('$\dfrac{\omega}{2\pi}$t  -------->')
plt.ylabel('${C_1}^2$  -------->')
plt.ylim(0,1.1)
if omega!=0:
	plt.plot([(i*omega)/(2*np.pi) for i in t_val],[i for i in Coeff2.values()])
else:
        C2_val = np.array([i for i in Coeff2.values()])
        plt.plot(t_val,C2_val)
plt.show()
'''=========================================================================='''
