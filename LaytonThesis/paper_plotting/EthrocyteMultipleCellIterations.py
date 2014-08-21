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

N_2048 = array([2048, 2048*2, 2048*4, 2048*8, 2048*16, 2048*32, 2048*64])
cells_2048 = array([32, 45, 52, 61, 72, 77, 84])

N_8192 = array([8192, 8192*2, 8192*4, 8192*8, 8192*16])
cells_8192 = array([37, 46, 55, 66, 73])

N_32768 = array([32768, 65536, 32768*4])
cells_32768 = array([37, 46, 53])

N_2cells = array([4096, 16384, 65536])
it_2cells = array([45, 46, 46])

N_4cells = array([8192, 32768, 131072])
it_4cells = array([52, 55, 53])

N_8cells = array([16384, 65536])
it_8cells = array([61, 66])

# set up plot
font = {'family':'serif','size':10}
fig = Figure(figsize=(7,4), dpi=80)
ax = fig.add_subplot(111)

# plot log-log
bar1 = ax.semilogx(N_2048,cells_2048,c='k',marker='o', ls='-', mfc='w', ms=5, label='')
bar2 = ax.semilogx(N_8192,cells_8192,c='k',marker='o', ls=':', mfc='w', ms=5, label='')
bar3 = ax.semilogx(N_32768,cells_32768,c='k',marker='o', ls='-.', mfc='w', ms=5, label='')
bar4 = ax.semilogx(N_2cells,it_2cells,c='r',marker='o', ls='-', mfc='w', ms=5, label='')
bar5 = ax.semilogx(N_4cells,it_4cells,c='r',marker='o', ls=':', mfc='w', ms=5, label='')
bar6 = ax.semilogx(N_8cells,it_8cells,c='r',marker='o', ls='-.', mfc='w', ms=5, label='')
rc('font',**font)

# axis labels
ax.set_ylabel('Iterations', fontsize=10)
ax.set_xlabel('N', fontsize=10)
ax.legend( (bar1[0],bar2[0],bar3[0],bar4[0],bar5[0],bar6[0]), ('2048 per cell','8192 per cell','32768 per cell','2 cells','4 cells','8cells'),loc=2)
fig.subplots_adjust(left=0.185, bottom=0.21, right=0.965, top=0.95)
canvas = FigureCanvasPdf(fig)



# plot to pdf
canvas.print_figure('EthrocyteMultipleCellIterations.pdf',dpi=80)

