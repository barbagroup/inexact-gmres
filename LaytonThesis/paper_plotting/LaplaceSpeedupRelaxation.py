import os
import numpy as np
from numpy import *
from matplotlib import *
from matplotlib.pyplot import *
from matplotlib.backends.backend_pdf import PdfFile, PdfPages, FigureCanvasPdf
import sys
import math

# set up data
N = 3

t_variable_1st = array([1.7, 5.07, 20.72])
t_variable_2nd = array([1.19, 5.92, 24.2])
t_fixed_1st = array([2.58, 7.1, 30.1])
t_fixed_2nd = array([1.49, 6.77, 30.01])

speedup_1st = t_fixed_1st / t_variable_1st;
speedup_2nd = t_fixed_2nd / t_variable_2nd;

ind = arange(N)
width = 0.35

# set up plot
font = {'family':'serif','size':10}
fig = Figure(figsize=(3,2), dpi=80)
ax = fig.add_subplot(111)

print speedup_1st, speedup_2nd
# plot log-log
bar1 = ax.bar(ind, speedup_1st, width, color='r')
bar2 = ax.bar(ind+width, speedup_2nd, width, color='b')
rc('font',**font)

# axis labels
ax.set_ylabel('Speedup', fontsize=10)
ax.set_xlabel('N', fontsize=10)
ax.set_xticks(ind+width)
ax.set_xticklabels( ('8192','32768','131072') )
ax.legend( (bar1[0], bar2[0]), ('1st-kind', '2nd-kind'), loc=4 )
fig.subplots_adjust(left=0.185, bottom=0.21, right=0.965, top=0.95)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('LaplaceSpeedupRelaxation.pdf',dpi=80)

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
