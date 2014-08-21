import os
import numpy as np
from numpy import *
from matplotlib import *
from matplotlib.pyplot import *
from matplotlib.backends.backend_pdf import PdfFile, PdfPages, FigureCanvasPdf
import sys
import math

# set up data
r = array([1.985e-03, 4.819e-04, 3.695e-04, 2.392e-04, 1.777e-04, 1.476e-04, 1.411e-04,
    1.296e-04, 1.187e-04, 1.088e-04, 9.828e-05, 8.027e-05, 6.599e-05, 5.445e-05,
    4.936e-05, 3.779e-05, 3.300e-05, 2.778e-05, 2.281e-05, 2.145e-05, 1.921e-05,
    1.770e-05, 1.462e-05, 1.367e-05, 1.137e-05, 1.054e-05, 9.2166e-06])

r2 = array([1.985e-03, 4.820e-04, 3.696e-04, 2.394e-04, 1.812e-04, 1.708e-04, 1.423e-04,
    1.366e-04, 1.242e-04, 1.111e-04, 9.853e-05, 8.041e-05, 6.692e-05, 5.988e-05,
    4.896e-05, 4.433e-05, 3.768e-05, 3.500e-05, 2.768e-05, 2.620e-05, 2.231e-05,
    1.997e-05, 1.744e-05, 1.623e-05, 1.419e-05, 1.245e-05, 1.006e-05, 8.2839e-06])

it1 = arange(size(r))
it2 = arange(size(r2))

# set up plot
font = {'family':'serif','size':10}
fig = Figure(figsize=(3,2), dpi=80)
ax = fig.add_subplot(111)

# plot log-log
line1 = ax.semilogy(it1,r,c='k',marker='', ls='-', mfc='w', ms=5, label='Fixed p')
line2 = ax.semilogy(it2,r2,c='k',marker='', ls=':', mfc='w', ms=5, label='Relaxed')
rc('font',**font)

# axis labels
ax.set_ylabel('Residual', fontsize=10)
ax.set_xlabel('Iteration', fontsize=10)
ax.legend( (line1, line2), ('Fixed p', 'Relaxed') )
fig.subplots_adjust(left=0.185, bottom=0.21, right=0.965, top=0.95)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('StokesResidualHistory.pdf',dpi=80)

