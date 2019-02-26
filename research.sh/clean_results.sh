

for marker in $*
do
    echo $pid;
    result_d=`find ~/project/results -name "*$marker\_*" -type d`
    echo "path is " $result_d
    if [[ -d "$result_d" ]]
    then
        read -p "do you want to remove the directory ?(y/n)" input
        case $input in
            [yY][eE][sS]|[yY])
                mv "$result_d" ~/tmp_as_deletes
            ;;
        esac
    else
        echo "not find it"
    fi

    tf_d=`find ~/project/runs -name "*$marker*" -type d`
    echo "path is " $tf_d
    if [[ -d "$result_d" ]]
    then
        read -p "do you want to remove the directory ?(y/n)" input
        case $input in
            [yY][eE][sS]|[yY])
                mv "$tf_d" ~/tmp_as_deletes
            ;;
        esac
    else
        echo "not find it"
    fi
done
