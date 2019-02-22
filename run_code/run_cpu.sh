source ~/software/dllib/bin/activate

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

no=0


python ./some_exp.py --file=$1 | while read line
do
    num=100
    while (( num > 60 ))
    do
        num=`top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}' | cut -d "." -f 1`
        if (( num < 60 ))
        then
            break
        fi
        echo "cpu use ", $num
        echo "sleep"
        sleep 30
    done

    if (( num < 60 ))
    then
        echo "cpu use ", $num
        echo $line
        if [[ $# > 1 ]]
        then
            ~/software/dllib/bin/python train_syn.py $line >> $2 &
        else
            ~/software/dllib/bin/python train_syn.py $line &
        fi
        (( no = no + 1))
        echo NO.$no task begins, $count in total
        echo NO.$no task begins, $count in total > parameter_process.log
        sleep 5
    fi
done
