import os
import numpy as np
from matplotlib import *
from matplotlib.pyplot import *
from matplotlib.backends.backend_pdf import PdfFile, PdfPages, FigureCanvasPdf
import sys
import math

# set up data
N = np.array([128., 512, 2048, 8192, 32768])
e1 = np.array([4.278e-02, 1.643e-02, 6.147e-03, 2.237e-03, 9.179e-04])
e2 = np.array([1.705e-02, 4.265e-03, 1.023e-03, 2.408e-04, 5.681e-05])

line_sqrtN = 1 / np.sqrt(N)
line_N = 1 / N

print line_sqrtN
print line_N
# set up plot
font = {'family':'serif','size':10}
fig = Figure(figsize=(3,2), dpi=80)
ax = fig.add_subplot(111)

# plot log-log
ax.loglog(N,e1,c='k',marker='o', ls='-', mfc='w', ms=5, label='')
ax.loglog(N,line_sqrtN,c='k',ls='--', mfc='w', ms=5, label='')
ax.loglog(N,e2,c='k',marker='o', ls=':', mfc='w', ms=5, label='')
ax.loglog(N,line_N,c='k',ls='--', mfc='w', ms=5, label='')
#ax.loglog(N, error, c='k', marker='o',ls=' ', mfc='w', ms=5, label='')
#ax.loglog(N, asymp, c='k', marker='None', ls=':', lw=0.8, label=None)
rc('font',**font)
loc = (3*N[0]+N[1])/4

# text on plot
# 1 / sqrt(N)
tex_loc = np.array((loc,N[0]*e1[0]/loc))
tex_angle = math.atan2(np.log(np.abs(line_sqrtN[-1]-line_sqrtN[0])),np.log(np.abs(N[-1]-N[0])))*180/math.pi
ax.text(4*tex_loc[0], 1.5*tex_loc[1],r'$O(1/\sqrt{N})$',fontsize=8,rotation=tex_angle,rotation_mode='anchor')
# 1 / N
tex_loc = np.array((loc,N[0]*e2[0]/loc))
tex_angle = math.atan2(np.log(np.abs(line_N[-1]-line_N[0])),np.log(np.abs(N[-1]-N[0])))*180/math.pi
ax.text(tex_loc[0], tex_loc[1]/5.,r'$O(1/N)$',fontsize=8,rotation=tex_angle,rotation_mode='anchor')

# axis labels
ax.set_ylabel('Relative Error', fontsize=10)
ax.set_xlabel('N', fontsize=10)
fig.subplots_adjust(left=0.185, bottom=0.21, right=0.965, top=0.95)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('LaplaceConvergence.pdf',dpi=80)

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
