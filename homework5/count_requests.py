from os import getcwd

with open(getcwd() + '/access.log') as file:
    print(len(file.readlines()))
