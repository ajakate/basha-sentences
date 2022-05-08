from IPython import embed
import os

def dedupe_list(my_list):
    res = []
    for i in my_list:
        if i not in res:
            res.append(i)
    return res

def add_newline(l):
    return l + "\n"

files = os.listdir('./speechling')

for f in files:
    start = []
    with open(f'speechling/{f}') as fi:
        for line in fi:
            start.append(line.split("\t")[0])
    start = dedupe_list(start)
    start = [ add_newline(l) for l in start ]
    with open(f'speechling/{f}', 'w') as f:
        f.writelines(start)
