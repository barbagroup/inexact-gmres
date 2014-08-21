import os
import numpy as np
from numpy import *
from matplotlib import *
from matplotlib.pyplot import *
from matplotlib.backends.backend_pdf import PdfFile, PdfPages, FigureCanvasPdf
import sys
import math

# set up data
N = array([128, 512, 2048, 8192, 32768, 131072])
e = array([1.84e-1, 9.27e-2, 4.61e-2, 2.41e-2, 1.14e-2, 5.80e-3])

line_sqrtN = 1 / np.sqrt(N)

# set up plot
font = {'family':'serif','size':10}
fig = Figure(figsize=(3,2), dpi=80)
ax = fig.add_subplot(111)

# plot log-log
ax.loglog(N,e,c='k',marker='o', ls='-', mfc='w', ms=5, label='')
ax.loglog(N,line_sqrtN,c='k',ls='--', mfc='w', ms=5, label='')
rc('font',**font)
loc = (3*N[0]+N[1])/4

# text on plot
# 1 / sqrt(N)
tex_loc = np.array((loc,N[0]*e[0]/loc))
tex_angle = math.atan2(np.log(np.abs(line_sqrtN[-1]-line_sqrtN[0])),np.log(np.abs(N[-1]-N[0])))*180/math.pi
ax.text(tex_loc[0], tex_loc[1]/3.5,r'$O(1/\sqrt{N})$',fontsize=8,rotation=tex_angle-10,rotation_mode='anchor')
# axis labels
ax.set_ylabel('Relative Error', fontsize=10)
ax.set_xlabel('N', fontsize=10)
fig.subplots_adjust(left=0.185, bottom=0.21, right=0.965, top=0.95)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('StokesConvergence.pdf',dpi=80)

