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
	if "StokesBEM on multiples rbcs" in line:
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
idx = numpy.where(temp > 2000)[0]

# set up data
N_2048 = temp[idx[0]] * temp[idx[0]+1:idx[1]:2]
cells_2048 = temp[idx[0]+2:idx[1]:2]

N_8192 = temp[idx[1]] * temp[idx[1]+1:idx[2]:2]
cells_8192 = temp[idx[1]+2:idx[2]:2]

N_32768 = temp[idx[2]] * temp[idx[2]+1::2]
cells_32768 = temp[idx[2]+2::2]

it_2cells = []
it_4cells = []
it_8cells = []

for index, elem in enumerate(temp):
	if elem == 2:
		it_2cells.append(temp[index+1])
	elif elem == 4:
		it_4cells.append(temp[index+1])
	elif elem == 8:
		it_8cells.append(temp[index+1])


N = numpy.array([2048, 8192, 32768])
N_2cells = 2 * N
N_4cells = 4 * N
N_8cells = 8 * N[:-1]

# set up plot
fig = pyplot.figure(figsize=(7,4), dpi=80)
ax = fig.add_subplot(111)

# plot log-log
bar1 = ax.semilogx(N_2048,cells_2048,c='k',marker='o', ls='-', mfc='w', ms=5, label='')
bar2 = ax.semilogx(N_8192,cells_8192,c='k',marker='o', ls=':', mfc='w', ms=5, label='')
bar3 = ax.semilogx(N_32768,cells_32768,c='k',marker='o', ls='-.', mfc='w', ms=5, label='')
bar4 = ax.semilogx(N_2cells,it_2cells,c='r',marker='o', ls='-', mfc='w', ms=5, label='')
bar5 = ax.semilogx(N_4cells,it_4cells,c='r',marker='o', ls=':', mfc='w', ms=5, label='')
bar6 = ax.semilogx(N_8cells,it_8cells,c='r',marker='o', ls='-.', mfc='w', ms=5, label='')

# axis labels
ax.set_ylabel('Iterations', fontsize=10)
ax.set_xlabel('N', fontsize=10)
ax.legend( (bar1[0],bar2[0],bar3[0],bar4[0],bar5[0],bar6[0]), ('2048 per cell','8192 per cell','32768 per cell','2 cells','4 cells','8cells'),loc=2)
fig.subplots_adjust(left=0.145, bottom=0.21, right=0.915, top=0.95)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('EthrocyteMultipleCellIterations.pdf',dpi=80)