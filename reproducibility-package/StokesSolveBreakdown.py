# coding: utf-8

import sys
import numpy
from matplotlib import pyplot, rcParams
from matplotlib.backends.backend_pdf import FigureCanvasPdf

rcParams['font.family'] = 'serif'
rcParams['font.size'] = '10'

result = open(sys.argv[1])
lines = result.readlines()

for i,line in enumerate(lines):
    if "StokesBEM on a sphere: Time breakdown" in line:
        break

temp = []

for line in lines[i+1:]:
    # remove string "s" (seconds) for parsing
    for elem in line.replace("s"," ").split():
        try:
            temp.append(float(elem))
        except ValueError:
            pass

# set up data
p2p = numpy.array(temp[::2], dtype=float)[1:]
m2l = numpy.array(temp[1::2], dtype=float)[1:] 

ind = numpy.arange(len(p2p))
width = 0.35

# set up plot
font = {'family':'serif','size':10}
fig = pyplot.figure(figsize=(9,4), dpi=80)
ax = fig.add_subplot(111)

# plot bars
bar1 = ax.bar(ind, p2p, width, fill=False, edgecolor='k', hatch='.'*3, linewidth=1)
bar2 = ax.bar(ind+width, m2l, width, fill=False, edgecolor='k', hatch='/'*10, linewidth=1)

# axis labels
ax.set_ylabel('Time (s)', fontsize=14)
ax.set_xlabel('Iteration', fontsize=14)
pyplot.xticks(numpy.arange(min(ind), max(ind)+1, 5.0))
# ax.set_xticklabels( ('8192','32768','131072') )
ax.legend( (bar1[0], bar2[0]), ('P2P', 'M2L'), loc=1, fontsize=10)
fig.subplots_adjust(left=0.065, bottom=0.21, right=0.965, top=0.95)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('StokesSolveBreakdown.pdf',dpi=80)