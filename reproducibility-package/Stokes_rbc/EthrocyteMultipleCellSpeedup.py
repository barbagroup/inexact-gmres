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

for i,line in enumerate(lines):
    if "StokesBEM on 1 rbc: Speedup test" in line:
        break

for j,line in enumerate(lines):
    if "StokesBEM on multiple rbcs: Speedup test" in line:
        break

for k,line in enumerate(lines):
    if "StokesBEM on multiples rbcs - num of iterations:" in line:
        break


# single rbc
temp1 = []

for line in lines[i+1:j]:
    # remove string "s" (seconds) for parsing
    for elem in line.replace("s","").split():
        try:
            temp1.append(float(elem))
        except ValueError:
            pass

del temp1[::2]
time_single = numpy.array(temp1).reshape(len(temp1)//3, 3)
time_single = numpy.mean(time_single, axis=1)
speedup_single = time_single[::2] / time_single[1::2]

# single cell
# print out the execution time
print("fixed-p: ", time_single[::2])
print("relaxed-p: ", time_single[1::2])

# multiple rbcs
temp2 = []
for line in lines[j+1:k]:
    # remove string "s" (seconds) for parsing
    for elem in line.replace("s","").split():
        try:
            temp2.append(float(elem))
        except ValueError:
            pass

del temp2[::2]
time_multi = numpy.array(temp2).reshape(len(temp2)//3, 3)
time_multi = numpy.mean(time_multi, axis=1)
speedup_multi = time_multi[::2] / time_multi[1::2]


# multiple cells
# print out the execution time
print("fixed-p: ", time_multi[::2])
print("relaxed-p: ", time_multi[1::2])

# set up data
# 2048, 8192, 32768 panels per cell
s_2048 = numpy.array([speedup_single[0], *speedup_multi[:3]])
s_8192 = numpy.array([0, speedup_single[1], *speedup_multi[3:5]])
s_32768 = numpy.array([0, 0, speedup_single[2], *speedup_multi[5:]])

print(s_2048)
print(s_8192)
print(s_32768)

# set up plot
fig = pyplot.figure(figsize=(4,3), dpi=80)
ax = fig.add_subplot(111)

ind = numpy.arange(4)
width = 0.3

# plot log-log
bar1 = ax.bar(ind, s_2048, width, fill=False,
	          edgecolor='k', hatch='..'*2, linewidth=1)
bar2 = ax.bar(ind+width, s_8192, width, fill=False,
	          edgecolor='k', hatch='//'*2, linewidth=1)
bar3 = ax.bar(ind+2*width, s_32768, width, fill=False,
	          edgecolor='k', hatch='x'*3, linewidth=1)


# axis labels
ax.set_ylabel('Speedup', fontsize=10)
ax.set_xlabel('N', fontsize=10)
ax.set_xticks(ind+1.5*width)
ax.set_xticklabels( ('2048','8192','32768','131072') )
ax.legend( (bar1[0], bar2[0], bar3[0]), ('2048 panels/cell', '8192 panels/cell', '32768 panels/cell'), loc=2, fontsize='small')
fig.subplots_adjust(left=0.195, bottom=0.21, right=0.955, top=0.95)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('EthrocyteMultipleCellSpeedup.pdf',dpi=80)