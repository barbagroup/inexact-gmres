#!/bin/bash

# set the number of threads (using # of physical cores)
export OMP_NUM_THREADS=6

# define the path
DIR="./"

# StokesBEM kernel
kernel="StokesBEM"

# define the result file
OUT='Stokes_sphere_result'

# remove the existing result file
rm -f $OUT

### when recursions=8 (131,072 triangles), not enough memory is available for the optimal setting (ncrit=400), a default ncrit is used (ncrit=64). 

# Fig - 3.8 Convergence: p = 16, 1st-kind, solver_tol = 1e-5:
printf "StokesBEM on a sphere: Convergence\n" >> $OUT
for i in {3..7}
	do eval $DIR$kernel -lazy_eval -p 16 -fixed_p -recursions $i -ncrit 400 | grep -i "error on a sphere" >> $OUT
done

eval $DIR$kernel -lazy_eval -p 16 -fixed_p -recursions 8 | grep -i "error on a sphere" >> $OUT

printf ">>>StokesBEM on a sphere: Convergence test completed!\n"

# Fig - 3.9 Residual History : p = 16, recursions = 6, 1st-kind:
printf "StokesBEM on a sphere: Residual History\n" >> $OUT
printf "fixed-p residual history\n" >> $OUT
eval $DIR$kernel -lazy_eval -recursions 6 -p 16 -fixed_p -ncrit 400 | grep -i fmm_req_p >> $OUT
printf "relaxed-p residual history\n" >> $OUT
eval $DIR$kernel -lazy_eval -recursions 6 -p 16 -ncrit 150 | grep -i fmm_req_p >> $OUT
printf ">>>StokesBEM on a sphere: Residual history test completed!\n"

# Fig - 3.11 Speedup: p = 16, recursions = {5,6,7,8}, 1st-kind:
printf "StokesBEM on a sphere: Speedup\n" >> $OUT
for i in {5..7}
do
    printf "recursions = $i fixed-p\n" >> $OUT
    for j in {1..3}
        do eval $DIR$kernel -lazy_eval -p 16 -recursions $i -fixed_p -ncrit 400 | grep -i "solve " >> $OUT
    done

    printf "recursions = $i relaxed-p\n" >> $OUT
    for j in {1..3}
        do eval $DIR$kernel -lazy_eval -p 16 -recursions $i -ncrit 150 | grep -i "solve " >> $OUT
    done
done
printf ">>>StokesBEM on a sphere: Speedup test completed!\n"
