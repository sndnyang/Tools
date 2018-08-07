#!/bin/bash
receiver=

while true
do
    cp ~/monitor_process.txt monitor.back
    # echo "" > ~/monitor_title.txt
    touch monitor_title.new
    touch monitor_process.new
    while read line
    do
        process=`ps aux | grep -w $line | grep -v grep`
        if [ -z "$process" ]
        then
            grep $line ~/monitor_title.txt | mail -s "Process done" "$receiver"
        else
            echo $line is working
            text=`echo $process | xargs python -c "import sys;print(' '.join(sys.argv[11:]));"`
            echo $line $text
            echo $line $text >> monitor_title.new
            echo $line >> monitor_process.new
        fi
    done < ~/monitor_process.txt
    mv monitor_process.new ~/monitor_process.txt
    mv monitor_title.new ~/monitor_title.txt
    sleep 60
done
