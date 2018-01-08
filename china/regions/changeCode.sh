#!/bin/sh


curDate=$(date "+%Y%m%d" -d "-1 days")
#curDate=$(date "+%Y%m%d" )

srcFile=$1

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
$(decoration $srcFile ./target.html)
