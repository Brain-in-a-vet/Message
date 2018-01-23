#!/bin/sh


curDate=$(date "+%Y%m%d" -d "-1 days")

#------------------------------------------------------------------------
question=""

while read line
do
 question+="$line                             "
 question+="                   "
done<questionList
echo "$question" | mailx -v -s "问题_$curDate" chunyuan2008@163.com

