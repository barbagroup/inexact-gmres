# coding: utf-8

import sys
import numpy
from matplotlib import pyplot, rcParams
from matplotlib.backends.backend_pdf import FigureCanvasPdf

rcParams['font.family'] = 'serif'
rcParams['font.size'] = '10'

# set up data
N = 4

eps = 1e-14
data_relax = numpy.array([[14.61,eps,eps],[87.20,69.03,eps],[444.55,371.06,276.52],[1481.47,1800.53,1397.27]])
data_fixed = numpy.array([[48.18,0.,0.],[267.64,234.44,0],[1358.07,1494.37,978.80],[7077.77,12817.01,7209.57]])

speedup = data_fixed / data_relax

print(speedup)

ind = numpy.arange(N)
width = 0.3

# set up plot
fig = pyplot.figure(figsize=(4,3), dpi=80)
ax = fig.add_subplot(111)

# plot log-log
bar1 = ax.bar(ind, speedup[:,0], width, fill=False, edgecolor='k', hatch='..'*2, linewidth=1)
bar2 = ax.bar(ind+width, speedup[:,1],width,fill=False, edgecolor='k', hatch='//'*2, linewidth=1)
bar3 = ax.bar(ind+2*width,speedup[:,2],width,fill=False, edgecolor='k', hatch='x'*3, linewidth=1)
# bar2 = ax.bar(ind+width, speedup_2nd, width, color='b')

# axis labels
ax.set_ylabel('Speedup', fontsize=10)
ax.set_xlabel('N', fontsize=10)
ax.set_xticks(ind+1.5*width)
ax.set_xticklabels( ('2048','8192','32768','131072') )
ax.legend( (bar1[0], bar2[0], bar3[0]), ('2048 panels/cell', '8192 panels/cell', '32768 panels/cell'), loc=2, fontsize='small')
fig.subplots_adjust(left=0.195, bottom=0.21, right=0.955, top=0.95)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('EthrocyteMultipleCellSpeedup.pdf',dpi=80)