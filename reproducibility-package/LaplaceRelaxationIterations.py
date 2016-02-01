# coding: utf-8

import sys
import numpy
from matplotlib import pyplot, rcParams
from matplotlib.backends.backend_pdf import FigureCanvasPdf

rcParams['font.family'] = 'serif'
rcParams['font.size'] = '10'

# set up data
it = numpy.array([5, 10, 15, 20, 25])

# it -> 50 ,t_fixed = 89.703, t_relaxed = 70.890

t_relax = numpy.array([6.4574, 10.930, 11.901, 14.712, 20.400])
t_fixed = numpy.array([10.787, 19.543, 28.605, 38.150, 45.513])

speedup = t_fixed / t_relax

print(t_relax, t_fixed)
print(speedup)

# set up plot
fig = pyplot.figure(figsize=(3,2), dpi=80)
ax = fig.add_subplot(111)

# plot log-log
ax.plot(it,speedup,c='k',marker='o', ls='-', mfc='w', ms=5, label='')

# axis labels
pyplot.xlim(5, 50)
pyplot.ylim(1, 4)
ax.set_ylabel('Speedup', fontsize=10)
ax.set_xlabel('Iterations', fontsize=10)
fig.subplots_adjust(left=0.195, bottom=0.21, right=0.955, top=0.95)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('LaplaceRelaxationIterations.pdf',dpi=80)