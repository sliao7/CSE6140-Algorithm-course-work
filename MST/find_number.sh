#!/bin/bash


graphFiles=`ls ./data/ | grep .gr`

for graph in ${graphFiles}
do
    filename=`echo ${graph} | cut -d'.' -f1`
    echo ${graph} ${filename}
    python3 ./src/find_numbers.py ./data/${graph} ./data/${filename}.extra 


done
