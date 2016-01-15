# coding: utf-8

import sys
import numpy
from matplotlib import pyplot, rcParams
from matplotlib.backends.backend_pdf import FigureCanvasPdf

rcParams['font.family'] = 'serif'
rcParams['font.size'] = '10'

result = open(sys.argv[1])
lines = result.readlines()

# Stokes convergence (recursions = {3..8})
recursions = numpy.arange(3,9, dtype=int)
N = 2 * 4**recursions

# parse the relative errors
e = []
for line in lines[1:len(recursions)+1]:
	for elem in line.split():
		try:
			e.append(float(elem))
		except ValueError:
			pass

e = numpy.array(e)

line_sqrtN = 1 / numpy.sqrt(N)

# set up plot
font = {'family':'serif','size':10}
fig = pyplot.figure(figsize=(3,2), dpi=80)
ax = fig.add_subplot(111)

# plot log-log
ax.loglog(N,e,c='k',marker='o', ls='-', mfc='w', ms=5, label='')
ax.loglog(N,line_sqrtN,c='k',ls='--', mfc='w', ms=5, label='')
loc = (3*N[0]+N[1])/4

# text on plot
# 1 / sqrt(N)
tex_loc = numpy.array((loc,N[0]*e[0]/loc))
tex_angle = numpy.arctan2(numpy.log(numpy.abs(line_sqrtN[-1]-line_sqrtN[0])),numpy.log(numpy.abs(N[-1]-N[0])))*180/numpy.pi
ax.text(tex_loc[0], tex_loc[1]/3.5,r'$O(1/\sqrt{N})$',fontsize=8,rotation=tex_angle-10,rotation_mode='anchor')
# axis labels
ax.set_ylabel('Relative Error', fontsize=10)
ax.set_xlabel('N', fontsize=10)
fig.subplots_adjust(left=0.185, bottom=0.21, right=0.965, top=0.95)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('StokesConvergence.pdf',dpi=80)