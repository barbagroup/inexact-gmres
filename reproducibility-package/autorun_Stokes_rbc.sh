#!/bin/bash
#
# inexact-GMRES reproducibility package:
# This script will automatically run a couple of tests on a Stokes problem on a
# sphere to generate the result data, which will be later used for reproducing
# the figures and tables in our paper.

# set the number of threads (using # of physical cores)
export OMP_NUM_THREADS=6

# define the path
DIR="./"

# define kernel name
KERNEL="StokesBEM"

# define the result file
OUT='Stokes_rbc_result'

# remove the existing result file
rm -f $OUT


#########################################################
########## Convergence for one red blood cell: ##########
#########################################################

printf "StokesBEM on 1 rbc: # of iterations:\n" >> $OUT

# When N = 131072, the memory on our machine is not enough for running with the optimal
# ncrit(around 400), so we use the largest possible ncrit(=150) in this case instead.

# fixed-p, tight parameters: p = 20, k = 13, tol = 1e-10, ncrit = 400
for i in {4..7}; do
	eval $DIR$KERNEL -p 20 -pmin 20 -fixed_p -k 13 -ncrit 400 -solver_tol 1e-10 -rbc $i -cells 1 | grep "Fx:" >> $OUT
done 

# fixed-p, tight parameters for the largest case (N = 131072)
eval $DIR$KERNEL -p 20 -pmin 20 -fixed_p -k 13 -ncrit 150 -solver_tol 1e-10 -rbc 8 -cells 1 | grep "Fx:" >> $OUT

# loose parameters: p/p_init = 14, pmin = 3, k = 4, tol = 1e-5
# fixed-p, loose parameters:
read ncrit_f[{5..8}] <<< $(echo 400 400 400 150)

for i in {5..8}; do
	eval $DIR$KERNEL -p 14 -pmin 14 -fixed_p -k 4 -ncrit ${ncrit_f[$i]} -solver_tol 1e-5 -rbc $i -cells 1 | grep "Fx:" >> $OUT
done

# relaxed-p, loose parameters:
read ncrit_r[{5..8}] <<< $(echo 130 140 120 100)

for i in {5..8}; do
	eval $DIR$KERNEL -p 14 -pmin 3 -k 4 -ncrit ${ncrit_r[$i]} -solver_tol 1e-5 -rbc $i -cells 1 | grep "Fx:" >> $OUT
done

# print out messages
printf ">>> StokesBEM on 1 rbc: Convergence test completed!\n"