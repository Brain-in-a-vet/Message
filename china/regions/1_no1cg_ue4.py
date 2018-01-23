# coding:utf-8

import requests
import chardet
import sys
import re
import argparse
import codecs
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

#targetUrl='http://www.no1cg.com/CGjiaocheng/UnrealEngine/index'
targetUrl='http://www.no1cg.com/e/search/result/?searchid=2852'
targetFile="test.sql"
#user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
User_Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'  
headers = {'User-Agent' : User_Agent}  

sourceAid=int(1)
targetAid=int(6)

for i in range(sourceAid,targetAid):
    if(i==1):
        wbdata = requests.get(targetUrl+".html",headers=headers).text
    else:
        wbdata = requests.get(targetUrl+"_"+str(i)+".html",headers=headers).text
     
    soup = BeautifulSoup(wbdata,"lxml")
    for p in soup.select('div.list > ul > li'):
        a=p.select('a')[0] 
        img=a.select('img')[0]
        span=a.select('span')[0]
        ps="insert into ue4_enviroment(imgsrc,href,name) values("
        ps+="\'"+img.get("src")+"\',"
        ps+="\'"+a.get("href")+"\',"
        ps+="\'"+span.string.decode('ascii','ignore').encode('utf-8')+"\');"
        ps+="\n"
        print ps
        

