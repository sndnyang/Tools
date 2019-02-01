source ~/path/bin/activate

count=`python ./some_exp.py | wc -l`

no=0

python ./some_exp.py | while read line
do
    num=`top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1"%"}'`
    if (( num < 80 ))
    then
        echo "cpu use ", $num
        /home/user/python/bin/python train_sync.py $line &
        (( no = no + 1))
        echo NO.$no task begins, $count in total
        echo NO.$no task begins, $count in total > parameter_process.log
        sleep 30
    else
        echo "cpu use ", $num
        echo "sleep"
        sleep 30
    fi
done

