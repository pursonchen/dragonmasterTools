import re

sourcedir = '20191019154717-players-dump.txt'
desinationdir = sourcedir+'.sql'
userlist = []
jsonlist = []
with open(sourcedir,'r') as f:
    sourceInline = f.readlines()
    for line in sourceInline:
        user = re.findall(r'(.+?) {', line)
        json = re.sub(r'(.+?) ', '',line)
 
        userlist.append(user)
        jsonlist.append(json)
            
with open(desinationdir, 'w'):
    

    
