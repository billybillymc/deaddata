import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
import time
df=pd.DataFrame()
data={}
ix=0
tp=100
textfile = open("a_file.txt", "r")
p=textfile.readlines()
for ps in p:
    response=requests.get(ps.replace("\n",""))
    soup=BeautifulSoup(response.content,"html.parser")
    songs=[]
    #getting text
    title=soup.find("h1",class_="sr-only")
    title=title.get_text().replace('\n    ','')
    t=title
    t=t.replace('?','').replace('\\','').replace('*','').replace('/','').replace('<','').replace('>','').replace('|>','').replace("\n",'')
    #getting name of songs
    name_of_songs=soup.find_all("meta",itemprop="name")
    i=0
    songs=[]
    for song in name_of_songs:
        i=i+1
        sin=song["content"]
        sin = sin.replace(' ->', '')
        songs.append(sin)
    #getting links
    d=[]
    final_list=[]
    linksy=soup.find_all("link",itemprop="associatedMedia")
    for linkst in linksy:
        d.append(linkst["href"])
    d=list(set(d))
    for r in range(0,len(d)):
        if "mp3" in d[r]:
            final_list.append(d[r])
    final_list=sorted(final_list)
    data={"title": title ,"link of concert":ps,"songs":songs,"link_of_songs":final_list}
    df=df.append(data,ignore_index=True)
    dfj=json.loads(df.to_json(orient="table",index=False))
    json_object=json.dumps(dfj,indent =4)
    try:
        with open(f"{t}.json", 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except:
        with open(f"title_missnaming.json", 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    time.sleep(1)
    ix=ix+1
    if ix==tp:
        tp=tp+100
        print(f"{ix} link is done")
    
        
