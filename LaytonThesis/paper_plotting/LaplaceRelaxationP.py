import os
import numpy as np
from numpy import *
from matplotlib import *
from matplotlib.pyplot import *
from matplotlib.backends.backend_pdf import PdfFile, PdfPages, FigureCanvasPdf
import sys
import math

# set up data
N = 5
t_relax = array([4.21, 6.24, 8.76, 13.2, 19.3])
t_fixed = array([6.34, 12.4, 18.5, 25.3, 38.3])

speedup = t_fixed / t_relax
ind = arange(N)
width = 0.35

# set up plot
font = {'family':'serif','size':10}
fig = Figure(figsize=(3,2), dpi=80)
ax = fig.add_subplot(111)

print array([t_relax,t_fixed])
# plot log-log
bar1 = ax.bar(ind, t_fixed, width, color='r')
bar2 = ax.bar(ind+width, t_relax, width, color='b')
rc('font',**font)

# axis labels
ax.set_ylabel('Time (s)', fontsize=10)
ax.set_xlabel('p', fontsize=10)
ax.set_xticks(ind+width)
ax.set_xticklabels( ('5','8','10','12','15') )
fig.subplots_adjust(left=0.185, bottom=0.21, right=0.965, top=0.95)
ax.legend( (bar1[0], bar2[0]), ('fixed p', 'Relaxed'), loc=2 )
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('LaplaceRelaxationP.pdf',dpi=80)

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
