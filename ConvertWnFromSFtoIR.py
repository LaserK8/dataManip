import string
import os.path
import sys
import numpy as np
import math

s1 = loadtxt("Scan1.txt") #import data from text file
x1 = s1[:,0] #select first column as x

vis=798.47 #set visible wavelength



wn=(((((1/x1)-(1/vis))**(-1))*(10**(-7)))**(-1)) #convert SF frequency (x) to IR using fixed (vis) freq

np.savetxt('WNCorrected798_47.txt', wn) #save as a new text file
