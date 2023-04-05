#! /usr/bin/env bash
for i in $(ls) ;do
case "$i" in
    *.py)
    python3 ${i} ;;
esac
done