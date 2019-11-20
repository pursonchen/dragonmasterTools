import re
import csv

sourcedir = 'server.2019-11-19.log.1'
desinationdir = sourcedir+'.csv'

with open(sourcedir, 'r') as f:
    sourceInline = f.readlines()
    for index, line in enumerate(sourceInline):
        time = re.match(r'^\[.*\]', line.strip())
        print(str(time.group(1)))
