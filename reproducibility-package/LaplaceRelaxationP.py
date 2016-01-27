# coding: utf-8

import sys
import numpy
from matplotlib import pyplot, rcParams
from matplotlib.backends.backend_pdf import FigureCanvasPdf

rcParams['font.family'] = 'serif'
rcParams['font.size'] = '10'

#result = open(sys.argv[1])
#lines = result.readlines()

# set up data
N = 5
t_relax = numpy.array([3.9448, 6.1992, 9.0813, 12.696, 22.055])
t_fixed = numpy.array([7.5261, 12.376, 19.960, 25.412, 37.766])

speedup = t_fixed / t_relax
ind = numpy.arange(N, dtype=int)
width = 0.35

# set up plot
font = {'family':'serif','size':10}
fig = pyplot.figure(figsize=(3,2), dpi=80)
ax = fig.add_subplot(111)

print(t_relax,t_fixed)
print(speedup)
# plot log-log
bar1 = ax.bar(ind, t_fixed, width, color='r')
bar2 = ax.bar(ind+width, t_relax, width, color='b')

# axis labels
ax.set_ylabel('Time (s)', fontsize=10)
ax.set_xlabel('p', fontsize=10)
ax.set_xticks(ind+width)
ax.set_xticklabels( ('5','8','10','12','15') )
fig.subplots_adjust(left=0.195, bottom=0.21, right=0.955, top=0.95)
ax.legend( (bar1[0], bar2[0]), ('fixed p', 'Relaxed'), loc=2 )
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('LaplaceRelaxationP.pdf',dpi=80)