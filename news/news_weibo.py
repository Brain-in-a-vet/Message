# coding:utf-8

import requests
import chardet
import sys
import re
import argparse
import codecs
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('gb2312')
 

targetUrl=sys.argv[1]
targetTitle=sys.argv[2]
targetName=sys.argv[3]
curTime=sys.argv[4]
targetFile=sys.argv[5]


user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
headers = { 'User-Agent' : user_agent }  
wbdata = requests.get(targetUrl,headers=headers).text


soup = BeautifulSoup(wbdata,"lxml")

news_titles = soup.find_all(href=re.compile(targetTitle),target="_blank")

with codecs.open(targetFile,'w',encoding="gb2312") as f:
    for n in news_titles:
        if n.string is not None :
            title = n.get_text()
            link=n.get("href")
            b=targetName+" <a href=\"http://s.weibo.com/"+link+"\">"+title+"</a><br/>"
            b+="\n"
            f.write(b)
            #print b
            
