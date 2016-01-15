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
	if "fixed-p residual history" in line:
		a = i
	elif "relaxed-p residual history" in line:
		b = i
	elif "StokesBEM on a sphere: Speedup" in line:
		c = i

# set up data
temp = []
for line in lines[a+1:b]:
	for elem in line.replace(",","").split():
		try:
			temp.append(float(elem))
		except ValueError:
			pass

it1 = numpy.array(temp[::3], dtype=int)
r1 = numpy.array(temp[1::3], dtype=float)

temp = []
for line in lines[b+1:c]:
	for elem in line.replace(",","").split():
		try:
			temp.append(float(elem))
		except ValueError:
			pass

it2 = numpy.array(temp[::3], dtype=int)
r2 = numpy.array(temp[1::3], dtype=float)

# set up plot
fig = pyplot.figure(figsize=(3,2), dpi=80)
ax = fig.add_subplot(111)

# plot log-log
line1, = ax.semilogy(it1,r1,color='k',marker='', ls='-', mfc='w', ms=5, label='Fixed p')
line2, = ax.semilogy(it2,r2,color='k',marker='', ls=':', mfc='w', ms=5, label='Relaxed')

# axis labels
ax.set_ylabel('Residual', fontsize=10)
ax.set_xlabel('Iteration', fontsize=10)
ax.legend( (line1, line2), ('Fixed p', 'Relaxed') )
ax.set_ylim(1e-6, 1e-2)
fig.subplots_adjust(left=0.185, bottom=0.21, right=0.965, top=0.95)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('StokesResidualHistory.pdf',dpi=80)