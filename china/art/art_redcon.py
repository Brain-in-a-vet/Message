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

targetUrl='http://so.redocn.com/s-d6d0b9fac3c0caf5b9dd-k-all-sheyingtu-----'

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
headers = { 'User-Agent' : user_agent }  

for i in range(1,6):
    wbdata = requests.get(targetUrl+str(i)+".htm",headers=headers).text
    soup = BeautifulSoup(wbdata,"lxml")
    for p in soup.find_all("img",attrs={'width':'204'}):
        name=p.get('alt').replace(' ','')
        imgsrc=p.get('src')
        print name+" "+imgsrc
    
