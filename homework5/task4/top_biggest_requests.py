import sys
import re
import json

requests = []
with open(sys.argv[1]) as file:
    for i in file.readlines():
        request = i.split(' ')
        if re.match(r'4\d\d', request[8]):
            requests.append([request[0], request[6], request[8], request[9]])

requests = sorted(requests, key=lambda a: int(a[3]))[-5:]

if len(sys.argv) == 3 and sys.argv[2] == '--json':
    json = json.dumps(requests)
    print(json)
else:
    for item in requests:
        print(f'{item[1]}\n{item[2]}\n{item[3]}\n{item[0]}\n')
