from os import getcwd
d = {}
with open(getcwd() + '/access.log') as file:
    for i in file.readlines():
        method = i.split(' ')[5][1:]

        if d.get(method) is not None:
            d[method] += 1
        else:
            d[method] = 1

for item in sorted(d.items(), key=lambda a: a[1], reverse=True):
    print(item[0], item[1])

