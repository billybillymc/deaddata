from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import pandas as pd
import json
from bs4 import BeautifulSoup
import time
chromedriver_autoinstaller.install()
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
textfile = open("a_file.txt", "r")
p=textfile.readlines()
data={}
ix=0
tp=100
df=pd.DataFrame()
for ps in p:
    driver.get(ps.replace('\n',''))
    songs=[]
    ix=ix+1
    #getting text
    title=driver.find_element_by_xpath("//span[@itemprop='name']").text
    t=title
    t=t.replace('?','').replace('\\','').replace('*','').replace('/','').replace('<','').replace('>','').replace('|>','').replace("\n",'')
    #getting name of songs
    name_of_songs=driver.find_elements_by_xpath("//span[@class='ttl']")
    i=0
    songs=[]
    for song in name_of_songs:
        i=i+1
        sin=song.text
        songs.append(sin)
    #getting links
    d=[]
    final_list=[]
    soup=BeautifulSoup(driver.page_source,"lxml")
    linksy=soup.find_all("link",itemprop="associatedMedia")
    for linkst in linksy:
        d.append(linkst["href"])
    d=list(set(d))
    for r in range(0,len(d)):
        if "mp3" in d[r]:
            final_list.append(d[r])
    final_list=sorted(final_list)
    timee=[]
    runtimes=driver.find_elements_by_xpath("//span[@class='tm']")
    for runtime in runtimes:
        timee.append(runtime.text)
    data={"title": title ,"link of concert":ps,"songs":songs,"runtime":timee,"link_of_songs":final_list}
    df=df.append(data,ignore_index=True)
    dfj=json.loads(df.to_json(orient="table",index=False))
    json_object=json.dumps(dfj,indent =4)
    with open(f"New folder/{t}({ix}).json", 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    df=pd.DataFrame()
    time.sleep(1)
    if ix==tp:
        tp=tp+1000
        print(f"{ix} link is done")
