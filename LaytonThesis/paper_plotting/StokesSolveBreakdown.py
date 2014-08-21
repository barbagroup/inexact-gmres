import os
import numpy as np
from numpy import *
from matplotlib import *
from matplotlib.pyplot import *
from matplotlib.backends.backend_pdf import PdfFile, PdfPages, FigureCanvasPdf
import sys
import math

# set up data
p2p = array([0.1977, 0.2002, 0.197, 0.1977, 0.1978, 0.1978, 0.1978, 0.1978,
    0.1978, 0.1981, 0.2011, 0.1984, 0.1985, 0.1987, 0.1986, 0.1989,
    0.1988, 0.1985, 0.1988, 0.1983, 0.1985, 0.1985, 0.1986, 0.1985,
    0.1984, 0.1979, 0.1978, 0.1977])

m2l = array([1.589, 0.1443, 0.09093, 0.084, 0.0836, 0.08419, 0.09001, 0.08439,
    0.08366, 0.08398, 0.09362, 0.08407, 0.09, 0.08516, 0.08458, 0.08407,
    0.08425, 0.08408, 0.08493, 0.08362, 0.08382, 0.08408, 0.08379, 0.084,
    0.08421, 0.08403, 0.0838, 0.08407])

ind = arange(size(p2p))
width = 0.35

# set up plot
font = {'family':'serif','size':10}
fig = Figure(figsize=(3,2), dpi=80)
ax = fig.add_subplot(111)

# plot bars
bar1 = ax.bar(ind, p2p, width, color='r')
bar2 = ax.bar(ind+width, m2l, width, color='b')
rc('font',**font)

# axis labels
ax.set_ylabel('Time (s)', fontsize=10)
ax.set_xlabel('Iteration', fontsize=10)
xticks(arange(min(ind), max(ind)+1, 5.0))
# ax.set_xticklabels( ('8192','32768','131072') )
ax.legend( (bar1[0], bar2[0]), ('P2P', 'M2L'), loc=1 )
fig.subplots_adjust(left=0.185, bottom=0.21, right=0.965, top=0.95)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('StokesSolveBreakdown.pdf',dpi=80)

# text on scaling plot
#fig = Figure(figsize=(3,2), dpi=80)
#ax = fig.add_subplot(111)
#asymp = N*log(N)*total_time[0]/(N[0]*log(N[0]))
#ax.loglog(N, total_time, c='k', marker='o',ls=' ', mfc='w', ms=5, label='')
#ax.loglog(N, asymp,c='k',marker='None',ls=':', lw=0.8, label=None)
#loc = (3*N[0]+N[1])/4
#tex_loc = array((loc, loc*log(loc)*total_time[0]/(N[0]*log(N[0]))))
#tex_angle = math.atan2(log(abs(asymp[-1]-asymp[0])),log(abs(N[-1]-N[0])))*180/math.pi
#ax.text(tex_loc[0], tex_loc[1], 'NlogN', fontsize=8,rotation=tex_angle, rotation_mode='anchor')
#rc('font',**font)
#ax.set_ylabel('Total time [s]', fontsize=10)
#ax.set_xlabel('Number of elements', fontsize=10)
#fig.subplots_adjust(left=0.185, bottom=0.21, right=0.965, top=0.95)
#canvas = FigureCanvasPdf(fig)
#canvas.print_figure('plot2.pdf',dpi=80)
