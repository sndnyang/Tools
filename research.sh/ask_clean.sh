
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

        if ls "$d"/*.npy > /dev/null 2>&1
        then
            if ls "$d"/*.png > /dev/null 2>&1
            then
                echo "there are npy files and figures, check it"
                firstfile=`ls "$d"/*.png | sort | head -n 1`
                eog "$firstfile"
            else
                echo "there are npy files, but no pictures, check it"
                ls "$d"
            fi
            read -p "do you want to remove the directory ?(y/n)" input
            case $input in
                    [yY][eE][sS]|[yY])
                        rm -fr "$d"
                    ;;
            esac
        else
            echo "There is no npy files, remove it"
            rm -fr "$d"
        fi
    fi
done
