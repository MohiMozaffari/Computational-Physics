#! /usr/bin/env bash
#A:
split -n 100 data.txt
#B:
for i in $(ls x*) ; do
    mv $i ${i}.txt
    mkdir -p $i
    mv ${i}.txt $i
done