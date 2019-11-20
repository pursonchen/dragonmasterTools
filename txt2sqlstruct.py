import re
import sys

sourcedir = '20191019154717-players-dump.txt' if len(sys.argv) == 1 else sys.argv[1]
desinationdir = sourcedir+'.sql'
userlist = []
jsonlist = []
with open(sourcedir,'r') as f:
    sourceInline = f.readlines()
    for index, line in enumerate(sourceInline):
        user = re.findall(r'(.+?) {', line)
        json = re.sub(r'(.+?) ', '',line)
        if(len(user) == 0):
            continue
        userlist.append(user[0].strip())
        jsonlist.append(json.strip())
        print('read: '+str(index)+' '+user[0])
            
with open(desinationdir, 'a') as f:
    for index, user in enumerate(userlist):
        query = "UPDATE player SET json="'{0}'" WHERE user='{1}'; \n".format(jsonlist[index], user.strip())
        f.write(query)
        print('write: '+str(index)+' '+user)
    
    

    
