import os
import numpy as np
from numpy import *
from matplotlib import *
from matplotlib.pyplot import *
from matplotlib.backends.backend_pdf import PdfFile, PdfPages, FigureCanvasPdf
import sys
import math

# set up data
N = 4

eps = 1e-14
data_relax = array([[11.,eps,eps],[59.8,52.4,eps],[331.,315.,223.],[1606.,1692.,1247.]])
data_fixed = array([[44.5,0.,0.],[236.,177.,0],[1261,1375,848],[9982,15980,9629]])

speedup = data_fixed / data_relax

print speedup

ind = arange(N)
width = 0.3

# set up plot
font = {'family':'serif','size':10}
fig = Figure(figsize=(4,3), dpi=80)
ax = fig.add_subplot(111)

# plot log-log
bar1 = ax.bar(ind, speedup[:,0], width, color='r')
bar2 = ax.bar(ind+width, speedup[:,1],width,color='b')
bar3 = ax.bar(ind+2*width,speedup[:,2],width,color='g')
# bar2 = ax.bar(ind+width, speedup_2nd, width, color='b')
rc('font',**font)

# axis labels
ax.set_ylabel('Speedup', fontsize=10)
ax.set_xlabel('N', fontsize=10)
ax.set_xticks(ind+1.5*width)
ax.set_xticklabels( ('2048','8192','32768','131072') )
ax.legend( (bar1[0], bar2[0], bar3[0]), ('2048 panels/cell', '8192 panels/cell', '32768 panels/cell'), loc=2 )
fig.subplots_adjust(left=0.185, bottom=0.21, right=0.965, top=0.95)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('EthrocyteMultipleCellSpeedup.pdf',dpi=80)
