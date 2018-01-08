#!/bin/bash

#curTime=$(date "+%Y%m%d%H%M%S")
curDate=$(date "+%Y%m%d")
curTime=$(date "+%Y%m%d%H%M")

baseDir=/opt/logs/python/douban/

#-----------------------------------------
if [ ! -f $baseDir/DouBan.$curDate ] ; then
    touch $baseDir/DouBan.$curDate
fi
python douban.py 'https://book.douban.com/top250?start=' '' 'DouBan' $curTime $baseDir/DouBan.$curTime
 
cat $baseDir/DouBan.$curTime >> $baseDir/DouBan.$curDate
rm -rf $baseDir/DouBan.$curTime

