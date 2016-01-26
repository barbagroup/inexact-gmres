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
    if "StokesBEM on a sphere: Speedup" in line:
        break

for j,line in enumerate(lines):
    if "StokesBEM on a sphere: Time breakdown" in line:
        break

temp = []

for line in lines[i+1:j]:
    # remove string "s" (seconds) for parsing
    for elem in line.replace("s","").split():
        try:
            temp.append(float(elem))
        except ValueError:
            pass

# remove problem size number from the list
N = 2 * 4**numpy.array(temp[::8], dtype=int)
del temp[::4]

# make an average for each case
time = numpy.mean(numpy.array(temp).reshape(-1,3), axis=1)

# calculate speedup
speedup = time[::2] / time[1::2]

# set up plot
fig = pyplot.figure(figsize=(3,2), dpi=80)
ax = fig.add_subplot(111)

# plot log-log
ax.semilogx(N,speedup,color='k',marker='o', ls='-', mfc='w', ms=5, label='')

# axis labels
ax.set_ylabel('Speedup', fontsize=10)
ax.set_xlabel('N', fontsize=10)
fig.subplots_adjust(left=0.195, bottom=0.21, right=0.955, top=0.95)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('StokesSpeedupRelaxation.pdf',dpi=80)