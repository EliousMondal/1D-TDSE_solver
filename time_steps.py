import numpy as np

'''=========================================================================='''
class time_steps(object):
    def __init__(self,ntp,k,omega):
        self.ntp = ntp
        self.k = k
        self.omega = omega

    def t_val(self):
        ntp = self.ntp
        k = self.k
        omega = self.omega
        try:
                t_scale = ntp*2*np.pi/omega
        except ZeroDivisionError:
                t_scale = ntp*2*np.pi
        t_val = []       #storing the time values for each time step
        ts = 0
        count = 0
        while ts<(t_scale):
            t_val.append(ts)
            ts = ts + k
            count = count + 1
        return t_val
'''=========================================================================='''
