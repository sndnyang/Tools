ps ux | grep python | grep -v debug.py | grep -v notebook | grep -v grep | grep -v tensorboard > ~/found_hidden_gpu_process.txt

nvidia-smi > ~/nv.txt

cat ~/found_hidden_gpu_process.txt | while read line
do
    ps_id=`echo $line | awk '{print $2}'`
    if grep $ps_id ~/nv.txt > /tmp/null
    then 
        echo $line
        echo id, $ps_id, match
        echo
    else
        echo $line
        echo id, $ps_id, miss
        echo 
    fi
done

