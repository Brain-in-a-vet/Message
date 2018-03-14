# coding:utf-8

import requests
import chardet
import sys
import argparse
import codecs
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('gb2312')

# 融资事件
targetUrl=sys.argv[1]
#targetUrl = "http://www.newseed.cn/project/p1"
# 受资方	时间	轮次	金额	投资方
targetTitle="div.project-list > table.table-list > tbody > tr"

# 请求腾讯新闻的URL，获取其text文本
wbdata = requests.get(targetUrl).text

# 对获取到的文本进行解析
soup = BeautifulSoup(wbdata,'lxml')

# 从解析文件中通过select选择器定位指定的元素，返回一个列表
data = soup.select(targetTitle)
 
# 对返回的列表进行遍历
with codecs.open("data_project.txt",'a',encoding="gb2312") as f:
    for tr in data:
        isHead=tr.get('class');
        if isHead != None:
            continue
        trMsg=""
        for td in tr.children:
            if td.name != None:
                if "td2" == td.get('class')[0]:
                    trMsg+=td.a.get_text()+"#"
                if "td3" == td.get('class')[0]:
                    trMsg+=td.get_text()+"#"
                if "td4" == td.get('class')[0]:
                    trMsg+=td.get_text()+"#"
                if "td5" == td.get('class')[0]:
                    trMsg+= td.get_text()+"#"
        #print trMsg
        trMsg+="\n"
        f.write(trMsg)