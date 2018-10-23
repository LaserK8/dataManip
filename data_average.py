import string
import os.path
import sys
import numpy as np
import math

import string
import os
import sys
from numpy import*
import math

s1 = loadtxt("scan1.txt")
y1 = s1[:,1]
#x1 = s1[:,0]

s2 = loadtxt("scan2.txt")
y2 = s2[:,1]

s3 = loadtxt("scan3.txt")
y3 = s3[:,1]

s4 = loadtxt("scan4.txt")
y4 = s4[:,1]

bk = loadtxt("bkg.txt")
yb = bk[:,1]

qtz = loadtxt("../../qtz_avg.txt")
#yq = qtz[:,0]
total=4
length=s1.shape[1]
#array=np.zeros(shape=(length,2))
#x_corr=np.xeros(shape=(length,1))

#x_corr=(1/((((1/x1)-(1/800))^-1))*10^-9)/100
y1f=(y1-yb)/qtz #n
y2f=(y2-yb)/qtz #n
y3f=(y3-yb)/qtz #n
y4f=(y4-yb)/qtz #n
#avg_a=(y1f+y2f+y3f+y4f)/total #n

avg=(y1+y2+y3+y4)/total
bk_sub=avg-yb
qtz_div=bk_sub/qtz

np.savetxt('Average.txt', qtz_div)
#np.savetxt('AverageIndiv.txt', avg_a) #n
np.savetxt('Scan1_Norm.txt', y1f) #n
np.savetxt('Scan2_Norm.txt', y2f) #n
np.savetxt('Scan3_Norm.txt', y3f) #n
np.savetxt('Scan4_Norm.txt', y4f) #n
#np.savetxt('fourteen.dat', dataI_avg)
#np.savetxt('thirteenNorm.dat', [dataR_avg[:,0],dataR_norm])
#np.savetxt('fourteenNorm.dat',[dataI_avg[:,0],dataI_norm])
