#!/bin/bash
# generate input and src files for the next unsolved day

set -euo pipefail
num_days_of_aoc=25

log_info () {
    echo "[INFO] $1"
}
log_fatal () {
    echo "[FATAL] $1"
    exit 1
}

source "config"
if [[ -n "$session_cookie" ]]; then
    log_info "session_cookie found"
fi
if [[ -n "$user_agent" ]]; then
    log_info "user_agent found"
fi
if [[ -n "$src_type" ]]; then
    log_info "src_type found"
fi

template="template.$src_type"
year=$(date +%Y)
year_src="$year/src"
cd "$year_src"

if [[ -f "$template" ]]; then
    log_info "$template found"
fi

# find the next unsolved puzzle
# this strategy allows for asynchronous completion of puzzles
day=1
printf -v solution "%02d.$src_type" $day
while [ -e "$solution" ]; do
    printf -v solution "%02d.$src_type" "$(( ++day ))"
done
if [[ "$day" -gt "$num_days_of_aoc" ]]; then
    log_fatal "day $day > the number of aoc days $num_days_of_aoc"
fi
printf -v txt '%02d.txt' $day

if [[ -f "../input/$txt" ]]; then
    log_info "cached input $txt found"
else
    curl "https://adventofcode.com/$year/day/$day/input" \
        -X "GET" \
        -H "Cookie: session=$session_cookie" \
        -H "User-Agent: $user_agent" >> "$txt"
    mv "$txt" "../input/$txt"
    log_info "generated $txt"
fi

cp "$template" "$solution"
log_info "generated $solution"
log_info "SUCCESS"