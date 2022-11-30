awk 'match($9, /5[[:digit:]][[:digit:]]/){print $1}' $1 | sort | uniq -c | sort -nk1 | tail -n5 | awk '{print $2 "\n" $1}'
