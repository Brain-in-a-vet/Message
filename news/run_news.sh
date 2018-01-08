#!/bin/bash

#curTime=$(date "+%Y%m%d%H%M%S")
curDate=$(date "+%Y%m%d")
curTime=$(date "+%Y%m%d%H%M")

baseDir=/opt/logs/python/news/

#-----------------------------------------
if [ ! -f $baseDir/Tencent.$curDate ] ; then
    touch $baseDir/Tencent.$curDate
fi
python news_tencent.py 'http://news.qq.com' 'div.text > em.f14 > a.linkto' 'Tencent' $curTime $baseDir/Tencent.$curTime
cat $baseDir/Tencent.$curTime >> $baseDir/Tencent.$curDate
rm -rf $baseDir/Tencent.$curTime

#-----------------------------------------
if [ ! -f $baseDir/WeiBo.$curDate ] ; then
    touch $baseDir/WeiBo.$curDate
fi
python news_weibo.py 'http://s.weibo.com/top/summary?cate=realtimehot' 'Refer=top' 'WeiBo' $curTime $baseDir/WeiBo.$curTime 
cat $baseDir/WeiBo.$curTime >> $baseDir/WeiBo.$curDate
rm -rf $baseDir/WeiBo.$curTime
