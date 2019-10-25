import string
import os.path
import sys
import numpy as np
import math
import os
from numpy import*

n0=0 #initial count
nE=4 #total number (later make it ask user)

while (n0 < nE):
  s(n0) = loadtxt("scan"(n0)".txt")  #how to use n0 to make names?
  y(n0) = s(n0)[:,1]
  n0 += 1

bk = loadtxt("bkg.txt")
yb = bk[:,1]

qtz = loadtxt("../../qtz_avg.txt")

total=4
length=s1.shape[1]

#x_corr=(1/((((1/x1)-(1/800))^-1))*10^-9)/100
y1f=(y1-yb)/qtz #n
y2f=(y2-yb)/qtz #n
y3f=(y3-yb)/qtz #n
y4f=(y4-yb)/qtz #n

avg=(y1+y2+y3+y4)/total
bk_sub=avg-yb
qtz_div=bk_sub/qtz

np.savetxt('Average.txt', qtz_div)
np.savetxt('Scan1_Norm.txt', y1f) 
np.savetxt('Scan2_Norm.txt', y2f) 
np.savetxt('Scan3_Norm.txt', y3f) 
np.savetxt('Scan4_Norm.txt', y4f) 
