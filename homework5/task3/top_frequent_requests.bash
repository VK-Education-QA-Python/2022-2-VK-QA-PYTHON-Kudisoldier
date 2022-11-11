awk '{print $7}' $1 | perl -nle 'print $& while m{(?<!:)(?<!\/)\/[^?]*}g' | sort | uniq -c | sort -nk1 | tail | awk '{print $2 "\n" $1 "\n"}'
