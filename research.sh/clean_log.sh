
for d in *
do
    if [ -d "$d" ]
    then
        echo "watch into " $d

        if ls "$d"/*.npy > /dev/null 2>&1
        then
            if ls "$d"/*.png > /dev/null 2>&1
            then
                echo "there are npy files and figures, keep it"
            else
                echo "there are npy files, but no pictures, check it"
            fi
        else
            echo "There is no npy files, remove it"
            rm -fr "$d"
        fi
    fi
done
