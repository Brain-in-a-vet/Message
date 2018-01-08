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

targetUrl='http://www.fabang.com/a/20100907/174488.html'

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
headers = { 'User-Agent' : user_agent }  
wbdata = requests.get(targetUrl,headers=headers).text


print('DROP TABLE IF EXISTS `fangguanwebsite`;  ')
print('CREATE TABLE `fangguanwebsite` (  ')
print('  `province` varchar(50) NOT NULL,  ')
print('  `city` varchar(50) NOT NULL,  ')
print('  `website` varchar(50) NOT NULL, ')
print('  PRIMARY KEY  (`city`)  ')
print(') ENGINE=MyISAM  DEFAULT CHARSET=utf8 COMMENT=\'各省市房管网站信息表\';  ')
print('\n')

soup = BeautifulSoup(wbdata,"lxml")
i=0
for p in soup.select('div.content > p'):
    if(i==1):
        tname=""
        for s in p.children:
            if(s.name=="strong"):
                tname=s.string
            elif(s.name=="a"):
                ps="insert into fangguanwebsite values(\'"
                ps+=tname+"\',\'"
                ps+=s.string+"\',\'"
                ps+=s.get("href")+"\');"
                print(ps)
    i=i+1 
