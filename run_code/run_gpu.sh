#!/usr/bin/env bash

para_file="para.ini"
out_file="stdout"
gpu_num=5

if [[ $# == 0 ]]
then
    echo "need to specify the script"
fi

if [[ $# > 1 ]]
then
    # given the hyperparameters to tune and their search space(values)
    para_file=$2
fi
if [[ $# > 2 ]]
then
    gpu_num=$3
fi
if [[ $# > 3 ]]
then
    out_file=$4
    echo > $4
fi

marker=`date +%m%d%H%M%S`
count=`python ~/bin/some_exp.py --file=$para_file | wc -l`
echo $count

echo "$para_file" > logs/process_$marker_$$.log

no=0

python ~/bin/some_exp.py --file=$para_file | while read line
do
    n=-1
    while (( n < 0 ))
    do
        # get the status of GPUs
        nvidia-smi > ~/nv1.txt 
        min=100
        # only use some GPUs, since they may are different GPUs (XP\1080\RTX)
        array=`grep Default ~/nv1.txt | head -n 8 | tail -n $gpu_num | cut -d "|" -f 4 | cut -f 7 | cut -d "%" -f 1`
        (( c = 8 - $gpu_num ))
        n=-1
        cat ~/nv1.txt | nvidia-htop.py 2>/dev/null | tail -n +35 | head -n -2 > ~/nv.txt

        # for each GPU
        for j in $array
        do
            if ((j < min))
            then
                # how many process are using it
                num=`cat ~/nv.txt | grep "|    $c " | wc -l`
                # how many memery
                mem=`cat ~/nv.txt | grep "|    $c " | awk 'BEGIN {num=0} {if ($0 ~ /MiB/) {gsub(/MiB/, "", $5); num+=$5} } END {print num}'`
                # cat ~/nv.txt | grep "  $c " | awk '{print $8 }' | awk -F ":" '{print $1$2$3}' | awk '{a=30;t="";} { if ($0 < a) {print $0; t=1;}}'
                # cost time
                tim=`cat ~/nv.txt | grep "|    $c " | awk '{print $8 }' | awk -F ":" '{print $1$2$3}' | awk '{a=30;t="";} { if ($0 < a) {print $0; t=1;}}{print t}'`

                echo $c "uses memory" $mem "with" $num processes, load $j, tim pass $tim

                if [[ ! -z $tim ]]
                then
                    (( c = c+1 ))
                    continue
                fi

                # if the GPU is busy, load/util is > 65%
                if (( num > 1 || $j > 65 ))
                then
                    (( c = c+1 ))
                    continue
                fi

                # if the GPU is busy, 10000MB of RTX are using(Remaining is 10000MB)
                if (( c < 3 && mem > 10000 )) 
                then
                    (( c = c+1 ))
                    continue
                fi
                # if the GPU is busy, 1000MB of XP are using(Remaining is 10000MB)
                if (( c > 2 && mem > 1000 )) 
                then
                    (( c = c+1 ))
                    continue
                fi
                (( min = j ))
                ((n = c))
            fi

            (( c = c+1 ))
        done
        if (( n < 0 ))
        then
            echo "sleep"
            sleep 60
        fi
    done
    
    if (( n > -1 ))
    then
        echo "min gpu use ", $min, "at", $n
        echo "$line"
        echo python $1 --gpu-id=$n $line
        echo python $1 --gpu-id=$n $line >> logs/process_$marker_$$.log
        echo python $1 --gpu-id=$n $line >> logs/process_$marker_$$.sh
        if [[ $# > 3 ]]
        then
            ~/conda/envs/dllib3/bin/python $1 --gpu-id=$n $line >> $2 &
            echo ""
        else
            ~/conda/envs/dllib3/bin/python $1 --gpu-id=$n $line &
            echo ""
        fi
        (( no = no + 1))
        echo NO.$no task begins, $count in total
        echo NO.$no task begins, $count in total >> logs/process_$marker_$$.log
        sleep 30
    fi
done

