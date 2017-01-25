#!/bin/bash

result_file=$1

if [[ -n "$result_file" ]]
then
    eval python EthrocyteConvergence.py $result_file
    eval python EthrocyteSingleCellIterations.py $result_file
    eval python EthrocyteMultipleCellSpeedup.py $result_file
    eval python EthrocyteMultipleCellIterations.py $result_file
else
    echo "Argument error, the format should be [./bash_script.sh] [result_file]"
fi