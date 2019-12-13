import re
import csv
from collections import deque
import sys
import json
import os

work_dir = '1213logs'
files = []
for parent, dirnames, filenames in os.walk(work_dir,  followlinks=True):
        for filename in filenames:
            file_path = os.path.join(parent, filename)
            print('文件名：%s' % filename)
            print('文件完整路径：%s\n' % file_path)
            files.append(file_path)
        desinationdir = '1108-1213.diamond.csv'
        for sourcedir in files:

                # 读取钻石
                with open(sourcedir, 'r') as f:
                    sourceInline = f.readlines()
                    with open(desinationdir, 'a+', newline='') as csvhandle:
                        with open("source1213.json", 'r') as user_source:
                            source_dict = json.load(user_source)
                            cWriter = csv.writer(csvhandle)
                            # header = ['时间','动作','用户名','数值','余额','标记','渠道']
                            # cWriter.writerow(header)
                            sumcost=0
                            for index, line in enumerate(sourceInline):
                                time = re.match(r'\[(.*)\] \[', line)
                                action = re.search(r'#add_diamond', line)
                                if action == None:
                                    continue
                                res_list = []
                                user = re.search(r'scatter:([1-5a-z\.]{0,12})', line)
                                other = deque(str(re.search(r'scatter:.*', line).group()).split())
                                other.popleft()

                                res_list.append(time.group(1).split('T')[0])
                                res_list.append(action.group())
                                res_list.append(user.group(1))
                                res_list = res_list + list(other)
                                res_list.append(source_dict[user.group(1)])
                                cWriter.writerow(res_list)
                                print(res_list)

# sourcedir = 'server.2019-11-19.log.1'  if len(sys.argv) == 1 else sys.argv[1]
# print(sourcedir)
# desinationdir = sourcedir+'.diamond.csv'
# desinationdir = '1108-1213.diamond.csv'

# # 读取钻石
# with open(sourcedir, 'r') as f:
#     sourceInline = f.readlines()
#     with open(desinationdir, 'a+', newline='') as csvhandle:
#         with open("source1213.json", 'r') as user_source:
#             source_dict = json.load(user_source)
#             cWriter = csv.writer(csvhandle)
#             header = ['时间','动作','用户名','数值','余额','标记','渠道']
#             cWriter.writerow(header)
#             sumcost=0
#             for index, line in enumerate(sourceInline):
#                 time = re.match(r'\[(.*)\] \[', line)
#                 action = re.search(r'#add_diamond', line)
#                 if action == None:
#                     continue
#                 res_list = []
#                 user = re.search(r'scatter:([1-5a-z]{0,12})', line)
#                 other = deque(str(re.search(r'scatter:.*', line).group()).split())
#                 other.popleft()
            
#                 res_list.append(time.group(1))
#                 res_list.append(action.group())
#                 res_list.append(user.group(1))
#                 res_list = res_list + list(other)
#                 res_list.append(source_dict[user.group(1)])
#                 cWriter.writerow(res_list)
#                 print(res_list)
        
# 读取日活


