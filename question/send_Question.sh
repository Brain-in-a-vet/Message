#!/bin/sh


curDate=$(date "+%Y%m%d" -d "-1 days")

#------------------------------------------------------------------------
cat questionList | mailx -v -s "问题_$curDate" chunyuan2008@163.com

