# -*- coding:utf-8 -*-
import sys
import os

# 某些print的时候用到的end
print_end = '\r'

def getfile(dir_,ext = None):
    """
    获取特定路径下面的全部文件的路径
    :param dir_: 文件夹名
    :param ext: 文件后缀名
    :return: 文件路径组成的list
    """
    allfiles = []
    need_ext_filter = (ext is not None)
    for root,dirs,files in os.walk(dir_):
        for files_path in files:
            file_path = os.path.join(root, files_path)
            extension = os.path.splitext(file_path)[1][1:]
            if need_ext_filter and extension in ext:
                allfiles.append(file_path)
            elif not need_ext_filter:
                allfiles.append(file_path)
    return allfiles

def print_exception():
    """
    打印错误
    :return: 
    """
    e = sys.exc_info()
    print(f"Error '{e[1]}' happened on line {e[2].tb_lineno}")