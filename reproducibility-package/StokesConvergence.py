# coding: utf-8

import sys
import numpy
from matplotlib import pyplot, rcParams
from matplotlib.backends.backend_pdf import FigureCanvasPdf

rcParams['font.family'] = 'serif'
rcParams['font.size'] = '10'

# load result file
result = open(sys.argv[1])
lines = result.readlines()

# find line numbers
for i,line in enumerate(lines):
    if "StokesBEM on a sphere: Time breakdown" in line:
        break

# panel numbers
recursions = numpy.arange(3,9, dtype=int)
N = 2 * 4**recursions

# parse the relative errors
temp = []
for line in lines[:i]:
	for elem in line.split():
		try:
			temp.append(float(elem))
		except ValueError:
			pass

temp = numpy.array(temp)

# relative error
e = temp[:6]    # fixed-p, tight parameters
e_fixed = temp[6:9]    # fixed-p, loose parameters
e_relaxed = temp[9:]   # relaxed-p, loose parameters

# reference line
line_sqrtN = 1 / numpy.sqrt(N)

# set up plot
fig = pyplot.figure(figsize=(3,2), dpi=80)
ax = fig.add_subplot(111)

# plot log-log
ax.loglog(N, e, c='k', ls='-', lw=1.0, marker='o', mfc='w', 
	      ms=5, label='fixed-p, tight parameters')
ax.loglog(N[3:], e_fixed, c='k', ls='-', lw=0.5, marker='+',
           ms=5, label='fixed-p, loose parameters')
ax.loglog(N[3:], e_relaxed, c='k', ls='-', lw=0.5, marker='x',
           ms=5, label='relaxed-p, loose parameters')
ax.loglog(N,line_sqrtN,c='k',ls='--', mfc='w', ms=5, label='')

# text on plot
# 1 / sqrt(N)
loc = (3*N[0]+N[1])/4
tex_loc = numpy.array((loc,N[0]*e[0]/loc))
tex_angle = numpy.arctan2(numpy.log(numpy.abs(line_sqrtN[-1]-line_sqrtN[0])), 
	                      numpy.log(numpy.abs(N[-1]-N[0])))*180/numpy.pi
ax.text(tex_loc[0], tex_loc[1]/3.5, r'$O(1/\sqrt{N})$', fontsize=8,
	    rotation=tex_angle-10, rotation_mode='anchor')

# axis labels
ax.set_ylabel('Relative Error', fontsize=10)
ax.set_xlabel('N', fontsize=10)
ax.legend(loc=1, fontsize=6)

fig.subplots_adjust(left=0.195, bottom=0.21, right=0.955, top=0.95)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('StokesConvergence.pdf',dpi=80)