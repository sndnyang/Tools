#!/bin/sh
echo $1

for f in `echo $PATH | sed 's/ /;/g;s/:/ /g' `
do
    dir=`echo $f | sed 's/;/ /g'`
    echo "$dir"
    ls "$dir"/* 2>/dev/null | grep $1
done
