# coding: utf-8

import sys
import numpy
from matplotlib import pyplot, rcParams
from matplotlib.backends.backend_pdf import FigureCanvasPdf

rcParams['font.family'] = 'serif'
rcParams['font.size'] = '10'

f1 = - 0.05705
f2 = - 0.07033
f3 = - 0.07678
f4 = - 0.07989

# calculate approximated exact solution using Richardson Extrapolation
f_bar = (f1*f3 - f2**2) / (f1 - 2*f2 + f3)

# absolute and relative error
err_abs = numpy.array([f1,f2,f3,f4])
err_rel = numpy.abs((err_abs - f_bar)/f_bar)

# set up data
N = numpy.array([512, 2048, 8192, 32768])

line_sqrtN = 1 / numpy.sqrt(N)

# set up plot
fig = pyplot.figure(figsize=(3,2), dpi=80)
ax = fig.add_subplot(111)

# plot log-log
ax.loglog(N,err_rel,c='k',marker='o', ls='-', mfc='w', ms=5, label='')
ax.loglog(N,line_sqrtN,c='k',ls='--', mfc='w', ms=5, label='')
loc = (3*N[0]+N[1])/4

# text on plot
# 1 / sqrt(N)
tex_loc = numpy.array((loc,N[0]*err_rel[0]/loc))
tex_angle = numpy.arctan2(numpy.log(numpy.abs(line_sqrtN[-1]-line_sqrtN[0])),numpy.log(numpy.abs(N[-1]-N[0])))*180/numpy.pi
ax.text(tex_loc[0], tex_loc[1]/3.5,r'$O(1/\sqrt{N})$',fontsize=8,rotation=tex_angle, rotation_mode='anchor')
# axis labels
ax.set_ylabel('Relative Error', fontsize=10)
ax.set_xlabel('N', fontsize=10)
fig.subplots_adjust(left=0.195, bottom=0.21, right=0.955, top=0.95)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('EthrocyteConvergence.pdf',dpi=80)