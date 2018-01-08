#!/bin/bash

#curTime=$(date "+%Y%m%d%H%M%S")
curDate=$(date "+%Y%m%d")
curTime=$(date "+%Y%m%d%H")

baseDir=/opt/logs/python/msg/

#-----------------------------------------
if [ ! -f $baseDir/Msg_Unreal.$curDate ] ; then
    touch $baseDir/Msg_Unreal.$curDate
fi
python msg_unreal.py 'https://www.unrealengine.com/zh-CN/blog' 'h2.headline > a.accent-hover-color' 'Unreal' $curTime $baseDir/Msg_Unreal.$curTime
cat $baseDir/Msg_Unreal.$curTime >> $baseDir/Msg_Unreal.$curDate
rm -rf $baseDir/Msg_Unreal.$curTime

if [ ! -f $baseDir/Msg_PolyCount.$curDate ] ; then
    touch $baseDir/Msg_PolyCount.$curDate
fi
python msg_polycount.py 'http://polycount.com/' '.Body > .Title > a[href^="/discussion"]' 'PolyCount' $curTime $baseDir/Msg_PolyCount.$curTime
cat $baseDir/Msg_PolyCount.$curTime >> $baseDir/Msg_PolyCount.$curDate
rm -rf $baseDir/Msg_PolyCount.$curTime
