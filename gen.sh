#!/bin/bash
# generate input and src files for the next unsolved day

num_days_of_aoc=25

info () {
    echo "[INFO] $1"
}
fatal () {
    echo "[FATAL] $1"
    exit 1
}

source "config"
if [[ -z "$session_cookie" ]]; then
    fatal "session_cookie not set"
fi

year=$(date +%Y)
year_src="$year/src"
cd "$year_src" || fatal "not configured for $year"

# find the next unsolved puzzle
day=1
printf -v py '%02d.py' $day
while [ -e "$py" ]; do
    printf -v py '%02d.py' "$(( ++day ))"
done
if [ "$day" -gt "$num_days_of_aoc" ]; then
    fatal "day $day geq the number of aoc days $num_days_of_aoc"
fi
printf -v txt '%02d.txt' $day

curl "https://adventofcode.com/$year/day/$day/input" \
    -X "GET" \
    -H "Cookie: session=$session_cookie" > "$txt"
if [[ ! -f "$txt" ]]; then
    fatal "failed to curl input"
fi

if mv "$txt" "../input/" && cp "template.py" "$py"; then
    info "generated $py and $txt"
else
    fatal "something happened while generating $py and $txt"
fi
