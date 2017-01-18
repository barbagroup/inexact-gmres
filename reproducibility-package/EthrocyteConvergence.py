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
    if "StokesBEM Convergence on 1 rbc:" in line:
        break

for j,line in enumerate(lines):
    if "StokesBEM on 1 rbc: num of Iterations test" in line:
        break


# panel numbers
recursions = numpy.arange(4, 9, dtype=int)
N = 2 * 4**recursions

temp = []

for line in lines[i+1:j]:
	for elem in line.replace(",","").split():
		# append numbers
		try:
			temp.append(float(elem))
		except ValueError:
			pass

temp = - numpy.array(temp[::2])    # only keep fx, negative sign shows fx's direction

f = temp[:5]    # fixed-p, tight parameters
f_fixed = temp[5:9]    # fixed-p, loose parameters
f_relaxed = temp[9:]   # relaxed-p, loose parameters

# use Richardson extrapolation to calculate f_bar
f_bar = (f[0]*f[2] - f[1]**2) / (f[0] - 2*f[1] + f[2])

# estimated relative error
e = numpy.abs((f-f_bar) / f_bar)
e_fixed = numpy.abs((f_fixed-f_bar) / f_bar)
e_relaxed = numpy.abs((f_relaxed-f_bar) / f_bar)

# reference line
# use scale to move up the line (save space for drawing legend)
scale1 = 1.6    # for plot adjustment
line_sqrtN = 1 / numpy.sqrt(N) * scale1

# set up plot
fig = pyplot.figure(figsize=(3,2), dpi=80)
ax = fig.add_subplot(111)

# plot log-log
ax.loglog(N, e, c='k', ls='-', lw=1.0, marker='o', mfc='w', 
	      ms=5, label='non-relaxed, tight parameters')
ax.loglog(N[1:], e_fixed, c='k', ls='-', lw=0.5, marker='+',
           ms=5, label='non-relaxed, loose parameters')
ax.loglog(N[1:], e_relaxed, c='k', ls='-', lw=0.5, marker='x',
           ms=5, label='relaxed, loose parameters')

# referece line
ax.loglog(N, line_sqrtN, c='k',ls='--')

# text on plot
scale2 = 0.6    # for plot adjustment
loc = (3*N[0]+N[1])/4
tex_loc = numpy.array((loc, N[0]*e[0]/loc)) * scale2
tex_angle = - 23
ax.text(tex_loc[0], tex_loc[1]/3.5, r'$O(1/\sqrt{N})$', 
	    fontsize=8, rotation=tex_angle, rotation_mode='anchor')

# axis labels
ax.set_ylabel('Relative Error', fontsize=10)
ax.set_xlabel('N', fontsize=10)
ax.set_ylim(5e-4, 1e0)
ax.legend(loc=3, fontsize=6)

fig.subplots_adjust(left=0.195, bottom=0.21, right=0.955, top=0.92)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('EthrocyteConvergence.pdf',dpi=80)