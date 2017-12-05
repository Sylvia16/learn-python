#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Sylvia'

import os
import re
import fnmatch

'''遍历指定目录下的匹配所给正则表达式的目录及文件'''

'''正则re库
    http://funhacks.net/2016/12/27/regular_expression/ '''
def traverse_files(path=None, pattern=None):
    global dir_path
    global cr
    if path and path != 'None':
        dir_path = path
    else:
        return
    if pattern and pattern != 'None':
        cr = re.compile(pattern)
    else:
        return
    for filename in os.listdir(dir_path):
        # print filename
        if cr.search(filename) and not os.path.isdir(dir_path + '/' + filename):
            print os.path.join(dir_path, filename)
        if cr.search(filename) and os.path.isdir(dir_path + '/' + filename):
            print os.path.join(dir_path, filename)
            traverse_files(dir_path + '/' + filename, cr)


def find_all(path=None, pattern=None):
    if path and path != 'None':
        dir_path = path
    else:
        return
    if pattern and pattern != 'None':
        regex_pattern = pattern
    else:
        return
    for allpath, subdirs, files in os.walk(dir_path):
        for file in files:
            # print fnmatch.fnmatch(file, pattern.strip())
            if fnmatch.fnmatch(file, regex_pattern.strip()):
                print os.path.join(dir_path, file)
                if os.path.isdir(dir_path + '/' + file):
                    find_all(dir_path + '/' + file)

        for subdir in subdirs:
            if fnmatch.fnmatch(subdir, regex_pattern.strip()):
                print os.path.join(dir_path, subdir)


if __name__ == '__main__':
    path = "../../algorithm"
    # pattern = r'^t'
    #re正则匹配
    pattern = r'^t'
    traverse_files(path, pattern)


    #fnmatch通常用于文件名，拿通配符来匹配
    pattern = r'*traverse*'
    # print fnmatch.translate(pattern)
    find_all(path, pattern)
