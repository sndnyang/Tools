

for marker in $*
do
    echo $pid;
    result_d=`find ~/project/results -name "*$marker\_*" -type d`
    echo "path is " $result_d
    read -p "do you want to remove the directory ?(y/n)" input
    case $input in
        [yY][eE][sS]|[yY])
            mv "$result_d" ~/tmp_as_deletes
        ;;
    esac

    tf_d=`find ~/project/runs -name "*$marker\_*" -type d`
    echo "path is " $tf_d
    read -p "do you want to remove the directory ?(y/n)" input
    case $input in
        [yY][eE][sS]|[yY])
            mv "$tf_d" ~/tmp_as_deletes
        ;;
    esac
done