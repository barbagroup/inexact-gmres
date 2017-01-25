# coding: utf-8

import sys
import numpy
from matplotlib import pyplot, rcParams
from matplotlib.backends.backend_pdf import FigureCanvasPdf

rcParams['font.family'] = 'serif'
rcParams['font.size'] = '10'

# open the result file
result = open(sys.argv[1])

# set up data
N, t = numpy.loadtxt(result, dtype=float, unpack=True)

# set up plot
fig = pyplot.figure(figsize=(3,2), dpi=80)
ax = fig.add_subplot(111)


# plot log-log
ax.loglog(N,t,color='k',marker='o', ms=5, mfc='w')
ax.loglog(N,N/20000,color='k', ls=':', ms=5, mfc='w')
loc = (3*N[0]+N[1])/4

# text of plot
tex_loc = numpy.array((loc,N[0]*t[0]/loc)) * 1.2
tex_angle = numpy.arctan2(numpy.log(abs(N[-1]/10000-N[0]/10000)),numpy.log(abs(N[-1]-N[0])))*180/numpy.pi
ax.text(tex_loc[0], 6.5*tex_loc[1],r'$O(N)$',fontsize=10,rotation=tex_angle,rotation_mode='anchor')

# axis labels
ax.set_ylabel('Time (s)', fontsize=10)
ax.set_xlabel('N', fontsize=10)
fig.subplots_adjust(left=0.195, bottom=0.21, right=0.955, top=0.95)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('FMMScaling.pdf',dpi=80)