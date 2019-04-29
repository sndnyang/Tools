
para_file="para.ini"
out_file="stdout"

if [[ $# == 0 ]]
then
    echo "need to specify the script"
fi

if [[ $# > 1 ]]
then
    para_file=$2
fi
if [[ $# > 2 ]]
then
    out_file=$3
    echo > $3
fi

marker=`date +%m%d%H%M%S`
count=`python ./some_exp.py --file=$para_file | wc -l`
echo $count

echo "$para_file" > logs/process_$marker_$$.log

no=0

python ./some_exp.py --file=$para_file | while read line
do
    n=-1
    while (( n < 0 ))
    do
        nvidia-smi > ~/nv.txt 
        min=100
        array=`grep Default ~/nv.txt | tail -n 7 | cut -d "|" -f 4 | cut -f 7 | cut -d "%" -f 1`
        c=1
        n=-1

        for j in $array
        do
            if ((j < min))
            then
                num=`grep " C " ~/nv.txt | grep " $c "| wc -l`
                mem=`grep " C " ~/nv.txt | grep " $c " | awk 'BEGIN {num=0} {if ($0 ~ / C /) {gsub(/MiB/, "", $0); num+=$6} } END {print num}'`
                echo $c "uses memory" $mem "with" $num processes

                if (( num > 4 || mem > 7000 || $j > 80 ))
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
            sleep 30
        fi
    done
    
    if (( n > -1 ))
    then
        echo "min gpu use ", $min, "at", $n
        echo "$line"
        echo python $1 --gpu-id=$n $line
        echo python $1 --gpu-id=$n $line >> logs/process_$marker_$$.log
        echo python $1 --gpu-id=$n $line >> logs/process_$marker_$$.sh
        if [[ $# > 2 ]]
        then
            ~/software/miniconda3/envs/dllib3/bin/python $1 --gpu-id=$n $line >> $2 &
            echo ""
        else
            ~/software/miniconda3/envs/dllib3/bin/python $1 --gpu-id=$n $line &
            echo ""
        fi
        (( no = no + 1))
        echo NO.$no task begins, $count in total
        echo NO.$no task begins, $count in total >> logs/process_$marker_$$.log
        sleep 50
    fi
done

