#!/bin/bash
# generate input and src files for the next unsolved day

num_days_of_aoc=25

source "config"
if [[ -z "$session_cookie" ]]; then
    echo "[FATAL] session_cookie not set"; exit 1
fi

year=$(date +%Y)
year_src="$year/src"
cd "$year_src" || { echo "[FATAL] not configured for $year"; exit 2; }

# find the next unsolved puzzle
day=1
printf -v py '%02d.py' $day
while [ -e "$py" ]; do
    printf -v py '%02d.py' "$(( ++day ))"
done
if [ "$day" -gt "$num_days_of_aoc" ]; then
    echo "[FATAL] day $day geq the number of aoc days $num_days_of_aoc"; exit 3
fi
printf -v txt '%02d.txt' $day

curl "https://adventofcode.com/$year/day/$day/input" \
    -X "GET" \
    -H "Cookie: session=$session_cookie" > "$txt"
if [[ ! -f "$txt" ]]; then
    echo "[FATAL] failed to curl input"; exit 4
fi

if mv "$txt" "../input/" && cp "template.py" "$py"; then
    echo "[INFO] generated $py and $txt"
else
    echo "[FATAL] something happened while generating $py and $txt"; exit 5
fi
