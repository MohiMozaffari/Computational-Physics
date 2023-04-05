#! /usr/bin/env bash
while true ;do
    read -p "Pleas input your name: " NAME
    read -p "Is ${NAME} correct?" COR
    case $COR in
        [Yy]*)
            break
    esac
done