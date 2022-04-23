import requests
import os
import json
import re
from urllib.parse import urlparse
import time

e = 'deaddata2/info_saves'
x = 0
for filename in os.listdir(e):
    try:
        if '.json' in filename:
            file = os.path.join(e, filename)
            f = open(file)
            data = json.load(f)
            show = filename.replace('.json','')
            print(show)
            path = 'E:/deaddata/' + show
            isdir = os.path.isdir(path)
            if isdir == False:
                os.makedirs(path)
                for g in data['link_of_songs']:
                    #time.sleep(0.5)
                    a = urlparse(g)
                    v = os.path.basename(a.path)
                    doc = requests.get(g)
                    with open('E:/deaddata/' + show + '/' + v, 'wb') as f:
                        f.write(doc.content)
                        print(v)
                print()
                print()
                print()
                x += 1
                print(show + ' is done.' + str(x) + '/16127')
                print()
                print()
                print()
    except:
        pass

## Several shows are empty becuase they're commercially available. Several are also appearances on talk shows.