#coding=utf-8
'''题目要求：现在有一个文件夹myDir，该文件夹中又有n个文件夹dir1,Dir2, ..., dir
N，每个文件夹中又有m个文件，这个实例需要达到的目的就是要将这n个文件夹dir1,D
ir2, ..., dirN中的所有文件全部写到一个新文件中，该新文件在文件夹myDir下。

1.找一个目录下的所有文件
2.将文件中的内容取出
3.将所有内容写入一个文件中
 '''

#不能运行
import os
import sys

path = '/home/linux/python/'
f = open('newfile.txt','a')
rootdir = os.path.join(path,'myDir')

def get_file(dirname):
    return os.listdir(rootdir + dirname) #获取当前文件夹下的所有文件

def get_content(filename):
    f = open(filename,'r+')
    return f.readlines()

def write_content(filename):
    r = open(filename,'r+')
    f.writelines(r.readlines())

for childir in rootdir:
    if os.path.isfile(rootdir + childir):
        pass
    else:
        filename = get_file(childir)
        for childfile in filename:
            filepath = os.path.join(rootdir,childir)
            write_content('filename')
