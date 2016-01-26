# coding: utf-8

import sys
import numpy
from matplotlib import pyplot, rcParams
from matplotlib.backends.backend_pdf import FigureCanvasPdf

rcParams['font.family'] = 'serif'
rcParams['font.size'] = '10'

result = open(sys.argv[1])
lines = result.readlines()

# set up data
N = 5
t_relax = array([4.21, 6.24, 8.76, 13.2, 19.3])
t_fixed = array([6.34, 12.4, 18.5, 25.3, 38.3])

speedup = t_fixed / t_relax
ind = arange(N)
width = 0.35

# set up plot
font = {'family':'serif','size':10}
fig = Figure(figsize=(3,2), dpi=80)
ax = fig.add_subplot(111)

print array([t_relax,t_fixed])
# plot log-log
bar1 = ax.bar(ind, t_fixed, width, color='r')
bar2 = ax.bar(ind+width, t_relax, width, color='b')

# axis labels
ax.set_ylabel('Time (s)', fontsize=10)
ax.set_xlabel('p', fontsize=10)
ax.set_xticks(ind+width)
ax.set_xticklabels( ('5','8','10','12','15') )
fig.subplots_adjust(left=0.185, bottom=0.21, right=0.965, top=0.95)
ax.legend( (bar1[0], bar2[0]), ('fixed p', 'Relaxed'), loc=2 )
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('LaplaceRelaxationP.pdf',dpi=80)