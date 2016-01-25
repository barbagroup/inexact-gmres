#!/bin/bash

result_file=$1

if [[ -n "$result_file" ]]
then
    eval python StokesConvergence.py $result_file
    eval python StokesResidualHistory.py $result_file
    eval python StokesSpeedupRelaxation.py $result_file
    eval python StokesSolveBreakdown.py $result_file
else
    echo "Argument error, the format should be [./bash_script.sh] [result_file]"
fi