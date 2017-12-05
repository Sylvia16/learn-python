#!/bin/sh
find_all(){
    #考虑隐藏文件夹
    for file2 in `ls -a $1`
    do
        if [ x"$file2" != x"." -a x"$file2" != x".." ];then
            echo "$1/$file2"
            if [ -d "$1/$file2" ];then
                find_all "$1/$file2"
            fi
        fi
    done
}

find_regex(){
    regex="*traverse*"
#    echo $regex
#    能拿到符合所有正则的文件
#    echo `find $1 -name $regex`

    for file2 in `ls -a $1`
    do
        if [ x"$file2" != x"." -a x"$file2" != x".." ];then
#        echo `echo $file2|grep -e "traverse"`
            if [ -d "$1/$file2" ];then
                echo `echo $1/$file2|grep -e "traverse"`
                find_regex "$1/$file2"
            fi
        fi
    done
}

#find_all ../../algorithm

#先找到所有符合条件的文件
echo `find ../../algorithm -name "*traverse*"`
#find_regex ../../algorithm