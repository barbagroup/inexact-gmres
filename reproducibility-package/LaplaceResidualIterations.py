# coding: utf-8

import sys
import numpy
from matplotlib import pyplot, rcParams
from matplotlib.backends.backend_pdf import FigureCanvasPdf

rcParams['font.family'] = 'serif'
rcParams['font.size'] = '10'

result = open(sys.argv[1])
lines = result.readlines()

# parse the residuals and required-p s
for i,line in enumerate(lines):
    if "LaplaceBEM Residual History and required-p" in line:
        break
for j,line in enumerate(lines):
    if "LaplaceBEM speedup test - 1st-kind" in line:
        break

temp = []
for line in lines[i+1:j]:
	for elem in line.replace(",","").split():
		try:
			temp.append(float(elem))
		except ValueError:
			pass

r = numpy.array(temp[1::3], dtype=float)
p = numpy.array(temp[2::3], dtype=int)

it = numpy.size(p)
ind = numpy.arange(it)

# set up plot
fig = pyplot.figure(figsize=(3.7,2), dpi=80)
ax = fig.add_subplot(111)

# plot log-log
ax.semilogy(ind,r,color='k',marker='', ls='-', mfc='w', ms=5)

ax2 = ax.twinx()
ax2.plot(ind,p,color='k',marker='o',ls=':', mfc='w', ms=5)

# axis labels
ax.set_ylabel('Residual', fontsize=10)
ax.set_xlabel('Iterations', fontsize=10)
ax2.set_ylabel('p',fontsize=10)
fig.subplots_adjust(left=0.185, bottom=0.21, right=0.965, top=0.95)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('LaplaceResidualIterations.pdf',dpi=80)

