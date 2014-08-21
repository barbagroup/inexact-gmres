import os
import numpy as np
from numpy import *
from matplotlib import *
from matplotlib.pyplot import *
from matplotlib.backends.backend_pdf import PdfFile, PdfPages, FigureCanvasPdf
import sys
import math

# set up data
N = np.array([10000, 13335, 17782, 23713, 31622, 42169, 56234, 74989, 100000, 
    133352, 177827, 237137, 316227, 421696, 562341, 749894, 1000000]);
t = np.array([2.598e-01, 3.211e-01, 4.182e-01, 5.954e-01, 9.709e-01, 1.539e+00, 
    2.436e+00, 2.603e+00, 3.135e+00, 3.949e+00, 5.281e+00, 8.501e+00, 
    1.298e+01, 2.107e+01, 2.299e+01, 2.656e+01, 3.254e+01]); 
e = np.array([])

# set up plot
font = {'family':'serif','size':10}
fig = Figure(figsize=(3,2), dpi=80)
ax = fig.add_subplot(111)

# plot log-log
ax.loglog(N,t,c='k',marker='o', ls='-', mfc='w', ms=5, label='')
ax.loglog(N,N/10000.,c='k',ls=':', mfc='w', ms=5, label='')
#ax.loglog(N, error, c='k', marker='o',ls=' ', mfc='w', ms=5, label='')
#ax.loglog(N, asymp, c='k', marker='None', ls=':', lw=0.8, label=None)
rc('font',**font)
loc = (3*N[0]+N[1])/4

# text of plot
tex_loc = array((loc,N[0]*t[0]/loc))
tex_angle = math.atan2(log(abs(N[-1]/10000-N[0]/10000)),log(abs(N[-1]-N[0])))*180/math.pi
ax.text(tex_loc[0], 6.5*tex_loc[1],r'$O(N)$',fontsize=8,rotation=tex_angle,rotation_mode='anchor')

# axis labels
ax.set_ylabel('Time (s)', fontsize=10)
ax.set_xlabel('N', fontsize=10)
fig.subplots_adjust(left=0.185, bottom=0.21, right=0.965, top=0.95)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('FMMScaling.pdf',dpi=80)

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
