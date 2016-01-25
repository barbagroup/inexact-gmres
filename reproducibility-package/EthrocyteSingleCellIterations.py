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
    if "StokesBEM on one rbc" in line:
        break

for j,line in enumerate(lines):
	if "StokesBEM on multiples rbcs" in line:
		break

temp = []

for line in lines[i+1:j]:
    for elem in line.split():
        try:
            temp.append(float(elem))
        except ValueError:
            pass

# set up data
N = 2 * 4**numpy.array(temp[::2], dtype=int)
it = numpy.array(temp[1::2], dtype=int)

# set up plot
fig = pyplot.figure(figsize=(3,2), dpi=80)
ax = fig.add_subplot(111)

# plot log-log
ax.semilogx(N,it,c='k',marker='o', ls='-', mfc='w', ms=5)


# axis labels
ax.set_ylabel('Iterations', fontsize=10)
ax.set_xlabel('N', fontsize=10)
fig.subplots_adjust(left=0.185, bottom=0.21, right=0.965, top=0.95)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('EthrocyteSingleCellIterations.pdf',dpi=80)