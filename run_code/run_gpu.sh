source ~/software/dllib3/bin/activate

python ./some_exp.py | while read line
do
    array=`grep 12189 ~/nv.txt | head -n 3 | cut -d "|" -f 4 | cut -f 7 | cut -d "%" -f 1`
    min=100
    n=-1
    c=0
    for j in $array
    do
        if ((j < min))
        then
            num=`grep " C " ~/nv.txt | grep " $c "| wc -l`
            mem=`grep " C " ~/nv.txt | grep " $c " | awk 'BEGIN {num=0} {if ($0 ~ / C /) {gsub(/MiB/, "", $0); num+=$6} } END {print num}'`
            echo $c "uses memory" $mem "with" $num processes

            if (( num > 3 || mem > 10000 ))
            then
                (( c = c+1 ))
                continue
            fi
            (( min = j ))
            ((n = c))
        fi

        (( c = c+1 ))
    done
    
    if (( n > -1 ))
    then
        echo "min gpu use ", $min, "at", $n
        echo "$line"
        /home/user/python/bin/python train_sync.py --gpu-id=$n $line &
        sleep 25
    else
        echo "sleep"
        sleep 30
    fi
done

