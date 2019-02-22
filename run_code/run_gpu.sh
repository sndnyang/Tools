source ~/software/venv/dllib3/bin/activate

para_file="para.ini"
out_file="stdout"

echo $#

if [[ $# > 0 ]]
then
    para_file=$1
fi
if [[ $# > 1 ]]
then
    out_file=$2
    echo > $2
fi

count=`python ./some_exp.py --file=$1 | wc -l`
echo $count

no=0
python --version

python ./some_exp.py --file=$1 | while read line
do
    n=-1
    while (( n < 0 ))
    do
        nvidia-smi > ~/nv.txt 
        min=100
        array=`grep 12189 ~/nv.txt | head -n 3 | cut -d "|" -f 4 | cut -f 7 | cut -d "%" -f 1`
        c=0
        n=-1

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
            if (( n < 0 ))
            then
                echo "sleep"
                sleep 30
            fi
        done
    done
    
    if (( n > -1 ))
    then
        echo "min gpu use ", $min, "at", $n
        echo "$line"
        if [[ $# > 1 ]]
        then
            ~/software/miniconda3/envs/theano27/bin/python train_mnist_sup.py --gpu_id=$n $line >> $2 &
        else
            ~/software/miniconda3/envs/theano27/bin/python train_mnist_sup.py --gpu_id=$n $line &
        fi
        (( no = no + 1))
        echo NO.$no task begins, $count in total
        echo NO.$no task begins, $count in total > parameter_process.log
        sleep 50
    fi
done

