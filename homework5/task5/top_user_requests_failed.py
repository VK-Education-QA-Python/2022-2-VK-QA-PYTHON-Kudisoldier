import sys
import re
import json

d = {}
with open(sys.argv[1]) as file:
    for i in file.readlines():
        request = i.split(' ')
        if re.match(r'5\d\d', request[8]):
            if d.get(request[0]) is not None:
                d[request[0]] += 1
            else:
                d[request[0]] = 1

d = dict(sorted(d.items(), key=lambda a: int(a[1]))[-5:])

if len(sys.argv) == 3 and sys.argv[2] == '--json':
    json = json.dumps(d)
    print(json)
else:
    for item in d.items():
        print(f'{item[0]}\n{item[1]}\n')
