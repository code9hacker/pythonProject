import os
from os.path import isfile


def solve():
    queue = ["/home/gaurav/Downloads/cfg"]
    while len(queue) > 0:
        dir = queue.pop()
        dirlist = os.listdir(dir)
        for f in dirlist:
            path = dir + '/' + f
            if isfile(path):
                print(f)
            else:
                queue.append(path)

solve()