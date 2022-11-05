import sys
import json

d = {}
with open(sys.argv[1]) as file:
    for i in file.readlines():
        path = i.split(' ')[6]
        path = path.replace('http://almhuette-raith.at', '')
        if path.find('?'):
            path = path.split('?')[0]

        if d.get(path) is not None:
            d[path] += 1
        else:
            d[path] = 1

d = dict(sorted(d.items(), key=lambda a: int(a[1]))[-10:])

if len(sys.argv) == 3 and sys.argv[2] == '--json':
    json = json.dumps(d)
    print(json)
else:
    for item in d.items():
        print(f'{item[0]}\n{item[1]}\n')
