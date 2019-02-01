source ~/path/bin/activate

python ./some_exp.py | while read line
do
    num=`top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1"%"}'`
    if (( num < 80 ))
    then
        echo "cpu use ", $num
        /home/user/python/bin/python train_sync.py $line &
        sleep 30
    else
        echo "cpu use ", $num
        echo "sleep"
        sleep 30
    fi
done

