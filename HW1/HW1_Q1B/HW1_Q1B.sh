#! /usr/bin/env bash
touch sentence.txt
for f1 in `ls partB` ;do
    for f2 in `ls partB/$f1` ;do
        for f3 in `ls partB/$f1/$f2` ;do
        s=partB/$f1/$f2/$f3/*
        cat $s
        echo `cat $s`>>sentence.txt
        done
    done
done