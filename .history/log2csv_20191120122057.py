import re
import csv

sourcedir = 'server.2019-11-19.log.1'
desinationdir = sourcedir+'.csv'

# with open(sourcedir, 'r') as f:
#     sourceInline = f.readlines()
#     for index, line in enumerate(sourceInline):
#         time = re.match(r'^\[.*\]', line)
#         print(str(time.group()))


a = '[2019-11-19T00:01:03.057] [DEBUG] server - #del_material scatter:rita52ryin52 402 11700ee10a1c11ea9463c5ccbef617f4 makeequipcost'
b =  re.match(r'\[(.*)\] \[', a)
c = re.search(r'#(.*) scatter', a)
print(b.group(1))
print(c.group(1))
