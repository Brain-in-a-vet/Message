#!/bin/sh


curDate=$(date "+%Y%m%d" -d "-1 days")
#curDate=$(date "+%Y%m%d" )

logsBaseDir=/opt/logs/python/

newsBaseDir=/opt/logs/python/news/
doubanBaseDir=/opt/logs/python/douban/
msgBaseDir=/opt/logs/python/msg/


function decoration(){
    sourceFile=$1
    targetFile=$2
    echo "<!DOCTYPE html>" >> $targetFile
    echo "<head>" >> $targetFile 
    echo "<meta charset=utf-8/> " >> $targetFile  
    echo "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" /> " >> $targetFile 
    echo "</head>" >> $targetFile
    echo "<body>" >> $targetFile 
    cat $sourceFile|sort -u > $targetFile
    echo "</body>" >> $targetFile
    echo "</html>" >> $targetFile
}
#------------------------------------------------------------------------
$(decoration $newsBaseDir/Tencent.$curDate $newsBaseDir/Tencent_News_$curDate.html)
$(decoration $newsBaseDir/WeiBo.$curDate $newsBaseDir/WeiBo_News_$curDate.html)

$(decoration $doubanBaseDir/DouBan.20171227.Code $doubanBaseDir/DouBan_$curDate.html)

$(decoration $msgBaseDir/Msg_Unreal.$curDate $msgBaseDir/Msg_Unreal_$curDate.html)
$(decoration $msgBaseDir/Msg_PolyCount.$curDate $msgBaseDir/Msg_PolyCount_$curDate.html)

imgIndex=$(date +"%d" | awk '{if(substr($0,0,1)==0){print substr($0,2,1)}else{print $0}}')

echo "$curDate 新闻/阅读/资讯" | mailx -v -s "Info_$curDate" -a $newsBaseDir/Tencent_News_$curDate.html -a $newsBaseDir/WeiBo_News_$curDate.html -a $doubanBaseDir/DouBan_$curDate.html -a $msgBaseDir/Msg_Unreal_$curDate.html -a $msgBaseDir/Msg_PolyCount_$curDate.html -a ./picture/$imgIndex.jpg chunyuan2008@163.com

rm -rf $newsBaseDir/Tencent_News_$curDate.html 
rm -rf $newsBaseDir/WeiBo_News_$curDate.html
rm -rf $doubanBaseDir/DouBan_$curDate.html
rm -rf $msgBaseDir/Msg_Unreal_$curDate.html
rm -rf $msgBaseDir/Msg_PolyCount_$curDate.html
