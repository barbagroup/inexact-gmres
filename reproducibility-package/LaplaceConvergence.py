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
    if "LaplaceBEM Residual History and required-p" in line:
        break

# panel numbers
recursions = numpy.arange(3, 9, dtype=int)
N = 2 * 4**recursions

# parse the relative errors
temp = []
for line in lines[:i]:
	for elem in line.split():
		try:
			temp.append(float(elem))
		except ValueError:
			pass

m = len(temp)    # total number of data
temp1 = numpy.array(temp[:m//2])   # 1st-kind
temp2 = numpy.array(temp[m//2:])   # 2nd-kind

# tight parameters, fixed-p
e1 = temp1[:6]
e2 = temp2[:6]

# loose parameters, fixed-p
e1_fixed = temp1[6:9]
e2_fixed = temp2[6:9]

# loose parameters, relaxed-p
e1_relaxed = temp1[9:]
e2_relaxed = temp2[9:]

# set up plot
fig = pyplot.figure(figsize=(7,3), dpi=80)

# left plot: 1st-kind
ax1 = fig.add_subplot(121)

ax1.loglog(N, e1, c='k', ls='-', lw=1.0, marker='o', mfc='w',
	       ms=5, label='fixed-p, tight parameters')
ax1.loglog(N[-3:], e1_fixed, c='k', ls='-', lw=0.5, marker='+',
           ms=5, label='fixed-p, loose parameters')
ax1.loglog(N[-3:], e1_relaxed, c='k', ls='-', lw=0.5, marker='x',
           ms=5, label='relaxed-p, loose parameters')

ax1.set_xlabel('$N$', fontsize=10)
ax1.set_ylabel('Relative Error')
ax1.legend(loc=1, fontsize=7)
ax1.grid('on')
ax1.set_title('1st-kind', fontsize=10)

# right plot: 2nd-kind
ax2 = fig.add_subplot(122)

ax2.loglog(N, e2, c='k', ls='-', lw=1.0, marker='o', mfc='w',
	       ms=5, label='fixed-p, tight parameters')
ax2.loglog(N[-3:], e2_fixed, c='k', ls='-', lw=0.5, marker='+',
           ms=5, label='fixed-p, loose parameters')
ax2.loglog(N[-3:], e2_relaxed, c='k', ls='-', lw=0.5, marker='x',
           ms=5, label='relaxed-p, loose parameters')

ax2.set_xlabel('$N$', fontsize=10)
ax2.legend(loc=1, fontsize=7)
ax2.set_yticklabels([])
ax2.grid('on')
ax2.set_title('2nd-kind', fontsize=10)

fig.subplots_adjust(left=0.15, bottom=0.15, right=0.87, top=0.92)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('LaplaceConvergence.pdf',dpi=80)