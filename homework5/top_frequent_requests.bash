awk '{print $7}' access.log | cut -d. -f2 | cut -d/ -f2- | cut -d? -f1 | sort | uniq -c | sort -nk1 | tail | awk '{print "/" $2 "\n" $1 }'
