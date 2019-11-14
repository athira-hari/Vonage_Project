#!/bin/bash

if [ -z $1 ]; then

        echo -e "Please input the source directory as an argument. \n ./Cleanup.sh <source direct>"
        exit 0
fi

cd $1
#The bew command removes all he .gz files from your input staging path which are older then 3 days
find . -type f -name "*.gz" -mtime +3 -exec rm -f {} \;
