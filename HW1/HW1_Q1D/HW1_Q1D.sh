#! /usr/bin/env bash

COLOR="Green Red Blue Purple Pink"
for C in  $COLOR ;do
	mkdir -p $C
	touch $C/color_is_${C}
done