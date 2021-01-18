#--------------------------------------------------------
#このブログラムは<doc  ~  /doc>
#を抜き出しデータベースに入れるプログラム
#xmlで抜き出しVersion2  pip install beautifulsoup4
#----------------------------------------------------------
import sqlite3
import codecs
from bs4 import BeautifulSoup
def db(title,contents):
    #conn = sqlite3.connect(r'D:\work2\wikipedia2.db')
    conn = sqlite3.connect(r'wikipedia2.db')
    
    c = conn.cursor()
    sql='insert into wikipedia(title,contents) values(?,?)'
    c.execute(sql,[title,contents])
    conn.commit()
    conn.close()
def wikiwrite2(path,d1,d2,str2):
    xml=open(path,"r", encoding='utf-8').read()
    j=1
    soup=BeautifulSoup(xml,'html.parser')
    for i in soup.find_all("doc"):
        print(i['title']) 
        db(i['title'],i.string)
        j=j+1
        print(d1,d2,str2,j)




#---------------
#BD28まで
#---------------  
# ALL
director1=["A","B"]
director2=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

director1=["A"]
director2=["A","B","C"]



path = "D:/work2/"
for i in director1:
    for j in director2:
        director3=i+j
        for k in range(0,100):
            if k<10:
                ii='0'+str(k)
            else:
                ii=str(k)    
            str2="/wiki_"+ii+""
            print("director1,director2",director1,director2)
            directory=path+director3+str2
            wikiwrite2(directory,director1,director2,str2)
