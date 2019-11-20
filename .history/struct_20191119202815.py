import re

dir = '20191019154717-players-dump.txt'
userlist = []
jsonlist = []
with open(dir,'r') as f:
    sourceInline = f.readlines()
    for line in sourceInline:
        user = re.findall(r'(.+?) {', line)
        json = re.match(r'^{+$', line)
        print(json)
        if user != '':
            userlist.append(user)
            jsonlist.append(json)
    
