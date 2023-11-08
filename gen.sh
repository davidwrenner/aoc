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
if [[ -z "$user_agent" ]]; then
    fatal "user_agent not set"
fi

year=$(date +%Y)
year_src="$year/src"
cd "$year_src" || fatal "repo not configured for $year"

# find the next unsolved puzzle
# this strategy allows for asynchronous completion of puzzles
day=1
printf -v py '%02d.py' $day
while [ -e "$py" ]; do
    printf -v py '%02d.py' "$(( ++day ))"
done
if [ "$day" -gt "$num_days_of_aoc" ]; then
    fatal "day $day > the number of aoc days $num_days_of_aoc"
fi
printf -v txt '%02d.txt' $day

if [[ -f "../input/$txt" ]]; then
    info "found existing input $txt, skipping GET"
else
    curl "https://adventofcode.com/$year/day/$day/input" \
        -X "GET" \
        -H "Cookie: session=$session_cookie" \
        -H "User-Agent: $user_agent" >> "$txt"
    mv "$txt" "../input/$txt"
    info "generated $txt"
fi

if cp "template.py" "$py"; then
    info "generated $py"
else
    fatal "template not found"
fi
