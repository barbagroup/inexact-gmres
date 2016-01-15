# coding: utf-8

import sys
import numpy
from matplotlib import pyplot, rcParams
from matplotlib.backends.backend_pdf import FigureCanvasPdf

rcParams['font.family'] = 'serif'
rcParams['font.size'] = '10'

result = open(sys.argv[1])
lines = result.readlines()

# Laplace Convergence (recursions={3, 4, 5, 6, 7})
start, n = 3, 5	# first value of recursions(=3), number of tests(=5, from 3 to 7)
recursions = numpy.arange(start, start+n, dtype=int)
N = 2 * 4**recursions	# number of panels

# parse the relative errors
e = []
for line in lines[:2*(n+1)]:
	for elem in line.split():
		try:
			e.append(float(elem))
		except ValueError:
			pass

e1 = numpy.array(e[:n])
e2 = numpy.array(e[n:])

# lines for reference
line_sqrtN = 1 / numpy.sqrt(N)
line_N = 1 / N

# set up plot
fig = pyplot.figure(figsize=(3,2), dpi=80)
ax = fig.add_subplot(111)

# plot log-log
ax.loglog(N,e1,color='k', marker='o', ls='-', mfc='w', ms=5)
ax.loglog(N,line_sqrtN,color='k',ls='--', mfc='w', ms=5)
ax.loglog(N,e2,color='k',marker='o', ls=':', mfc='w', ms=5)
ax.loglog(N,line_N,color='k',ls='--', mfc='w', ms=5)
loc = (3*N[0]+N[1])/4

# text on plot
# 1 / sqrt(N)
tex_loc = numpy.array((loc,N[0]*e1[0]/loc))
tex_angle = numpy.arctan2(numpy.log(numpy.abs(line_sqrtN[-1]-line_sqrtN[0])),numpy.log(numpy.abs(N[-1]-N[0])))*180/numpy.pi
ax.text(4*tex_loc[0], 1.5*tex_loc[1],r'$O(1/\sqrt{N})$',fontsize=8,rotation=tex_angle,rotation_mode='anchor')
# 1 / N
tex_loc = numpy.array((loc,N[0]*e2[0]/loc))
tex_angle = numpy.arctan2(numpy.log(numpy.abs(line_N[-1]-line_N[0])),numpy.log(numpy.abs(N[-1]-N[0])))*180/numpy.pi
ax.text(tex_loc[0], tex_loc[1]/5.,r'$O(1/N)$',fontsize=8,rotation=tex_angle,rotation_mode='anchor')

# axis labels
ax.set_ylabel('Relative Error', fontsize=10)
ax.set_xlabel('N', fontsize=10)
fig.subplots_adjust(left=0.185, bottom=0.21, right=0.965, top=0.95)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('LaplaceConvergence.pdf',dpi=80)

