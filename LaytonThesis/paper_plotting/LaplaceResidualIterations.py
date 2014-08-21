import os
import numpy as np
from numpy import *
from matplotlib import *
from matplotlib.pyplot import *
from matplotlib.backends.backend_pdf import PdfFile, PdfPages, FigureCanvasPdf
import sys
import math

# set up data
p = array([8,8, 7, 6, 5, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1])
r = array([1.016e-02, 2.123e-03, 6.290e-04, 2.550e-04, 1.638e-04, 1.247e-04, 8.260e-05,
    7.000e-05, 4.220e-05, 2.883e-05, 2.372e-05, 1.888e-05, 1.394e-05, 1.168e-05, 9.4244e-06])

it = size(p)
ind = arange(it)

# set up plot
font = {'family':'serif','size':10}
fig = Figure(figsize=(3.7,2), dpi=80)
ax = fig.add_subplot(111)

# plot log-log
ax.semilogy(ind,r,c='k',marker='', ls='-', mfc='w', ms=5, label='')
rc('font',**font)

ax2 = ax.twinx()
ax2.plot(ind,p,c='k',marker='o',ls=':', mfc='w', ms=5, label='')

# axis labels
ax.set_ylabel('Residual', fontsize=10)
ax.set_xlabel('Iterations', fontsize=10)
ax2.set_ylabel('p',fontsize=10)
fig.subplots_adjust(left=0.185, bottom=0.21, right=0.965, top=0.95)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('LaplaceResidualIterations.pdf',dpi=80)
