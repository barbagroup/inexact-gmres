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
    if "case 1" in line:
        break

for j,line in enumerate(lines):
    if "case 2" in line:
        break

for k,line in enumerate(lines):
    if "LaplaceBEM speedup test - 1st-kind" in line:
        break

temp1 = []   # p=12, k=4, ncrit=300
temp2 = []	 # p=8, k=4, ncrit=100
for line in lines[i+1:j]:
	for elem in line.replace(",","").split():
		try:
			temp1.append(float(elem))
		except ValueError:
			pass

for line in lines[j+1:k]:
	for elem in line.replace(",","").split():
		try:
			temp2.append(float(elem))
		except ValueError:
			pass

# append the final residual at the end
r1 = numpy.append(numpy.array(temp1[1::3], dtype=float), 9.8885e-07)
p1 = numpy.append(numpy.array(temp1[2::3], dtype=int), 1)
r2 = numpy.append(numpy.array(temp2[1::3], dtype=float), 9.6815e-07)
p2 = numpy.append(numpy.array(temp2[2::3], dtype=int), 1)

it1 = numpy.size(p1)
ind1 = numpy.arange(it1, dtype=int) + 1
it2 = numpy.size(p2)
ind2 = numpy.arange(it2, dtype=int) + 1

# set up plot
fig = pyplot.figure(figsize=(7,2), dpi=80)
# left plot
ax1 = fig.add_subplot(121)
	# plot residual
ax1.semilogy(ind1,r1,color='k',marker='', ls='-', mfc='w', ms=5)
ax1.set_xticks(ind1[::2])
	# plot required-p
ax2 = ax1.twinx()
ax2.plot(ind1,p1,color='k',marker='o',ls=':', mfc='w', ms=5)
	# axis labels
ax1.set_ylabel('Residual', fontsize=10)
ax1.set_xlabel('Iterations', fontsize=10)
ax1.set_ylim(1e-6, 1e-4)
ax2.set_ylim(1,12)
ax2.set_xlim(1,16)
pyplot.setp(ax2.get_yticklabels(), visible=False)

# right plot
ax3 = fig.add_subplot(122)
	# plot residual
ax3.semilogy(ind2,r2,color='k',marker='', ls='-', mfc='w', ms=5)
ax3.set_xticks(ind1[::2])   # use the same xticks for both
	# plot required-p
ax4 = ax3.twinx()
ax4.plot(ind2,p2,color='k',marker='o',ls=':', mfc='w', ms=5)
	# axis labels
ax3.set_xlabel('Iterations', fontsize=10)
ax3.set_ylim(1e-6, 1e-4)
ax4.set_ylabel('$p$', fontsize=10)
ax4.set_xlim(1,16)
ax4.set_ylim(1,12)
pyplot.setp(ax3.get_yticklabels(), visible=False)

fig.subplots_adjust(left=0.145, bottom=0.21, right=0.865, top=0.95)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('LaplaceResidualIterations.pdf',dpi=80)

