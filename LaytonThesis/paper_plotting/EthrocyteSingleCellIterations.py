import os
import numpy as np
from numpy import *
from matplotlib import *
from matplotlib.pyplot import *
from matplotlib.backends.backend_pdf import PdfFile, PdfPages, FigureCanvasPdf
import sys
import math

# set up data
N = array([128, 512, 2048, 8192, 32768, 32768*4])
it = array([19, 24, 32, 37, 37, 36])

# set up plot
font = {'family':'serif','size':10}
fig = Figure(figsize=(3,2), dpi=80)
ax = fig.add_subplot(111)

# plot log-log
ax.semilogx(N,it,c='k',marker='o', ls='-', mfc='w', ms=5, label='')
rc('font',**font)

# axis labels
ax.set_ylabel('Iterations', fontsize=10)
ax.set_xlabel('N', fontsize=10)
fig.subplots_adjust(left=0.185, bottom=0.21, right=0.965, top=0.95)
canvas = FigureCanvasPdf(fig)

# plot to pdf
canvas.print_figure('EthrocyteSingleCellIterations.pdf',dpi=80)

