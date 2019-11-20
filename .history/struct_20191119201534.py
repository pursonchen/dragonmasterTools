import re

dir = '20191019154717-players-dump.txt'
user = []
with open(dir,'r') as f:
    sourceInline = f.readlines()
    for line in sourceInline:
        if line == '':
            continue
        print(re.findall(r'(.+?) {', line)[0])
