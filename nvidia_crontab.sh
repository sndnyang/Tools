#!/bin/bash
receiver=

nvidia-smi > ~/nv.txt

cat ~/nv.txt

grep -nE "^\|    " ~/nv.txt | while read line
do
    gpuid=`echo $line | cut -d\  -f 3`
    # echo $gpuid
    process=`ps aux | grep xyang | grep -w $gpuid | grep -v "grep -w"`
    if [ ! -z "$process" ]
    then
        echo "$gpuid" process is using GPU
        echo "$process"
        echo "$process" | mail -s "Processes take GPU" "$receiver"
    fi
done

