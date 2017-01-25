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
	if "StokesBEM on 1 rbc: num of Iterations test" in line:
		break

for j,line in enumerate(lines):
    if "StokesBEM on 1 rbc: Speedup test" in line:
        break

for k,line in enumerate(lines):
	if "StokesBEM on multiple rbcs: Speedup test" in line:
		break



temp = []

# only extract the numbers of iterations
for line in lines[i+1:j] + lines[j+1:k]:
    for elem in line.split():
        try:
            temp.append(float(elem))
        except ValueError:
            pass

# recursions = 3,4
iters3 = int(temp.pop(0))
iters4 = int(temp.pop(0))

# calculate the average number of iterations for each run
# recursions = 5,6,7,8
iters = numpy.array(temp).reshape((len(temp)//3), 3)
iters = numpy.mean(iters, axis=1)

# set up data
N = 2 * 4**numpy.arange(3,9)

# only need fixed-p cases
# recursions = 5,6,7,8
iters_fixed = numpy.array(iters[::2], dtype=int)
# recursions = 3,4
iters_fixed = numpy.insert(iters_fixed, [0,0], [iters3, iters4])

print(iters_fixed)

# set up plot
fig = pyplot.figure(figsize=(3,2), dpi=80)
ax = fig.add_subplot(111)

# plot log-log
ax.semilogx(N, iters_fixed, c='k', marker='o', ls='-', mfc='w', ms=5)


# axis labels
ax.set_ylabel('Iterations', fontsize=10)
ax.set_xlabel('N', fontsize=10)
fig.subplots_adjust(left=0.195, bottom=0.21, right=0.955, top=0.95)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('EthrocyteSingleCellIterations.pdf',dpi=80)