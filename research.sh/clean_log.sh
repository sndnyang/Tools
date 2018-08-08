
for d in *
do
    if [ -d "$d" ]
    then
        echo "watch into " $d

        if [[ ! "$d" =~ ^[0-9]+$ ]]
        then
            echo "it contains chars, keep it"
            continue
        fi

        if find "$d" -name "*.npy" > /dev/null 2>&1
        then
            if find "$d" -name "*.png" > /dev/null 2>&1
            then
                echo "there are npy files and figures, keep it"
            else
                echo "there are npy files, but no pictures, check it"
            fi
        else
            echo "There is no npy files "
            read -p "do you want to remove the directory ?(y/n)" input
            case $input in
                    [yY][eE][sS]|[yY])
                        rm -fr "$d"
                    ;;
            esac

        fi
    fi
done
