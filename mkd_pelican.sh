#!/bin/bash 
#===============================================================================
#
#          FILE: mkd_pelican.sh
# 
#         USAGE: ./mkd_pelican.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: 杨秀隆
#  ORGANIZATION: 
#       CREATED: 2014年08月16日 17:13
#===============================================================================

set -o nounset                              # Treat unset variables as an error

for file in $@
do
    filename=`basename $file`
    name=${filename%.*}

    string=""

    if !(sed -n '1,10p' $file | grep -iE "^date:" > /dev/null)
    then
        last_time=`stat -c %y $file | cut -d "." -f 1`
        string="date: "$last_time"   \n"
    fi

    if !(sed -n '1,10p' $file | grep -iE "^title:" > /dev/null)
    then
        string="title: "$name"   \n"$string
    fi
    if [[ $string != "" ]]
    then
        sed -i "1i\\$string" $file
    fi

done
