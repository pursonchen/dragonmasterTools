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
        print('read: '+line)
            
with open(desinationdir, 'a') as f:
    for index, user in enumerate(userlist):
        query = 'UPDATE `player` SET json={0} WHERE user={1} \n'.format(user.strip(),jsonlist[index])
        f.write(query)
        print('write: '+user[0])
    
    

    
