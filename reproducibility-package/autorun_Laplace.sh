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

# define KERNEL name
KERNEL="LaplaceBEM"

# define the result filename
OUT='Laplace_result'

# remove the existing result file
rm -f $OUT

########## Convergence: 1st-kind problem: ##########

# fixed-p, tight parameters: p = 20, k = 13, tol = 1e-10, ncrit = 400
printf "LaplaceBEM Convergence - 1st-kind:\n" >> $OUT
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
read ncrit[{6..8}] <<< $(echo 100 100 200)
for i in {6..8}; do
	eval $DIR$KERNEL -p ${p[$i]} -k 4 -ncrit ${ncrit[$i]} -solver_tol 1e-6 -recursions $i | grep 'external phi' >> $OUT
done

# print out messages
printf ">>>LaplaceBEM convergence test for the 1st-kind problem completed!\n"


########## Convergence: 2nd-kind problem: ##########

# fixed-p, tight parameters: p = 20, k = 13, tol = 1e-10, ncrit = 400
printf "LaplaceBEM Convergence - 2nd-kind:\n" >> $OUT
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
read ncrit[{6..8}] <<< $(echo 300 300 300)
for i in {6..8}; do
	eval $DIR$KERNEL -p ${p[$i]} -k 4 -ncrit ${ncrit[$i]} -solver_tol 1e-6 -recursions $i -second_kind | grep 'external phi' >> $OUT
done

# print out messages
printf ">>>LaplaceBEM convergence test for the 2nd-kind problem completed!\n"



# comment out below
: <<'END'

# Fig-5 Convergence: 2nd-kind problem: p = 12, solver_tol = 1e-6, no relaxation
printf "LaplaceBEM Convergence - 2nd-kind:\n" >> $OUT
for i in {3..7}
do eval $DIR$KERNEL -p 12 -fixed_p -k 4 -ncrit 400 -solver_tol 1e-6 -recursions $i -second_kind | grep -i relative >> $OUT
done
printf ">>>LaplaceBEM convergence test for the 2nd-kind problem completed!\n"

# Fig-6 Residual & required-p: 1st-kind problem: N = 32768, solver_tol = 1e-6, with relaxation
printf "LaplaceBEM Residual History and required-p:\n" >> $OUT
printf "case 1:\n" >> $OUT
eval $DIR$KERNEL -p 8 -k 4 -recursions 7 -ncrit 150 -solver_tol 1e-6 | grep -i fmm_req_p >> $OUT
printf "case 2:\n" >> $OUT
eval $DIR$KERNEL -p 12 -k 4 -recursions 7 -ncrit 150 -solver_tol 1e-6 | grep -i fmm_req_p >> $OUT
printf ">>>LaplaceBEM residual history test completed!\n"

# Fig-7 Table-1 Speedup 1st-kind:
# set optimal ncrits
read ncrit_r_set[{5..8}] <<< $(echo 300 175 200 200)
printf "LaplaceBEM speedup test - 1st-kind:\n" >> $OUT
for i in {5..8}
do
	printf "recursions = $i fixed-p 1st-kind\n" >> $OUT
	for j in {1..3}
	do eval $DIR$KERNEL -p 10 -k 4 -recursions $i -ncrit 400 -fixed_p -solver_tol 1e-6 | grep -i "solve " >> $OUT
	done

	printf "recursions = $i relaxed 1st-kind\n" >> $OUT
	for j in {1..3}
	do eval $DIR$KERNEL -p 10 -k 4 -recursions $i -ncrit ${ncrit_r_set[$i]} -solver_tol 1e-6 | grep -i "solve " >> $OUT
	done
done
printf ">>>LaplaceBEM speedup test for the 1st-kind problem completed!\n"

# Fig-7 Table-2 Speedup 2nd-kind:
# set optimal ncrits
read ncrit_r_set[{5..8}] <<< $(echo 300 300 200 200)
printf "LaplaceBEM speedup test - 2nd-kind:\n" >> $OUT
for i in {5..8}
do
	printf "recursions = $i fixed-p 2nd-kind\n" >> $OUT
	for j in {1..3}
	do eval $DIR$KERNEL -p 10 -k 4 -recursions $i -ncrit 400 -fixed_p -second_kind -solver_tol 1e-6 | grep -i "solve " >> $OUT
	done

	printf "recursions = $i relaxed 2nd-kind\n" >> $OUT
	for j in {1..3}
	do eval $DIR$KERNEL -p 10 -k 4 -recursions $i -ncrit ${ncrit_r_set[$i]} -second_kind -solver_tol 1e-6 | grep -i "solve " >> $OUT
	done
done
printf ">>>LaplaceBEM speedup test for the 2nd-kind problem completed!\n"

# Fig-8 Table-3 Speedup with increasing value of p_intial, N = 32768, change tolerance to fix iteration count at 10, p = {5, 8, 10, 12, 15}:
printf "LaplaceBEM speedup test with an increasing p_intial:\n" >> $OUT
    # define the p_set, its corresponding optimal ncrit and solver's tolerance
read p_set[{1..5}] <<< $(echo 5 8 10 12 15)
read ncrit_f_set[{1..5}] <<< $(echo 100 400 400 600 600)
read ncrit_r_set[{1..5}] <<< $(echo 100 100 150 150 150)
read tol_f_set[{1..5}] <<< $(echo 5.0e-5 3.3e-6 2.3e-6 2.0e-6 1.5e-6)
read tol_r_set[{1..5}] <<< $(echo 4.0e-5 5.0e-6 3.3e-6 2.0e-6 1.9e-6)

for i in {1..5}
do
    printf "p=${p_set[$i]}, fixed-p 1st-kind:\n" >> $OUT
    for j in {1..3}
    do eval $DIR$KERNEL -p ${p_set[$i]} -recursions 7 -ncrit ${ncrit_f_set[$i]} -fixed_p -solver_tol ${tol_f_set[$i]} | grep -i "solve " >> $OUT
    done

    printf "p=${p_set[$i]}, relaxed-p 1st-kind:\n" >> $OUT
    for j in {1..3}
    do eval $DIR$KERNEL -p ${p_set[$i]} -recursions 7 -ncrit ${ncrit_r_set[$i]} -solver_tol ${tol_r_set[$i]} | grep -i "solve " >> $OUT
    done
done
printf ">>>LaplaceBEM speedup test with an increasing p_initial completed!\n"

# Fig-9 Table-4 Speedup with various tolerances, N = 8192, p = 10
printf "LaplaceBEM speedup test with various tolerances:\n" >> $OUT
read ncrit_f_set[{1..7}] <<< $(echo 400 400 400 400 400 400 400)
read ncrit_r_set[{1..7}] <<< $(echo 400 300 300 300 300 300 300)
read tol_set[{1..7}] <<< $(echo 1e-5 1e-6 1e-7 1e-8 1e-9 1e-10 1e-11)

for i in {1..7}
do
	printf "tol=${tol_set[$i]}, fixed-p:\n" >> $OUT
	for j in {1..3}
	do eval $DIR$KERNEL -p 10 -recursions 6 -ncrit ${ncrit_f_set[$i]} -fixed_p -solver_tol ${tol_set[$i]} | grep -i "solve " >> $OUT
	done

	printf "tol=${tol_set[$i]}, relaxed-p:\n" >> $OUT
	for j in {1..3}
	do eval $DIR$KERNEL -p 10 -recursions 6 -ncrit ${ncrit_r_set[$i]} -solver_tol ${tol_set[$i]} | grep -i "solve " >> $OUT
	done
done
printf ">>>LaplaceBEM speedup test with various tolerances completed!\n"

END