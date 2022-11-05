awk '{print $7}' $1 | sed 's#http://almhuette-raith.at##' | cut -d? -f1 | sort | uniq -c | sort -nk1 | tail | awk '{print $2 "\n" $1 "\n"}'
