import sys
import json
import re

d = {}
with open(sys.argv[1]) as file:
    for i in file.readlines():
        path = i.split(' ')[6]
        location = re.search(r'(?<!:)(?<!\/)\/[^?]*', path)[0]

        if d.get(location) is not None:
            d[location] += 1
        else:
            d[location] = 1

d = dict(sorted(d.items(), key=lambda a: int(a[1]))[-10:])

if len(sys.argv) == 3 and sys.argv[2] == '--json':
    json = json.dumps(d)
    print(json)
else:
    for item in d.items():
        print(f'{item[0]}\n{item[1]}\n')
