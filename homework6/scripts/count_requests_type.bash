awk '{print substr($6, 2)}' $1 | sort | uniq -c | sort -nk1 | awk '{print $2, $1}'
