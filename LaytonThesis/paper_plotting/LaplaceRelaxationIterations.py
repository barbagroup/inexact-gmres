import os
import numpy as np
from numpy import *
from matplotlib import *
from matplotlib.pyplot import *
from matplotlib.backends.backend_pdf import PdfFile, PdfPages, FigureCanvasPdf
import sys
import math

# set up data
it = array([5, 10, 15, 20, 25, 50])

t_relax = array([8.57, 9.81, 11.1, 12.4, 13.7, 20.6])
t_fixed = array([10, 18.4, 26.9, 35.3, 43.8, 86.2])

speedup = t_fixed / t_relax;

# set up plot
font = {'family':'serif','size':10}
fig = Figure(figsize=(3,2), dpi=80)
ax = fig.add_subplot(111)

# plot log-log
ax.plot(it,speedup,c='k',marker='o', ls='-', mfc='w', ms=5, label='')
rc('font',**font)

# axis labels
ax.set_ylabel('Speedup', fontsize=10)
ax.set_xlabel('Iterations', fontsize=10)
fig.subplots_adjust(left=0.185, bottom=0.21, right=0.965, top=0.95)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('LaplaceRelaxationIterations.pdf',dpi=80)

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
