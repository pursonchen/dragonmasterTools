import re
import csv
from collections import deque

sourcedir = 'server.2019-11-19.log.1'
desinationdir = sourcedir+'.csv'

with open(sourcedir, 'r') as f:
    sourceInline = f.readlines()
    for index, line in enumerate(sourceInline):
        time = re.match(r'\[(.*)\] \[', line)
        action = re.search(r'#add_diamond', line)
        if action == None:
            continue
        user = re.search(r'scatter:([1-5a-z]{0,12})', line)
        other = deque(str(re.search(r'scatter:.*', line).group()).split()).pop()
        print(time.group(1))
        print(action.group())
        print(user.group(1))
        print(other)
        
        


