#!/bin/bash

# set the number of threads (using # of physical cores)
export OMP_NUM_THREADS=6

# define the path
DIR="./"

# StokesBEM kernel
kernel="StokesBEM"

# define the result file
OUT='Stokes_rbc_result'

# remove the existing result file
rm -f $OUT

# Fig-3.14 Num of iterations need to converge for a single rbc: p = 16, rbc {3..8}
printf "StokesBEM on 1 rbc: # of iterations:\n" >> $OUT
for i in {3..8}
	do eval $DIR$kernel -lazy_eval -p 16 -fixed_p -rbc $i -cells 1
done 


# Fig 3.16 Num of iterations need to converge for multiple rbcs: p = 16, 