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

# define the result filename
OUT='Stokes_sphere_result'

# remove the existing result file
rm -f $OUT


##################################
########## Convergence: ##########
##################################

# When N = 131072, the memory on our machine is not enough for running with the optimal
# ncrit(around 400), so we use the largest possible ncrit(=150) in this case instead.

# fixed-p, tight parameters: p = 20, k = 13, tol = 1e-10, ncrit = 400
printf "StokesBEM on a sphere: Convergence\n" >> $OUT

for i in {3..7}; do
	eval $DIR$KERNEL -p 20 -pmin 20 -fixed_p -k 13 -ncrit 400 -solver_tol 1e-10 -recursions $i | grep "error on a sphere" >> $OUT
done

# fixed-p, tight parameters for the largest case (N = 131072)
eval $DIR$KERNEL -p 20 -pmin 20 -fixed_p -k 13 -ncrit 150 -solver_tol 1e-10 -recursions 8 | grep "error on a sphere" >> $OUT

# fixed-p, loose parameters:
read p[{6..8}] <<< $(echo 12 12 14)
read ncrit[{6..8}] <<< $(echo 300 400 150)

for i in {6..8}; do
	eval $DIR$KERNEL -p ${p[$i]} -pmin ${p[$i]} -fixed_p -k 4 -ncrit ${ncrit[$i]} -solver_tol 1e-5 -recursions $i | grep "error on a sphere" >> $OUT
done

# relaxed-p, loose parameters:
read p[{6..8}] <<< $(echo 12 12 14)
read pmin[{6..8}] <<< $(echo 4 3 4)
read ncrit[{6..8}] <<< $(echo 100 60 80)
read tol[{6..8}] <<< $(echo 1e-5 1e-5 5e-6)

for i in {6..8}; do
	eval $DIR$KERNEL -p ${p[$i]} -pmin ${pmin[$i]} -k 4 -ncrit ${ncrit[$i]} -solver_tol ${tol[$i]} -recursions $i | grep "error on a sphere" >> $OUT
done

# print out messages
printf ">>> StokesBEM on a sphere: Convergence test completed!\n"



################################################
########## Time Breakdown P2P vs M2L: ##########
################################################

printf "StokesBEM on a sphere: Time breakdown\n" >> $OUT

# the optimal case for N = 32768
# p_init = 12, p_min = 3, k = 4, tol = 1e-5, ncrit = 60
eval $DIR$KERNEL -p 12 -pmin 3 -k 4 -ncrit 60 -solver_tol 1e-5 -recursions 6 | grep "P2P" >> $OUT

# print out messages
printf ">>> StokesBEM on a sphere: Time breakdown test completed!\n"



###################################
########## Speedup Test: ##########
###################################

printf "StokesBEM on a sphere: Speedup\n" >> $OUT

# speedup test: using loose parameters, optimal ncrits
read p[{6..8}] <<< $(echo 12 12 14)   # p or p_intial
read pmin[{6..8}] <<< $(echo 4 3 4)  # p_min
read ncrit_f[{6..8}] <<< $(echo 300 400 150)   # fixed-p
read ncrit_r[{6..8}] <<< $(echo 100 60 80)   # relaxed-p
read tol[{6..8}] <<< $(echo 1e-5 1e-5 5e-6)   # tolerance

for i in {6..8}; do

    printf "recursions = $i fixed-p\n" >> $OUT
    for j in {1..3}; do 
    	eval $DIR$KERNEL -p ${p[$i]} -pmin ${p[$i]} -fixed_p -k 4 -ncrit ${ncrit_f[$i]} -solver_tol 1e-5 -recursions $i | grep "solve " >> $OUT
    done

    printf "recursions = $i relaxed-p\n" >> $OUT
    for j in {1..3}; do
    	eval $DIR$KERNEL -p ${p[$i]} -pmin ${pmin[$i]} -k 4 -ncrit ${ncrit_r[$i]} -solver_tol ${tol[$i]} -recursions $i | grep "solve " >> $OUT
    done

done
printf ">>> StokesBEM on a sphere: Speedup test completed!\n"