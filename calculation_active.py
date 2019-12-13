import re
import csv
from collections import deque
import sys

sourcedir = './server.2019-11-19.log.1'  if len(sys.argv) == 1 else sys.argv[1]
print(sourcedir)
desinationdir = sourcedir+'.active.csv'

# 读取链接数
with open(sourcedir, 'r') as f:
    sourceInline = f.readlines()
    with open(desinationdir, 'a+', newline='') as csvhandle:
        cWriter = csv.writer(csvhandle)
        header = ['时间','动作','登陆数']
        cWriter.writerow(header)
        sumcost=0
        for index, line in enumerate(sourceInline):
            time = re.match(r'\[(.*)\] \[', line)
            action = re.search(r'#player ', line)
            if action == None:
                continue
            res_list = []
            # other = deque(str(re.search(r'\/(.*)\)', line).group(1)).split('/'))
            # other = deque(str(re.search(r'\/(.*)\)', line).group(1)).split('/'))
            # other.popleft()
            maxlogin = deque(str(re.search(r'scatter:(.*)', line).group()).split())
            print(time.group(1))
            print(action.group())
            print(maxlogin)
        
            res_list.append(time.group(1))
            res_list.append(action.group())
            res_list.append(maxlogin.popleft())
          
            cWriter.writerow(res_list)
            print(res_list)
        
# 读取日活


