import sys
import json

with open(sys.argv[1]) as file:
    requests_count = len(file.readlines())

    if len(sys.argv) == 3 and sys.argv[2] == '--json':
        d = {'requests_count': requests_count}
        json = json.dumps(d)
        print(json)
    else:
        print(requests_count)
