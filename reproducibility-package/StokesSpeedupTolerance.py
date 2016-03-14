# coding: utf-8

import sys
import numpy
from matplotlib import pyplot, rcParams
from matplotlib.backends.backend_pdf import FigureCanvasPdf

rcParams['font.family'] = 'serif'
rcParams['font.size'] = '10'

# set up data
tol = 10**numpy.arange(-3, -11, -1, dtype=float)
print(tol)

t_relax = numpy.array([1.0780e+01, 3.0205e+01, 4.9527e+01, 7.8644e+01, 1.0592e+02, 1.8391e+02, 2.3971e+02, 3.2187e+02])
t_fixed = numpy.array([1.7921e+01, 6.6619e+01, 1.5039e+02, 2.4847e+02, 3.3733e+02, 4.2533e+02, 5.0892e+02, 5.6729e+02])

res = numpy.array([2.64378e-02, 2.31630e-02, 2.47985e-02, 2.00446e-02, 2.27640e-02, 2.30615e-02, 2.30037e-02, 2.30257e-02])

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

pyplot.ylim(0,4)
fig.subplots_adjust(left=0.195, bottom=0.21, right=0.955, top=0.95)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('StokesSpeedupTolerance.pdf',dpi=80)