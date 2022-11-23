import sys
import json

d = {}
with open(sys.argv[1]) as file:
    for i in file.readlines():
        method = i.split(' ')[5][1:]

        if d.get(method) is not None:
            d[method] += 1
        else:
            d[method] = 1
if len(sys.argv) == 3 and sys.argv[2] == '--json':
    json = json.dumps(d)
    print(json)
else:
    for item in sorted(d.items(), key=lambda a: int(a[1])):
        print(item[0], item[1])
