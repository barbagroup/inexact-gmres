# coding: utf-8

import sys
import numpy
from matplotlib import pyplot, rcParams
from matplotlib.backends.backend_pdf import FigureCanvasPdf

rcParams['font.family'] = 'serif'
rcParams['font.size'] = '10'

# set up data
tol = 10**numpy.arange(-5, -12, -1, dtype=float)
print(tol)

# it -> 50 ,t_fixed = 89.703, t_relaxed = 70.890

t_relax = numpy.array([1.6450, 2.3425, 4.0652, 5.7684, 8.1425, 1.0105e+01, 1.2244e+01])
t_fixed = numpy.array([3.1261, 4.7109, 7.9344, 9.8651, 1.2510e+01, 1.6292e+01, 1.7878e+01])

speedup = t_fixed / t_relax

print(t_relax, t_fixed)
print(speedup)

# set up plot
fig = pyplot.figure(figsize=(3,2), dpi=80)
ax = fig.add_subplot(111)

# plot log-log
ax.plot(tol,speedup,c='k',marker='o', ls='-', mfc='w', ms=5, label='')

# axis labels
#pyplot.xlim(5, 50)
#pyplot.ylim(1, 4)
ax.set_ylabel('Speedup', fontsize=10)
ax.set_xlabel('tolerance', fontsize=10)
ax.set_xscale('log')

pyplot.axhline(y=1.0, linestyle='dashed', color='k')

pyplot.ylim(0,2.5)
fig.subplots_adjust(left=0.195, bottom=0.21, right=0.955, top=0.95)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('LaplaceSpeedupTolerance.pdf',dpi=80)