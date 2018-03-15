#!/bin/sh

i=1
while true
do
    if [ $i -le 1523 ];then
        python invest.py "http://www.newseed.cn/invest/p$i"
        echo "$i Done"
        i=$(($i+1))
    else
    	break;
    fi
done

i=1
while true
do
    if [ $i -le 4016 ];then
        python project.py "http://www.newseed.cn/project/p$i"
        echo "$i Done"
        i=$(($i+1))
    else
    	break;
    fi
done

i=1
while true
do
    if [ $i -le 136 ];then
        python investor.py "http://www.newseed.cn/investor/p$i"
        echo "$i Done"
        i=$(($i+1))
    else
    	break;
    fi
done

i=1
while true
do
    if [ $i -le 634 ];then
        python vc.py "http://www.newseed.cn/vc/p$i"
        echo "$i Done"
        i=$(($i+1))
    else
    	break;
    fi
done
