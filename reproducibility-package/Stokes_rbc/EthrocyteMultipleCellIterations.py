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
	if "StokesBEM on multiples rbcs - num of iterations:" in line:
		break

temp =[]

for line in lines[i+1:]:
    for elem in line.split():
        try:
            temp.append(float(elem))
        except ValueError:
            pass

temp = numpy.array(temp, dtype=int)


# find the indices of 2048, 8192, 32768
a, b, c = numpy.where(temp > 2000)[0]

# set up data
it_cells_2048 = temp[a+1:b]
it_cells_8192 = temp[b+1:c]
it_cells_32768 = temp[c+1:]

N_2048 = 2048 * 2**numpy.arange(len(it_cells_2048))
N_8192 = 8192 * 2**numpy.arange(len(it_cells_8192))
N_32768 = 32768 * 2**numpy.arange(len(it_cells_32768))

# we don't have the third case for 8 cells due to memory limitation
it_2cells = numpy.array([it_cells_2048[1], it_cells_8192[1], it_cells_32768[1]])
it_4cells = numpy.array([it_cells_2048[2], it_cells_8192[2], it_cells_32768[2]])
it_8cells = numpy.array([it_cells_2048[3], it_cells_8192[3]])

N = numpy.array([2048, 8192, 32768])
N_2cells = 2 * N
N_4cells = 4 * N
N_8cells = 8 * N[:-1]

# set up plot
fig = pyplot.figure(figsize=(7,4), dpi=80)
ax = fig.add_subplot(111)

# plot log-log
bar4 = ax.semilogx(N_2cells, it_2cells, c='k', marker='o',
	               ls=':', mfc='w', ms=6, label='', lw=1)
bar5 = ax.semilogx(N_4cells, it_4cells, c='k', marker='^',
	               ls=':', mfc='w', ms=7, label='', lw=1)
bar6 = ax.semilogx(N_8cells, it_8cells, c='k', marker='D',
	               ls=':', mfc='w', ms=5, label='', lw=1)

bar1 = ax.semilogx(N_2048, it_cells_2048, c='k', marker='x',
	               ls='-', mfc='w', ms=4, label='', lw=1)
bar2 = ax.semilogx(N_8192, it_cells_8192, c='k', marker='x',
	               ls='--', mfc='w', ms=4, label='', lw=1)
bar3 = ax.semilogx(N_32768,it_cells_32768,c='k', marker='x',
	               ls='-.', mfc='w', ms=4, label='', lw=1)

# axis labels
ax.set_ylim(30, 80)
ax.set_ylabel('Iterations', fontsize=10)
ax.set_xlabel('N', fontsize=10)
ax.legend( (bar1[0],bar2[0],bar3[0],bar4[0],bar5[0],bar6[0]), 
	      ('2048 per cell','8192 per cell','32768 per cell',
	       '2 cells','4 cells','8 cells'),loc=2, fontsize=10)
fig.subplots_adjust(left=0.145, bottom=0.21, right=0.915, top=0.95)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('EthrocyteMultipleCellIterations.pdf',dpi=80)