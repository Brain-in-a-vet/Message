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

targetUrl='http://www.jmfdc.gov.cn/content.php?aid='
targetFile="test.sql"
#user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
User_Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'  
headers = {'User-Agent' : User_Agent}  


print('DROP TABLE IF EXISTS `fangHubeiJinmenYushou`;  ')
print('CREATE TABLE `fangHubeiJinmenYushou` (  ')
print('  `projectName` varchar(50) NOT NULL,  ')
print('  `projectAddress` varchar(100) NOT NULL,  ')
print('  `projectNo` varchar(50) NOT NULL, ')
print('  `projectArea` varchar(50) NOT NULL, ')
print('  `regTime` varchar(50) NOT NULL, ')
print('  PRIMARY KEY  (`projectNo`)  ')
print(') ENGINE=MyISAM  DEFAULT CHARSET=utf8 COMMENT=\'湖北荆州预售信息表\';  ')
print('\n')


sourceAid=int(262630)
targetAid=int(262646)

with codecs.open(targetFile,'w',encoding="utf-8") as f:
    for i in range(sourceAid,targetAid):
        wbdata = requests.get(targetUrl+str(i),headers=headers).text
        soup = BeautifulSoup(wbdata,"lxml")
        j=0
        for p in soup.select('table > tbody > tr'):
            if(j!=0):
                ps="insert into fangHubeiJinmenYushou values("
                for s in p.children:
                    ps+="\'"
                    ps+=s.string
                    ps+="\',"
                ps=ps[:-1]
                ps+=");"
                
                #print(ps)
                ps+="\n"
                f.write(ps)
            j=j+1 
