#! /usr/bin/env bash

touch output.txt
i=1
for topic in $(<topics.txt) ;do
    echo ${i}-${topic}>>output.txt
    ((i++))
done