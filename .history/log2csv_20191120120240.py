import re
import csv

sourcedir = 'server.2019-11-19.log.1'
desinationdir = sourcedir+'.csv'

with open(sourcedir, 'r') as f:
    sourceInline = f.readlines()
    for index, line in enumerate(sourceInline):
        time = re.sub(r' ', '', line)
        print('read: '+time)
