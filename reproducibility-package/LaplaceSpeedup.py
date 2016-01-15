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
    if "LaplaceBEM speedup test - 1st-kind" in line:
        break

# initialize a list of temporary parsing result
temp = []

for line in lines[i+1:]:
    # remove string "s" (seconds) for parsing
    for elem in line.replace("s","").split():
        try:
            temp.append(float(elem))
        except ValueError:
            pass

# remove recursion number from the list
del temp[::4]

# make an average for each case
time = numpy.mean(numpy.array(temp).reshape(-1,3), axis=1)

# calculate the speedups
speedup = time[::2] / time[1::2]
speedup_1st = speedup[:len(speedup)/2]
speedup_2nd = speedup[len(speedup)/2:]

# set up plot
ind = numpy.arange(len(speedup)/2)
width = 0.35

fig = pyplot.figure(figsize=(3,2), dpi=80)
ax = fig.add_subplot(111)

# plot log-log
bar1 = ax.bar(ind, speedup_1st, width, color='r')
bar2 = ax.bar(ind+width, speedup_2nd, width, color='b')

# axis labels
ax.set_ylabel('Speedup', fontsize=10)
ax.set_xlabel('N', fontsize=10)
ax.set_xticks(ind+width)
ax.set_xticklabels( ('2048','8192','32768','131072') )
ax.legend( (bar1[0], bar2[0]), ('1st-kind', '2nd-kind'), loc=4)
fig.subplots_adjust(left=0.185, bottom=0.21, right=0.965, top=0.95)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('LaplaceSpeedup.pdf',dpi=80)