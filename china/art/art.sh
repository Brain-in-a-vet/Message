#!/bin/sh

#sed -i 's/_small//g' art
#while read line
#do
#    name=$(echo $line|awk '{print $1}')
#    imgsrc=$(echo $line|awk '{print $2}')
#    wget -O art_img/$name.jpg $imgsrc
#done<art
while read line
do
    name=$(echo $line|awk '{print $1}')
    path=$(echo $line|awk '{print $2}')
    python art_baidu_v2.py $name $path
done<baidu_girl
