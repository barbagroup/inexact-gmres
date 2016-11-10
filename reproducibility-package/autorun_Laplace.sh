#!/bin/bash
#
# inexact-GMRES reproducibility package:
# This script will automatically run a couple of tests on a Laplace problem to 
# generate the result data, which will be later used for reproducing the figures
# and tables in our paper.

# set the number of threads (using # of physical cores)
export OMP_NUM_THREADS=6

# define the path
DIR="./"

# define kernel name
KERNEL="LaplaceBEM"

# define the result filename
OUT='Laplace_result'

# remove the existing result file
rm -f $OUT


####################################################
########## Convergence: 1st-kind problem: ##########
####################################################

printf "LaplaceBEM Convergence - 1st-kind:\n" >> $OUT

# fixed-p, tight parameters: p = 20, k = 13, tol = 1e-10, ncrit = 400
for i in {3..8}; do
	eval $DIR$KERNEL -p 20 -fixed_p -k 13 -ncrit 400 -solver_tol 1e-10 -recursions $i | grep 'external phi' >> $OUT
done

# fixed-p, loose parameters:
read p[{6..8}] <<< $(echo 8 10 10)
read ncrit[{6..8}] <<< $(echo 300 400 500)
for i in {6..8}; do
	eval $DIR$KERNEL -p ${p[$i]} -fixed_p -k 4 -ncrit ${ncrit[$i]} -solver_tol 1e-6 -recursions $i | grep 'external phi' >> $OUT
done

# relaxed-p, loose parameters:
read p[{6..8}] <<< $(echo 8 10 10)
read ncrit[{6..8}] <<< $(echo 100 100 200)
for i in {6..8}; do
	eval $DIR$KERNEL -p ${p[$i]} -k 4 -ncrit ${ncrit[$i]} -solver_tol 1e-6 -recursions $i | grep 'external phi' >> $OUT
done

# print out messages
printf ">>> LaplaceBEM convergence test for the 1st-kind problem completed!\n"


####################################################
########## Convergence: 2nd-kind problem: ##########
####################################################

printf "LaplaceBEM Convergence - 2nd-kind:\n" >> $OUT

# fixed-p, tight parameters: p = 20, k = 13, tol = 1e-10, ncrit = 400
for i in {3..8}; do
	eval $DIR$KERNEL -p 20 -fixed_p -k 13 -ncrit 400 -solver_tol 1e-10 -recursions $i -second_kind | grep 'external phi' >> $OUT
done

# fixed-p, loose parameters:
read p[{6..8}] <<< $(echo 8 10 10)
read ncrit[{6..8}] <<< $(echo 300 400 500)
for i in {6..8}; do
	eval $DIR$KERNEL -p ${p[$i]} -fixed_p -k 4 -ncrit ${ncrit[$i]} -solver_tol 1e-6 -recursions $i -second_kind | grep 'external phi' >> $OUT
done

# relaxed-p, loose parameters:
read p[{6..8}] <<< $(echo 8 10 10)
read ncrit[{6..8}] <<< $(echo 300 300 300)
for i in {6..8}; do
	eval $DIR$KERNEL -p ${p[$i]} -k 4 -ncrit ${ncrit[$i]} -solver_tol 1e-6 -recursions $i -second_kind | grep 'external phi' >> $OUT
done

# print out messages
printf ">>> LaplaceBEM convergence test for the 2nd-kind problem completed!\n"


###################################################################
########## Residual & required-p plot: 1st-kind problem: ##########
###################################################################

printf "LaplaceBEM Residual History and required-p:\n" >> $OUT

# N = 32768, k = 4, solver_tol = 1e-6, ncrit = 100 (optimal), p = {8,10} with relaxation

# case 1 when p = 8:
printf "case 1, p = 8:\n" >> $OUT
eval $DIR$KERNEL -p 8 -k 4 -recursions 7 -ncrit 100 -solver_tol 1e-6 | grep -E "fmm_req_p|residual" >> $OUT

# case 2 when p = 10:
printf "case 2, p = 10:\n" >> $OUT
eval $DIR$KERNEL -p 10 -k 4 -recursions 7 -ncrit 100 -solver_tol 1e-6 | grep -E "fmm_req_p|residual" >> $OUT

# print out messages
printf ">>> LaplaceBEM residual history & required-p test completed!\n"


#####################################################
########## Speedup test: 1st-kind problem: ##########
#####################################################

printf "LaplaceBEM speedup test - 1st-kind:\n" >> $OUT

# Speedup 1st-kind: using loose parameters, optimal ncrits
read p[{6..8}] <<< $(echo 8 10 10)   # p or p_intial
read ncrit_f[{6..8}] <<< $(echo 300 400 500)   # fixed-p
read ncrit_r[{6..8}] <<< $(echo 100 100 200)   # relaxed-p

for i in {6..8}; do
	
	printf "recursions = $i fixed-p 1st-kind\n" >> $OUT
	for j in {1..3}; do 
		eval $DIR$KERNEL -p ${p[$i]} -fixed_p -k 4 -ncrit ${ncrit_f[$i]} -solver_tol 1e-6 -recursions $i | grep "solve " >> $OUT
	done

	printf "recursions = $i relaxed-p 1st-kind\n" >> $OUT
	for j in {1..3}; do
		eval $DIR$KERNEL -p ${p[$i]} -k 4 -ncrit ${ncrit_r[$i]} -solver_tol 1e-6 -recursions $i | grep "solve " >> $OUT
	done

done

# print out messages
printf ">>> LaplaceBEM speedup test for the 1st-kind problem completed!\n"


#####################################################
########## Speedup test: 2nd-kind problem: ##########
#####################################################

printf "LaplaceBEM speedup test - 2nd-kind:\n" >> $OUT

# Speedup 2nd-kind: using loose parameters, optimal ncrits
read p[{6..8}] <<< $(echo 8 10 10)   # p or p_intial
read ncrit_f[{6..8}] <<< $(echo 300 400 500)   # fixed-p
read ncrit_r[{6..8}] <<< $(echo 300 300 300)   # relaxed-p

for i in {6..8}; do

	printf "recursions = $i fixed-p 2nd-kind\n" >> $OUT
	for j in {1..3}; do 
		eval $DIR$KERNEL -p ${p[$i]} -fixed_p -k 4 -ncrit ${ncrit_f[$i]} -solver_tol 1e-6 -recursions $i -second_kind | grep "solve " >> $OUT
	done

	printf "recursions = $i relaxed-p 2nd-kind\n" >> $OUT
	for j in {1..3}; do
		eval $DIR$KERNEL -p ${p[$i]} -k 4 -ncrit ${ncrit_r[$i]} -solver_tol 1e-6 -recursions $i -second_kind | grep "solve " >> $OUT
	done

done

# print out messages
printf ">>> LaplaceBEM speedup test for the 2nd-kind problem completed!\n"