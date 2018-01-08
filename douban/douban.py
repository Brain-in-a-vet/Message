#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from lxml import etree
import requests
urls=['https://book.douban.com/top250?start={}'.format(str(i) for i in range(0, 226, 25))]
for url in urls:
    html=requests.get(url).content
    selector=etree.HTML(html)
    infos=selector.xpath('//tr[@class="item"]')
    for info in infos:
        book_name = info.xpath('td/div/a/@title')[0]
        book_url = info.xpath('td/div/a/@href')[0]
        published_infos = str(info.xpath('td/p/text()')[0])
        splitlistinfos = published_infos.split('/')
        #print splitlistinfos
        published_date=str(splitlistinfos[-2])
        #print published_date
        price = str(splitlistinfos[-1])
        #print price
        rate = info.xpath('td/div/span[2]/text()')[0]
        # comment_nums = info.xpath('td/div/span[3]/text()')[0]
        # print comment_nums
        comment_nums = info.xpath('td/div/span[3]/text()')[0].strip('(').strip().strip(')').strip().strip('人评价').strip() +'人评价'
        introduceinfo = info.xpath('td/p/span/text()')
        print book_name,book_url,published_date,price,rate,comment_nums,introduceinfo[0] if len(introduceinfo) > 0 else ''
