#!/bin/bash

# generate a script file from template.py and an empty input file
# for the next day of challenges

day=0
printf -v py '%02d.py' $day

while [ -e $py ]; do
    printf -v py '%02d.py' "$(( ++day ))"
done

printf -v txt '%02d.txt' $day
touch $txt && cp template.py $py
mv $txt ../input/

if [ $? -eq 0 ]; then
    echo \[SUCCESS\] Generated $py, $txt
else
   echo \[ERROR\] generating $py, $txt
fi
