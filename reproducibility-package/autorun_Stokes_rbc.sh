#!/bin/bash
#
# inexact-GMRES reproducibility package:
# This script will automatically run a couple of tests on a Stokes problem on
# red blood cells to generate the result data, which will be later used for
# reproducing the figures and tables in our paper.

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

printf "StokesBEM Convergence on 1 rbc:\n" >> $OUT

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


###############################################################
########## num of iterations for one red blood cell: ##########
###############################################################

# recursions = {3,4}, just for plotting # of iterations for one red blood cell
# for larger meshes, we obtain the iteration number from the speedup tests below

printf "StokesBEM on 1 rbc: num of Iterations test\n" >> $OUT

for i in {3..4}; do

	eval $DIR$KERNEL -p 14 -pmin 14 -fixed_p -k 4 -ncrit 400 -solver_tol 1e-5 -rbc $i -cells 1 | grep "Final" >> $OUT

done

printf ">>> StokesBEM on 1 rbc: num of Iterations test completed!\n"

#####################################################
########## Speedup for one red blood cell: ##########
#####################################################

printf "StokesBEM on 1 rbc: Speedup test\n" >> $OUT

# speedup test: using loose parameters, optimal ncrits
read ncrit_f[{5..8}] <<< $(echo 400 400 400 150)   # fixed-p
read ncrit_r[{5..8}] <<< $(echo 130 140 120 100)   # relaxed-p

# record both execution time and # of iterations
for i in {5..8}; do

	printf "recursions = $i, cells = 1, fixed-p\n" >> $OUT
	for j in {1..3}; do
		eval $DIR$KERNEL -p 14 -pmin 14 -fixed_p -k 4 -ncrit ${ncrit_f[$i]} -solver_tol 1e-5 -rbc $i -cells 1 | grep -E "solve|Final" >> $OUT
	done

	printf "recursions = $i, cells = 1, relaxed-p\n" >> $OUT
	for j in {1..3}; do
		eval $DIR$KERNEL -p 14 -pmin 3 -k 4 -ncrit ${ncrit_r[$i]} -solver_tol 1e-5 -rbc $i -cells 1 | grep -E "solve|Final" >> $OUT
	done

done

# print out messages
printf ">>> StokesBEM on 1 rbc: Speedup test completed!\n"


###########################################################
########## Speedup for multiple red blood cells: ##########
###########################################################

printf "StokesBEM on multiple rbcs: Speedup test\n" >> $OUT

# speedup test: using loose parameters, optimal ncrits

# 2048 panels per cell, cells = {4, 16, 64}
read cells[{1..3}] <<< $(echo 4 16 64)
read ncrit_f[{1..3}] <<< $(echo 400 400 150)   # fixed-p
read ncrit_r[{1..3}] <<< $(echo 140 100 120)   # relaxed-p

for i in {1..3}; do
	
	printf "recursions = 5, cells = ${cells[$i]}, fixed-p\n" >> $OUT
	for j in {1..3}; do
		eval $DIR$KERNEL -p 14 -pmin 14 -fixed_p -k 4 -ncrit ${ncrit_f[$i]} -solver_tol 1e-5 -rbc 5 -cells ${cells[$i]} | grep -E "solve|Final" >> $OUT
	done

	printf "recursions = 5, cells = ${cells[$i]}, relaxed-p\n" >> $OUT
	for j in {1..3}; do
		eval $DIR$KERNEL -p 14 -pmin 3 -k 4 -ncrit ${ncrit_r[$i]} -solver_tol 1e-5 -rbc 5 -cells ${cells[$i]} | grep -E "solve|Final" >> $OUT
	done

done

# 8192 panels per cell, cells = {4, 16}
read cells[{1..2}] <<< $(echo 4 16)
read ncrit_f[{1..2}] <<< $(echo 400 150)   # fixed-p
read ncrit_r[{1..2}] <<< $(echo 120 100)   # relaxed-p
read pmin[{1..2}] <<< $(echo 3 4)    # pmin

for i in {1..2}; do
	
	printf "recursions = 6, cells = ${cells[$i]}, fixed-p\n" >> $OUT
	for j in {1..3}; do
		eval $DIR$KERNEL -p 14 -pmin 14 -fixed_p -k 4 -ncrit ${ncrit_f[$i]} -solver_tol 1e-5 -rbc 6 -cells ${cells[$i]} | grep -E "solve|Final" >> $OUT
	done

	printf "recursions = 6, cells = ${cells[$i]}, relaxed-p\n" >> $OUT
	for j in {1..3}; do
		eval $DIR$KERNEL -p 14 -pmin ${pmin[$i]} -k 4 -ncrit ${ncrit_r[$i]} -solver_tol 1e-5 -rbc 6 -cells ${cells[$i]} | grep -E "solve|Final" >> $OUT
	done

done

# 32768 panels per cell, cells = {4}
printf "recursions = 7, cells = 4, fixed-p\n" >> $OUT
for j in {1..3}; do
	eval $DIR$KERNEL -p 14 -pmin 14 -fixed_p -k 4 -ncrit 150 -solver_tol 1e-5 -rbc 7 -cells 4 | grep -E "solve|Final" >> $OUT
done

printf "recursions = 7, cells = 4, relaxed-p\n" >> $OUT
for j in {1..3}; do
	eval $DIR$KERNEL -p 14 -pmin 3 -k 4 -ncrit 120 -solver_tol 1e-5 -rbc 7 -cells 4 | grep -E "solve|Final" >> $OUT
done

# print out messages
printf ">>> StokesBEM on multiple rbcs: Speedup test completed!\n"