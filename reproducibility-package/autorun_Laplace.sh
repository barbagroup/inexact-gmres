#!/bin/bash

# set the number of threads (using # of physical cores)
export OMP_NUM_THREADS=6

# define the path
DIR="./"

# LaplaceBEM kernel
kernel="LaplaceBEM"

# define the result file
OUT='Laplace_result'

# remove the existing result file
rm -f $OUT

# Fig-5 Convergence: 1st-kind problem: p = 10, solver_tol = 1e-6, no relaxation 
printf "LaplaceBEM Convergence - 1st-kind:\n" >> $OUT
for i in {3..7}
do eval $DIR$kernel -p 10 -fixed_p -solver_tol 1e-6 -recursions $i | grep -i relative >> $OUT
done
printf ">>>LaplaceBEM convergence test for the 1st-kind problem completed!\n"

# Fig-5 Convergence: 2nd-kind problem: p = 10, solver_tol = 1e-6, no relaxation
printf "LaplaceBEM Convergence - 2nd-kind:\n" >> $OUT
for i in {3..7}
do eval $DIR$kernel -p 10 -fixed_p -solver_tol 1e-6 -recursions $i -second_kind | grep -i relative >> $OUT
done
printf ">>>LaplaceBEM convergence test for the 2nd-kind problem completed!\n"

# Fig-6 Residual & required-p: 1st-kind problem: N = 32768, solver_tol = 1e-5, with relaxation
printf "LaplaceBEM Residual History and required-p:\n" >> $OUT
eval $DIR$kerne -p 8 -recursions 7 -ncrit 150 -solver_tol 1e-6 | grep -i fmm_req_p >> $OUT
printf ">>>LaplaceBEM residual history test completed!\n"

# Fig-7 Table-1 Speedup 1st-kind:
printf "LaplaceBEM speedup test - 1st-kind:\n" >> $OUT
for i in {5..8}
do
	printf "recursions = $i fixed-p 1st-kind\n" >> $OUT
	for j in {1..3}
	do eval $DIR$kernel -p 8 -recursions $i -ncrit 400 -fixed_p | grep -i "solve " >> $OUT
	done

	printf "recursions = $i relaxed 1st-kind\n" >> $OUT
	for j in {1..3}
	do eval $DIR$kernel -p 8 -recursions $i -ncrit 150 | grep -i "solve " >> $OUT
	done
done
printf ">>>LaplaceBEM speedup test for the 1st-kind problem completed!\n"

# Fig-7 Table-2 Speedup 2nd-kind:
printf "LaplaceBEM speedup test - 2nd-kind:\n" >> $OUT
for i in {5..8}
do
	printf "recursions = $i fixed-p 2nd-kind\n" >> $OUT
	for j in {1..3}
	do eval $DIR$kernel -p 8 -recursions $i -ncrit 400 -fixed_p -second_kind | grep -i "solve " >> $OUT
	done

	printf "recursions = $i relaxed 2nd-kind\n" >> $OUT
	for j in {1..3}
	do eval $DIR$kernel -p 8 -recursions $i -ncrit 150 -second_kind | grep -i "solve " >> $OUT
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
    do eval $DIR$kernel -p ${p_set[$i]} -recursions 7 -ncrit ${ncrit_f_set[$i]} -fixed_p -solver_tol ${tol_f_set[$i]} | grep -i "solve " >> $OUT
    done

    printf "p=${p_set[$i]}, relaxed-p 1st-kind:\n" >> $OUT
    for j in {1..3}
    do eval $DIR$kernel -p ${p_set[$i]} -recursions 7 -ncrit ${ncrit_r_set[$i]} -solver_tol ${tol_r_set[$i]} | grep -i "solve " >> $OUT
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
	do eval $DIR$kernel -p 10 -recursions 6 -ncrit ${ncrit_f_set[$i]} -fixed_p -solver_tol ${tol_set[$i]} | grep -i "solve " >> $OUT
	done

	printf "tol=${tol_set[$i]}, relaxed-p:\n" >> $OUT
	for j in {1..3}
	do eval $DIR$kernel -p 10 -recursions 6 -ncrit ${ncrit_r_set[$i]} -solver_tol ${tol_set[$i]} | grep -i "solve " >> $OUT
	done
done
printf ">>>LaplaceBEM speedup test with various tolerances completed!\n"