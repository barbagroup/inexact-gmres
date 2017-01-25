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
    if "case 1, p = 8" in line:
        break

for j,line in enumerate(lines):
    if "case 2, p = 10" in line:
        break

for k,line in enumerate(lines):
    if "LaplaceBEM speedup test - 1st-kind" in line:
        break


# parse the numbers from strings
temp1 = []   # case 1
temp2 = []	 # case 2

for line in lines[i+1:j]:
	for elem in line.replace(",","").split():
		# append numbers
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

# the second number of each line is residual
res1 = temp1[1:-2:3]
res2 = temp2[1:-2:3]

# the third number of each line is p_req
p1 = temp1[2:-2:3]
p2 = temp2[2:-2:3]

# the last line/iteration has a different format
# p_req = 1, residual parsed from result
res1.append(temp1[-2])
res2.append(temp2[-2])
p1.append(1)
p2.append(1)


# set the array of iteration numbers
it1 = len(p1)
ind1 = numpy.arange(it1, dtype=int) + 1
it2 = len(p2)
ind2 = numpy.arange(it2, dtype=int) + 1

# set up plot
fig = pyplot.figure(figsize=(7,2), dpi=80)

# left plot
ax1 = fig.add_subplot(121)
# plot residual
ax1.semilogy(ind1, numpy.array(res1, dtype=float),
	         color='k', ls='-')
# plot required-p
ax2 = ax1.twinx()
ax2.plot(ind1, numpy.array(p1, dtype=int), color='k',
	     marker='o', ls=':', mfc='w', ms=5)
# axis info
ax1.set_xlabel('Iterations', fontsize=10)
ax1.set_ylabel('Residual', fontsize=10)
ax1.set_ylim(1e-6, 1e-4)
ax2.set_xlim(1,18)
ax2.set_ylim(1,12)
pyplot.setp(ax2.get_yticklabels(), visible=False)

# right plot
ax3 = fig.add_subplot(122)
# plot residual
ax3.semilogy(ind2, numpy.array(res2, dtype=float),
	         color='k', ls='-')
# plot required-p
ax4 = ax3.twinx()
ax4.plot(ind2, numpy.array(p2, dtype=int), color='k',
	     marker='o', ls=':', mfc='w', ms=5)
# axis info
ax3.set_xlabel('Iterations', fontsize=10)
ax3.set_ylim(1e-6, 1e-4)
ax4.set_ylabel('$p$', fontsize=10)
ax4.set_xlim(1,18)
ax4.set_ylim(1,12)
pyplot.setp(ax3.get_yticklabels(), visible=False)

fig.subplots_adjust(left=0.145, bottom=0.21, right=0.865, top=0.95)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('LaplaceResidualIterations.pdf',dpi=80)