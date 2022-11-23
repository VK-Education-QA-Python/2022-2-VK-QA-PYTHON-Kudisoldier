awk 'match($9, /4[[:digit:]][[:digit:]]/){print $1, $7, $9, $10}' $1 | sort -nk4 | tail -n5 | awk '{print $2 "\n" $3 "\n" $4 "\n" $1 "\n"}'
