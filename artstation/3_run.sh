#!/bin/sh
echo "">jobDetail
echo "">skill
echo "">company
while read line
do
    python 3_getD2.py $line 0 >>jobDetail
    echo "-------------------">>jobDetail
    
    python 3_getD2.py $line 1 >>skill
    echo "-------------------">>skill
    
    python 3_getD2.py $line 3 >>company
    echo "-------------------">>company
done<ajlist
