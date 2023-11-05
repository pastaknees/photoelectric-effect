#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 18:16:02 2023

@author: nicoleevans
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

lam, V_stop, u_V_stop, band = np.loadtxt('/Users/nicoleevans/phy224/photoelectric effect experiment 1.csv', delimiter=',',unpack=True)

def V_stop_freq(f,h, E_0)->float:
    return (1/(1.6e-19))*((h*f)-E_0)

f = (3*10e8)/lam

u_f = f*(band/lam)

popt, pcov=curve_fit(V_stop_freq, f, V_stop, sigma=u_V_stop)
h=popt[0]
E_0=popt[1]
u_h=np.sqrt(np.diag(pcov))[0]
u_E_0=np.sqrt(np.diag(pcov))[1]

print('The value of h is',h,'J*s +-',u_h,'J*s.')
print('The value of E_0 is',E_0,'J +-',u_E_0,'J.')

plt.ylabel('$V_{stop} \\ (V)$')
plt.xlabel('$f\ (Hz)$')
plt.ylim(0,1.5)
plt.title('Experiment 1: Stopping Voltage versus Frequency')
plt.grid(visible=True, which='both', axis='both')
plt.errorbar(f,V_stop, xerr=u_V_stop, marker='|', capsize=4, ecolor='black',fmt = 'none', mfc='black', mec='black', ms=5, mew=2, label='Measurement Uncertainty')
plt.plot(f, V_stop_freq(f,h,E_0), color='red', linestyle='solid',label='$CurveFit$')
plt.plot(f, V_stop, color='blue', linestyle='none',marker='o', markersize=5, markerfacecolor="blue", label='Measured stopping voltage')
plt.legend(loc='upper left', frameon=True)
plt.savefig('Experiment 1 plot.png')