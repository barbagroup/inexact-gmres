#!/bin/bash

result_file=$1

if [[ -n "$result_file" ]]
then
    eval python LaplaceConvergence.py $result_file
    eval python LaplaceResidualIterations.py $result_file
    eval python LaplaceSpeedup.py $result_file
else
    echo "Argument error, the format should be [./bash_script.sh] [result_file]"
fi

