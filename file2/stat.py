#coding=utf-8
import os
import time
filename = raw_input('file name:')
file_stat = os.stat(filename)          # stat获取文件的相应属性信息
print file_stat
print time.localtime(file_stat.st_ctime)
