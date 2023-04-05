#! /usr/bin/env bash

for i in `ls ./partA`; do
    #creat directory for each py file
    mkdir -p ${i//.py}
    #move files into the directory
    mv ./partA/${i} ${i//.py}

    start=$(date +%s)
    python3 ${i//.py}/${i}
    end=$(date +%s)
    timee=$(($end-$start))
    touch ${i//.py}/time${i//[^0-9]/}
    echo ${timee} >>${i//.py}/time${i//[^0-9]/}
    touch Alltime
    echo ${timee}>> Alltime
done