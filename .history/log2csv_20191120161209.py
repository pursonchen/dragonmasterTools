import re
import csv
from collections import deque
import sys

sourcedir = 'server.2019-11-19.log.1'  if len(sys.argv) == 0 else sys.argv[0]
print(sourcedir)
desinationdir = sourcedir+'.diamond.csv'

# 读取钻石
with open(sourcedir, 'r') as f:
    sourceInline = f.readlines()
    with open(desinationdir, 'a+', newline='') as csvhandle:
        cWriter = csv.writer(csvhandle)
        header = ['时间','动作','用户名','数值','余额','标记']
        cWriter.writerow(header)
        sumcost=0
        for index, line in enumerate(sourceInline):
            time = re.match(r'\[(.*)\] \[', line)
            action = re.search(r'#add_diamond', line)
            if action == None:
                continue
            res_list = []
            user = re.search(r'scatter:([1-5a-z]{0,12})', line)
            other = deque(str(re.search(r'scatter:.*', line).group()).split())
            other.popleft()
        
            res_list.append(time.group(1))
            res_list.append(action.group())
            res_list.append(user.group(1))
            res_list = res_list + list(other)
            cWriter.writerow(res_list)
            print(res_list)
        
# 读取日活


